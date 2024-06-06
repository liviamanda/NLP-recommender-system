'''
=================================================================================================================================

Final Project

Team Members    :
- Livia Amanda Annafiah
- Alfarabi
- Badriah Nursakinah

Dataset         : https://www.kaggle.com/datasets/juhibhojani/airline-reviews/data
Hugging Face    : https://huggingface.co/spaces/liviamanda/FlightBuddy

Problem Statement :
Choosing the right airline can greatly affect a traveler's overall experience, including comfort, service quality, and in-flight amenities. With many online reviews available, airline passengers often rely on these reviews to make informed decisions about which airline to choose. However, the large number of reviews can make it difficult and time-consuming to read through and understand the general opinion about an airline.

FlightBuddy aims to solve this problem by using advanced Natural Language Processing (NLP) techniques to analyze airline reviews quickly and accurately. By processing and understanding a large number of reviews, FlightBuddy can determine whether the opinions in the reviews are positive or negative.

Objective :

The main goal of FlightBuddy is to improve the decision-making process for travelers by providing personalized airline recommendations based on the analysis of review sentiments. Specifically, FlightBuddy aims to:
- Analyze the sentiment of airline reviews to classify them as positive or negative, with accuracy serving as the metric.
- Recommend five airlines with similar positive characteristics for users who have seen favorable reviews.
- Suggest top-rated alternative airlines for users who have encountered negative experiences, ensuring they have better options for future travel.

=================================================================================================================================

'''

# Import libraries
import pandas as pd
import numpy as np
import psycopg2 as db
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from elasticsearch import Elasticsearch

def get_data():
    '''Fetches data from PostgreSQL and returns it as a DataFrame.
    
    Parameters:
        None
    
    Returns:
        None
    Usage example:
        df = get_data()
    '''
    
    db_name = 'finpro'
    db_user = 'airflow'
    db_password = 'airflow'
    db_host = 'postgres'
    db_port = '5432'
    
    # PostgreSQL connection string
    connection = db.connect(
        database = db_name,
        user = db_user,
        password = db_password,
        host = db_host,
        port = db_port)

    # Fetch data from the table 'table_m3'
    data = pd.read_sql("SELECT * FROM airline_reviews", connection)
    connection.close()
    
    # Save the data to CSV file
    data.to_csv('airline_reviews.csv')


def clean_data():
    '''Cleans data by dropping duplicates, standardizing column names, and handling missing values.
    
    Parameters:
        None
        
    Returns:
        None

    Usage example:
        df = clean_data()
    '''
    # Read data
    data = pd.read_csv('airline_reviews.csv')
    
    # Remove duplicate rows
    data = data.drop_duplicates()

    # Renaming column names
    data.columns = (data.columns
                    .str.lower()
                    .str.replace(' ', '_')
                    .str.replace('&', 'and'))

    # Function to impute missing values
    def impute_missing_values(data):
        for column in data.columns:
            # Numerical columns
            if data[column].dtype in ['float64', 'int64']:
                if data[column].skew() > 0.5 or data[column].skew() < -0.5:
                    # Highly skewed
                    median_value = data[column].median()
                    data[column] = data[column].fillna(median_value)
                else:
                    # Normally distributed
                    mean_value = data[column].mean()
                    data[column] = data[column].fillna(mean_value)

            # Categorical columns
            elif data[column].dtype == 'object':
                mode_value = data[column].mode()[0]
                data[column] = data[column].fillna(mode_value)

    # Impute missing values
    impute_missing_values(data)
    
    # Save the cleaned data to a new CSV file
    data.to_csv('airline_reviews_clean.csv', index=False)
    
def convert_data():
    '''Converts the cleaned data into a new CSV file containing rating columns only for recommendation system.
    
    Parameters:
        None
        
    Returns:
        None

    Usage example:
        convert_data()
    '''
    # Read cleaned data
    data = pd.read_csv('airline_reviews_clean.csv')
    
    # Group by airline_name and calculate the average ratings
    avg_ratings = data.groupby('airline_name').agg({
        'seat_comfort': 'mean',
        'cabin_staff_service': 'mean',
        'food_beverages': 'mean',
        'ground_service': 'mean',
        'inflight_entertainment': 'mean',
        'wifi_connectivity': 'mean',
        'value_for_money': 'mean'
    }).reset_index()
    
    # Rename columns to match the required output
    avg_ratings.columns = [
        'airline_name', 
        'avg_seat_comfort', 
        'avg_cabin_staff_service', 
        'avg_food_beverages', 
        'avg_ground_service', 
        'avg_inflight_entertainment', 
        'avg_wifi_connectivity', 
        'avg_value_for_money']
    
    # Save the average ratings to a new CSV file
    avg_ratings.to_csv('rating_table.csv', index=False)
    
def insert_data():
    '''Inserts the cleaned data into Elasticsearch.
    
    Parameters:
        None
        
    Returns:
        None

    Usage example:
        insert_data()
    '''

    # Read data
    data = pd.read_csv('airline_reviews_clean.csv')
    
    # Define Elasticsearch
    es = Elasticsearch('http://elasticsearch:9200')
    print('Connection status: ', es.ping())

    for i, r in data.iterrows():
        doc = r.to_json()
        res = es.index(index="finpro", doc_type="doc", body=doc)
        print(res)

# Define default arguments for the DAG
default_args = {'owner': 'group2',
                'start_date': datetime(2024, 6, 4),
                'retries': 3,
                'retry_delay': timedelta(minutes=1),}

# Define the DAG with the given name, default arguments, and schedule interval
with DAG ('flightBuddy',
          default_args = default_args,
          schedule_interval = '0 0 1 * *') as dag:
    
          # First task : calling 'get_data' function
          getData = PythonOperator(task_id = 'GetData',
                                   python_callable = get_data)
          
          # Second task : calling 'clean_data' function
          cleanData = PythonOperator(task_id = 'CleanData',
                                     python_callable = clean_data)
          
          # Third task : calling 'rating_table' function
          convertData = PythonOperator(task_id = 'convertData',
                                     python_callable = convert_data)

          # Third task : calling 'insert_data' function
          insertData = PythonOperator(task_id = 'InsertData',
                                      python_callable = insert_data)

# Set up the task dependencies
getData >> cleanData >> convertData >> insertData