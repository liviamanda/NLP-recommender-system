<a name="readme-top"></a>

<div align='center'>
    <h1><b>FlightBuddy</b></h1>
    <img src='deployment/companyLogo.png'/>
    <br><br>
    <p>This project is focused on creating a Natural Language Processing (NLP) model that can determine if reviews are positive or negative (performing sentiment analysis) and provide recommendations based on the results.</p>
    <br>

![Python](https://badgen.net/badge/Python/3.9.18/blue?)
![Streamlit](https://badgen.net/badge/Streamlit/1.10.0/orange?)
![Pandas](https://badgen.net/badge/Pandas/1.4.3/blue?)
![Seaborn](https://badgen.net/badge/Seaborn/0.11.2/green?)
![Matplotlib](https://badgen.net/badge/Matplotlib/3.5.2/blue?)
![Scikit-learn](https://badgen.net/badge/scikit-learn/1.4.2/yellow?)
![Plotly](https://badgen.net/badge/Plotly/5.22.0/cyan?)
![TensorFlow](https://badgen.net/badge/TensorFlow/2.15.0/orange?)
![WordCloud](https://badgen.net/badge/WordCloud/1.8.1/purple?)
![NLTK](https://badgen.net/badge/NLTK/3.7/red?)
![Docker](https://badgen.net/badge/Docker/20.10/cyan?)

</div>

---

## 🧑‍💻 **Team Members**

- **Livia Amanda Annafiah**
  - Role: Data Scientist and Data Engineer  
  - [Github](https://github.com/liviamanda) | [LinkedIn](https://www.linkedin.com/in/liviaamanda/)

- **Alfarabi**
  - Role: Data Analyst and Data Scientist  
  - [Github](https://github.com/Alfarabi58) | [LinkedIn](https://www.linkedin.com/in/alfa-rabi-49b9b8285/)
  
- **Badriah Nursakinah**
  - Role: Data Analyst  
  - Github | [LinkedIn](https://www.linkedin.com/in/badriah-nursakinah-s-t-m-kom-247b20159/)

<br />

## 💾 **Dataset**

The dataset is obtained from a credible source and comprises relevant details regarding airline reviews. For further information or to access the dataset, please refer to the provided source [here](https://www.kaggle.com/datasets/juhibhojani/airline-reviews/data).

<br />

## ⚠️ **Problem Statement**

Choosing the right airline can greatly affect a traveler's overall experience, including comfort, service quality, and in-flight amenities. With many online reviews available, airline passengers often rely on these reviews to make informed decisions about which airline to choose. However, the large number of reviews can make it difficult and time-consuming to read through and understand the general opinion about an airline.

FlightBuddy aims to solve this problem by using advanced Natural Language Processing (NLP) techniques to analyze airline reviews quickly and accurately. By processing and understanding a large number of reviews, FlightBuddy can determine whether the opinions in the reviews are positive or negative.

<br />

## 📌 **Objective**

The main goal of FlightBuddy is to improve the decision-making process for travelers by providing personalized airline recommendations based on the analysis of review sentiments. Specifically, FlightBuddy aims to:
- Analyze the sentiment of airline reviews to classify them as positive or negative, with accuracy serving as the metric.
- Recommend five airlines with similar positive characteristics for users who have seen favorable reviews.
- Suggest top-rated alternative airlines for users who have encountered negative experiences, ensuring they have better options for future travel.

<br />

---

## 🗒️ **Setup and Installation**

To get started with FlightBuddy, ensure you have the following prerequisites:

- **Dataset**: Accessible [here](https://www.kaggle.com/datasets/juhibhojani/airline-reviews/data).
- **Python**: Version 3.9.18 or later.
- **Docker**: Version 20.10 or later for container deployment.

### **Environment Configuration**  
Ensure you have all necessary Python packages by installing them from the provided `requirements.txt`. Also, ensure Docker is set up if you prefer containerized environments.

### **Project Setup**  
Follow these steps to set up the project:

1. **Clone the Repository**
   Clone this repository to your local machine. Choose the method that best suits your setup:
   - **HTTPS**:
     ```
     git clone https://github.com/FTDS-assignment-bay/p2-final-project-flightbuddy/
     ```
   - **SSH**:
     ```
     git clone git@github.com:FTDS-assignment-bay/p2-final-project-flightbuddy.git
     ```

2. **Compose Docker Containers (Optional)**  
   If you prefer using Docker, build and run the Docker container as follows:
```
docker build -t flightbuddy-app .
docker run -it flightbuddy-app
```


3. **Environment Setup**  
- Navigate to the cloned directory:
  ```
  cd p2-final-project-flightbuddy
  ```
- Set up a virtual environment (optional but recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # On MacOS/Linux
  .\venv\Scripts\activate   # On Windows
  ```
- Install the required dependencies:
  ```
  pip install -r requirements.txt
  ```

4. **Run the Application**  
Execute the main application script:
```
python app.py
```

5. **Access and Use**  
After starting the application, you can access and interact with it as specified in your project documentation.

### **Additional Resources**  
For further exploration or modifications, access the full project documentation and source code on the [GitHub repository](https://github.com/FTDS-assignment-bay/p2-final-project-flightbuddy/).

By following these setup instructions, you'll be able to replicate the FlightBuddy project and explore its functionalities related to analyzing airline review sentiments.

---

## 💻 **Tools and Libraries**

![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-%238DD6F9.svg?style=for-the-badge&logo=seaborn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23D00000.svg?style=for-the-badge&logo=matplotlib&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-%232376C6.svg?style=for-the-badge&logo=nltk&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![WordCloud](https://img.shields.io/badge/WordCloud-%23FF8800.svg?style=for-the-badge&logo=wordcloud&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-%23157AF6.svg?style=for-the-badge&logo=textblob&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white)

<br />

## 🔄 **Workflow**
- Data Analyst (DA): Responsible for creating visualizations to provide insights from the data.
- Data Scientist (DS): Develops the NLP model and the recommender system, and handles deployment using Streamlit.
- Data Engineer (DE): Manages databases, manipulates data in PostgreSQL, and schedules tasks using Elasticsearch.

<br />

## 📂 **File Descriptions**
- final_project_DAG.py: Contains the engineering workflows and pipelines.
- final_project_NLP.ipynb: Notebook for developing the NLP model, including training and preprocessing.
- final_project_NLP_inference.ipynb: Notebook for testing the NLP model with unseen data.
- final_project_query_recsys.sql: SQL script for manipulating tables for the recommender system.
- final_project_recsys.ipynb: Notebook for developing the recommender system.

<br />

## 🚀 **Deployment**
The application is deployed on Hugging Face Spaces. Access it using the following link:
[FlightBuddy on Hugging Face](https://huggingface.co/spaces/liviamanda/FlightBuddy)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





