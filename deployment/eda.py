# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Define custom color palette
custom_palette = px.colors.qualitative.Set3

# Function to generate word cloud
def generate_wordcloud(text, title, ax):
    if text.strip():
        wordcloud = WordCloud(width=400, height=200, background_color='white').generate(text)
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.set_title(title, size=15)
        ax.axis('off')
    else:
        ax.text(0.5, 0.5, 'No words available', horizontalalignment='center', verticalalignment='center', size=15, color='red')
        ax.set_title(title, size=15)
        ax.axis('off')

# Create the main program
def run():
    # Load the dataset
    data = pd.read_csv('airline_review_cleaned.csv')
    
    # Add title to the app
    st.title('Exploratory Data Analysis')
    
    # Checkbox to display raw data
    if st.checkbox('Show raw data'):
        st.markdown('#### Raw Data')
        st.write(data)
    
    # Dropdown for different analysis options
    option = st.selectbox('Select Analysis', ('Overview', 'Distribution Plots', 'Categorical Analysis', 'Correlation Heatmap', 'Word Cloud'))
    
    # Overview analysis
    if option == 'Overview':
        st.subheader('Dataset Overview')
        st.write('This dataset contains reviews from airline passengers along with their ratings on various aspects of the flight.')
        st.markdown('###### Summary Statistics')
        numerical_columns = data[['seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money']]
        st.write(numerical_columns.describe())
        st.markdown('''The statistical description of the dataset reveals several insights: The columns `Seat Comfort`, `Cabin Staff Service`, `Food & Beverages`, `Ground Service`, `Inflight Entertainment`, `Wifi & Connectivity`, and `Value For Money` exhibit varying means, indicating differences in satisfaction levels across these aspects. The standard deviations suggest differing degrees of dispersion or variability in ratings across these aspects. The minimum and maximum values reflect the range of ratings given by reviewers, spanning from 0 to 5. Additionally, the quartiles (25th, 50th, and 75th percentiles) provide a snapshot of the distribution of ratings, highlighting median values and the spread of data around these central values.''')
    
    # Distribution plots analysis
    elif option == 'Distribution Plots':
        st.subheader('Distribution of Numerical Variables')
        numerical_columns = st.multiselect('Select columns to visualize', ['seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money'], 
                                           ['seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money'])
        
        # Add insight for each variable
        column_descriptions = {
            'seat_comfort': "The highest frequency of ratings appears at 1.0, suggesting a lot of passengers find the seats uncomfortable. However, a significant number of reviews also gather around the 3.0 to 4.0 marks, indicating some level of satisfaction among other passengers.",
            'cabin_staff_service': "This category has pronounced peaks at both 1.0 and 5.0. It seems that passengers are divided, with many experiencing poor service while an equal number feel highly satisfied.",
            'food_and_beverages': 'The peak at 1.0 suggests widespread dissatisfaction with the food and beverages, though the distribution across other rating values is fairly even, indicating a mix of opinions.',
            'ground_service': 'Ratings mostly start high at 1.0, with fewer complaints as the ratings go higher, showing that dissatisfaction is more common, but there is an upward trend towards satisfaction among fewer passengers.',
            'inflight_entertainment':'The peak at 2.0, closely followed by 1.0, suggests that the inflight entertainment does not generally meet passengers’ expectations, though it seems slightly more favorable than the lowest rating.',
            'wifi_and_connectivity': 'Dominantly, ratings are clustered at 1.0, with minimal higher ratings, highlighting a general dissatisfaction with internet services on flights.',
            'value_for_money': "Most ratings cluster at 1.0, indicating a perception of poor value for money, yet there's a notable peak at 5.0 as well, suggesting that some passengers perceive great value."
            }
        
        for idx, col in enumerate(numerical_columns):
            fig = px.histogram(data, x=col, title=f'Distribution of {col.title().replace("_", " ")}', nbins=30, color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
            st.markdown(column_descriptions[col])
    
    # Categorical analysis
    elif option == 'Categorical Analysis':
        st.subheader('Categorical Data Analysis')
        categorical_columns = st.multiselect('Select columns to visualize', ['verified', 'type_of_traveller', 'seat_type', 'recommended'], 
                                             ['verified','type_of_traveller','seat_type', 'recommended'])
        
        # Add insight for each variable
        column_descriptions = {
            'verified': "The number of verified reviews is slightly higher than unverified reviews. This shows that the majority of users prefer to leave verified reviews.",
            'type_of_traveller': "The majority of reviews come from solo leisure travelers, followed by couple leisure travelers. Business travelers and family leisure travelers contribute fewer reviews, with business travelers being the least frequent.",
            'seat_type': "The vast majority of reviews are from passengers in economy class, with a significant margin compared to business class, premium economy, and first class. This suggests that economy class is the dominant choice for travelers.",
            'recommended': "More reviews do not recommend the airline compared to those that do. This may indicate that there are issues or dissatisfaction among many users with the services provided by the airline."
        }
        for idx, col in enumerate(categorical_columns):
            fig = px.histogram(data, x=col, title=f'{col.title().replace("_", " ")} Distribution', color_discrete_sequence=[custom_palette[idx]])
            st.plotly_chart(fig)
            st.markdown(column_descriptions[col])

    # Word cloud analysis
    elif option == 'Word Cloud':
        st.subheader('Word Cloud Analysis')
        
        wordcloud_options = st.multiselect('Select Word Cloud', ['All Reviews', 'Recommended (Yes)', 'Recommended (No)'], ['All Reviews'])
        
        if wordcloud_options:
            for wordcloud_option in wordcloud_options:
                fig, ax = plt.subplots(figsize=(10, 5))
                
                if wordcloud_option == 'All Reviews':
                    all_text = ' '.join(data['review'].dropna())
                    generate_wordcloud(all_text, 'Word Cloud - All Reviews', ax)
                    st.pyplot(fig)
                    st.markdown('''In the word cloud for all reviews, the most prominent words are `flight,` `airline,` `seat,` `time,` `check,` `plane,` and `staff.` These words suggest that passengers commonly discuss aspects of the flight itself, including timing and seating arrangements, as well as interactions with airline staff and the overall airline experience.''')
                elif wordcloud_option == 'Recommended (Yes)':
                    recommended_yes_text = ' '.join(data[data['recommended'] == 'yes']['review'].dropna())
                    generate_wordcloud(recommended_yes_text, 'Word Cloud - Recommended (Yes)', ax)
                    st.pyplot(fig)
                    st.markdown('''In the word cloud for recommended reviews, the dominant words include `flight,` `seat,` `time,` `good,` `service,` `staff,` and `airline.` Positive reviews emphasize `good` and `service,` indicating that passengers who recommend the airline often appreciate the quality of service, the condition of seats, and the timely operation of flights.''')
                elif wordcloud_option == 'Recommended (No)':
                    recommended_no_text = ' '.join(data[data['recommended'] == 'no']['review'].dropna())
                    generate_wordcloud(recommended_no_text, 'Word Cloud - Recommended (No)', ax)
                    st.pyplot(fig)
                    st.markdown('''For not recommended reviews, the key words are `flight,` `check,` `time,` `seat,` `service,` `staff,` and `airport.` Negative reviews focus on issues such as the check-in process, waiting times, and customer service problems. The prominence of `check` and `time` indicates dissatisfaction with delays and the efficiency of airline operations.''')

    # Correlation heatmap analysis
    elif option == 'Correlation Heatmap':
        st.subheader('Correlation Heatmap')
        numerical_columns = data[['seat_comfort', 'cabin_staff_service', 'food_and_beverages', 'ground_service', 'inflight_entertainment', 'wifi_and_connectivity', 'value_for_money']]
        corr = numerical_columns.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1, ax=ax)
        st.pyplot(fig)
        st.markdown('''The correlation heatmap reveals key relationships between different aspects of passenger satisfaction: There is a strong positive correlation (0.71) between seat comfort and perceived value for money, indicating that comfortable seating significantly enhances passengers' perception of value. Service categories such as cabin staff service, food and beverages, and ground service show strong correlations (around 0.6 to 0.7) with each other, suggesting that satisfaction in one area tends to align with satisfaction in others. WiFi and connectivity show weaker correlations (around 0.2 to 0.4) with other metrics, indicating they have less impact on overall passenger satisfaction. Inflight entertainment has a moderate influence, with some correlations to other services, suggesting it plays a contributing but not dominant role in overall satisfaction. Overall, the heatmap suggests that focusing on improving seat comfort and integrated service quality could notably enhance overall passenger satisfaction.''')

# Run the app
if __name__ == '__main__':
    run()
