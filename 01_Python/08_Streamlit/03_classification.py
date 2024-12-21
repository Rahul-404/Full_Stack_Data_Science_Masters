import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_resource
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_name = load_data()

# print(type(df))
# st.write(df)

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1], df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal Width", float(df["sepal width (cm)"].min()), float(df["sepal width (cm)"].max()))
petal_length = st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal Width", float(df["petal width (cm)"].min()), float(df["petal width (cm)"].max()))


input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

st.write(f"Prediction")
st.write(f"The predicted species is: {predicted_species}")