#pip install streamlit pandas scikit-learn seaborn matplotlib plotly

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load Dataset
try:
    df = pd.read_csv('diabetes.csv')
except FileNotFoundError:
    st.error('Dataset not found. Please make sure diabetes.csv is in the same folder.')
    st.stop()

# App Title
st.title('🩺 Diabetes Checkup')
st.sidebar.header('Patient Data')

# Display basic statistics
st.subheader('📊 Training Data Stats')
st.write(df.describe())

# Feature selection
X = df.drop(['Outcome'], axis=1)
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Function to get sidebar input
def user_input_features():
    pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
    glucose = st.sidebar.slider('Glucose', 0, 200, 120)
    bp = st.sidebar.slider('Blood Pressure', 0, 122, 70)
    skinthickness = st.sidebar.slider('Skin Thickness', 0, 100, 20)
    insulin = st.sidebar.slider('Insulin', 0, 846, 79)
    bmi = st.sidebar.slider('BMI', 0.0, 67.0, 20.0)
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0, 2.5, 0.47)
    age = st.sidebar.slider('Age', 21, 88, 33)

    data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': bp,
        'SkinThickness': skinthickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }
    return pd.DataFrame(data, index=[0])

# Get input
user_data = user_input_features()

# Display patient data
st.subheader('Patient Data')
st.write(user_data)

# Train model
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Predict
user_result = rf.predict(user_data)
st.write(f"Prediction Raw Output: {user_result}")  # Debug line to check result (0 or 1)

# Visualise comparisons
st.subheader('Visualised Patient Report')
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction']
for feature in features:
    fig = plt.figure()
    sns.scatterplot(x=df['Age'], y=df[feature], hue=df['Outcome'], palette='coolwarm')
    plt.scatter(user_data['Age'], user_data[feature], color='red', s=150, label='Your Data')
    plt.title(f'{feature} vs Age (Yours in Red)')
    st.pyplot(fig)

# Display Prediction
st.subheader(' Your Report:')
if user_result[0] == 0:
    result = 'You are **not diabetic**.'
else:
    result = 'You are **diabetic**.'
st.success(result)

# Accuracy
accuracy = accuracy_score(y_test, rf.predict(X_test))
st.subheader(' Model Accuracy:')
st.write(f"{accuracy * 100:.2f}%")

#streamlit run pr.py on the terminal