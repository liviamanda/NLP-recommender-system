import eda, predict
import streamlit as st

# Add side bar for navigation
navigation = st.sidebar.selectbox('Navigation', ['Home', 'Exploratory Data Analysis', 'Review Prediction'])

st.sidebar.markdown('# About')

# Introduction
st.sidebar.write('''This tool is designed to explore and predict airline reviews. It employs advanced data analysis and machine learning models to offer insights and predictions that can assist users in understanding and analyzing airline reviews.''')

# Features
st.sidebar.write('''### Key Features:
- **Exploratory Data Analysis**: Analyze the data to uncover patterns and insights related to airline reviews.
- **Review Predictor**: Use predictive models to forecast the sentiment of airline reviews.''')

# Target Audience
st.sidebar.write('''### Who can benefit?
- **Travelers**: Understand sentiments about airlines from various reviews.
- **Airline Companies**: Analyze and improve customer satisfaction based on reviews.
- **Data Scientists**: Develop and evaluate machine learning models for review sentiment prediction.''')

# Tools
st.sidebar.write('''### Tools Utilized:
- `Python`: For backend operations and model computations.
- `Streamlit`: For creating this interactive web application.
- `TensorFlow/Keras`: For implementing machine learning models.''')

# Define the Home Page
def show_home():
    st.image('companyLogo.png')
    st.write('')
    st.write('''This application is specifically designed to facilitate both exploratory data analysis and predictive modeling regarding airline reviews. It provides users with advanced analytical tools that help in understanding trends and patterns within the data. To begin, please use the navigation menu on the left side of the screen to select the particular module that you intend to explore. Whether you're looking to uncover insights or forecast future trends, this tool equips you with the necessary resources to effectively analyze the feedback from airline passengers.''')
    st.markdown('---')
    
    # Dataset section
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('1.png', use_column_width=True)
    with col2:
        st.markdown('### Dataset')
        st.markdown('''The dataset is obtained from a credible source and comprises relevant details regarding airline reviews. For further information or to access the dataset, please refer to the provided source [Airline Reviews](https://www.kaggle.com/datasets/juhibhojani/airline-reviews/data).''')
    
    # Problem Statement section
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image('2.png', use_column_width=True)
    with col2:
        st.markdown('### Problem Statement')
        st.markdown('''Choosing the right airline can greatly affect a traveler's overall experience, including comfort, service quality, and in-flight amenities. With many online reviews available, airline passengers often **rely on these reviews** to make informed decisions about which airline to choose. However, the large number of reviews can make it difficult and **time-consuming** to read through and understand the general opinion about an airline.''')
        st.markdown('''**FlightBuddy** aims to solve this problem by using advanced Natural Language Processing (NLP) techniques to analyze airline reviews quickly and accurately. By processing and understanding a large number of reviews, FlightBuddy can determine whether the opinions in the reviews are positive or negative.''')
    
    # Objective section
    st.write('')
    st.write('')
    st.write('')
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image('3.png', use_column_width=True)
    with col2:
        st.markdown('### Objective')
        st.markdown('''The main goal of **FlightBuddy** is to improve the decision-making process for travelers by providing personalized airline recommendations based on the analysis of review sentiments. Specifically, FlightBuddy aims to:

- Analyze the sentiment of airline reviews to classify them as positive or negative, with accuracy serving as the metric.
- Recommend five airlines with similar positive characteristics for users who have seen favorable reviews.
- Suggest top-rated alternative airlines for users who have encountered negative experiences, ensuring they have better options for future travel.''')

if navigation == 'Home':
    show_home()
elif navigation == 'Exploratory Data Analysis':
    eda.run()
elif navigation == 'Review Prediction':
    predict.run()