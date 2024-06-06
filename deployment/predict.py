# Import necessary libraries
import pandas as pd
import numpy as np
import streamlit as st
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from time import sleep

# Download necessary NLTK resources for text processing
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load English stopwords and extend with custom list for better filtering
stopwords_eng = set(stopwords.words('english'))
additional_stopwords = ['the', 'to', 'and', 'I', 'was', 'a', 'in', 'of', 'for', 'on', 'flight', 'with', 'that', 'my', 'is', 'not', 'were', 'they',
                        'The', 'at', 'we', 'had', 'from', 'but', 'have', 'it', 'this', 'no', 'as', 'me', 'you', 'our', 'be', 'are', 'an', 'very', 'so',
                        'service', 'their', 'We', 'time', 'airline', 'would', 'or', 'us', 'by', 'only', 'get', 'all', 'which']
stopwords_eng.update(additional_stopwords)

# Load the pre-trained logistic regression model
model_path = os.path.join('unzipped_model', 'model_logreg')
model = load_model(model_path)

# Define a WordNet lemmatizer for text normalization
lemmatizer = WordNetLemmatizer()

# Load datasets
df = pd.read_csv('avg_ratings_per_airline.csv')
raw = pd.read_csv('airline_review_cleaned.csv')

# Define a function for preprocessing text for analysis
def preprocess_text(text):
    # Lowercasing, removing URLs, hashtags, digits, and non-letter characters
    text = text.lower()  
    text = re.sub(r'https?://(?:www\.[^\s\n\r]+|[^\s\n\r]+)', '', text) 
    text = re.sub(r'#', '', text)  
    text = re.sub(r'[\n\r]', '', text)  
    text = re.sub(r'\d+', '', text)  
    text = re.sub("[^A-Za-z\s']", " ", text)  
    tokens = word_tokenize(text)  
    tokens = [word for word in tokens if word not in stopwords_eng]  
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  
    return ' '.join(tokens)  

# Normalize the ratings data using standard scaler
scaler = StandardScaler()
rating_columns = ['avg_seat_comfort', 'avg_cabin_staff_service', 'avg_food_beverages', 'avg_ground_service',
                  'avg_inflight_entertainment', 'avg_wifi_connectivity', 'avg_value_for_money']
normalized_data = scaler.fit_transform(df[rating_columns])

# Compute cosine similarity among airlines based on ratings
similarity_matrix = cosine_similarity(normalized_data)
similarity_df = pd.DataFrame(similarity_matrix, index=df['airline_name'], columns=df['airline_name'])

# Functions to recommend similar airlines based on reviews
def recommendation_positive(airline, n_recommendations=5):
    similar_scores = similarity_df[airline].sort_values(ascending=False)
    similar_scores = similar_scores.drop(airline)
    similar_scores.reset_index(drop=True, inplace=True)
    top_positive_airlines = similar_scores.head(n_recommendations)
    top_airlines_with_names = df.loc[top_positive_airlines.index, 'airline_name']
    return pd.DataFrame({'Airline': top_airlines_with_names.values, 'Similarity Score': top_positive_airlines.values})

# Functions to recommend top 5 airlines based on reviews
def recommendation_negative(airline, n_recommendations=5):
    mean_ratings = df[rating_columns].mean(axis=1)
    top_airlines = mean_ratings.nlargest(n_recommendations)
    top_airlines_with_names = df.loc[top_airlines.index, 'airline_name']
    return pd.DataFrame({'Airline': top_airlines_with_names.values, 'Mean Rating': top_airlines.values})

# Main function to run the Streamlit application
def run():
    st.title('Airplane Review')
    st.markdown('---')
    
    # User input for review details
    with st.expander("Enter Review Details"):
        col1, col2 = st.columns(2)
        with col1:
            airline = st.selectbox("Select an Airline", df['airline_name'])
            aircraft = st.text_input("Aircraft Model", help="Enter the model of the aircraft you flew with. Skip if you don't know")
            type_of_traveller = st.selectbox('Type of Traveller', raw['type_of_traveller'].unique(), help="Choose the type of traveller you were during the flight.")
        with col2:
            seat_type = st.selectbox('Type of Seat', raw['seat_type'].unique(), help="Choose the type of seat you had during the flight.")
            route = st.text_input("Route", help="Enter the route of your travel, from departure to destination. Ex: Frankfurt to Pristina")
            date_flown = st.date_input("Date Flown", help="Select the date when you flew.")

    # User input for rating experience
    with st.expander("Rate Your Experience"):
        col1, col2 = st.columns(2)
        with col1:
            seat_comfort = st.slider('Seat Comfort', 0, 5, help="Rate the comfort of your seat.")
            cabin_staff_service = st.slider('Cabin Staff Service', 0, 5, help="Rate the cabin staff service.")
            food_and_beverages = st.slider('Food & Beverages', 0, 5, help="Rate the quality of food and beverages.")
            ground_service = st.slider('Ground Service', 0, 5, help="Rate the quality of ground service.")
        with col2:
            inflight_entertainment = st.slider('Inflight Entertainment', 0, 5, help="Rate the inflight entertainment.")
            wifi_and_connectivity = st.slider('WiFi Connectivity', 0, 5, help="Rate the WiFi connectivity.")
            value_for_money = st.slider('Value for Money', 0, 5, help="Rate the overall value for money.")

    # Form for submitting reviews
    with st.form(key='review_sentiment_detect'):
        st.write("### Provide Your Feedback")
        review_title = st.text_input("Title of Your Review:", help="Enter a brief title for your review.")
        review_text = st.text_area("Your Review:", help="Write your detailed review here.")
        submitted = st.form_submit_button('Analyze Feedback')
        
        if submitted:
            
                    # Add progression
            bar = st.progress(0)
            for percent_complete in range(101):
                sleep(0.005)
                bar.progress(percent_complete)
        
            if not review_text.strip():
                st.error("Please fill in the review text field to submit your feedback.")
            else:
                processed_text = preprocess_text(review_text)
                input_data = {'text': processed_text}
                input_df = pd.DataFrame([input_data])
                prediction = model.predict(input_df['text'])
                predicted_label = np.argmax(prediction)
                
                if predicted_label == 0:
                    st.error("Negative Feedback - Not Recommended")
                    st.write("We're sorry you had a less than ideal experience. Based on our analysis, here are the top 5 airlines that might better meet your expectations and provide a superior experience, ensuring you have better options for your future travels:")
                    st.subheader("Top 5 Airlines Recommendations:")
                    similar_airlines = recommendation_negative(airline)
                    st.write(similar_airlines)
                elif predicted_label == 1:
                    st.success("Positive Feedback - Recommended")
                    st.write("Since you've had a positive experience with this airline, you might also enjoy flying with these top-rated airlines that share similar positive characteristics. This recommendation aims to further enhance your travel options and ensure you continue to have great flying experiences:")
                    st.subheader("Similar Airlines Recommendations:")
                    similar_airlines = recommendation_positive(airline)
                    st.write(similar_airlines)

                # Thank you note at the end of the interaction
                st.markdown("### Thank You for Using FlightBuddy!")
                st.write("We appreciate you taking the time to provide feedback and hope our tool has helped enhance your travel planning and decision-making process. Safe travels and we look forward to assisting you again!")
                    
if __name__ == '__main__':
    run()
