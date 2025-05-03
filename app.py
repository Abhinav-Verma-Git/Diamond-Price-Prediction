import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

data=pd.read_csv("diamonds.csv")
model=joblib.load("model.pkl")


menu=st.sidebar.radio("Menu",["Home","Analysis","Price Prediction"])
if menu=="Home":
    st.title(" Diamond Price Prediction") 
    st.image("diamondpp.png",width=500)
    st.markdown("This project implements a simple Linear Regression model to predict the price of diamonds based on features like carat and depth.")
    st.divider()
if menu=="Analysis":
    st.title("Analytical  Data of the Diamonds")
    st.image("analysis.png",width=500)
    if st.checkbox("Tabular Data"):
        st.table(data.head(50))
        st.text("Note: Model is trained on:")
        st.text(data.shape)
        st.divider()
    if st.checkbox("Statistics"):
        st.table(data.describe())
        st.divider()
    if st.checkbox("Correlation Heatmap"):
        fig=plt.figure(figsize=(10, 6))
        sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Correlation Heatmap")
        st.pyplot(fig)
        st.divider()
    if st.checkbox("Scatterplot"):
       value=st.slider("Filter the data using carat",0,6)
       data=data.loc[data["carat"]>=value]
       fig,ax=plt.subplots(figsize=(10,6))
       sns.scatterplot(data=data,x="carat",y="price",hue="cut")
       st.pyplot(fig)
       st.divider()
    if st.checkbox("Lineplot"):
        value=st.slider("Filter using the data using carat",0,6)
        data=data.loc[data["carat"]>=value]
        fig,ax=plt.subplots(figsize=(10,6))   
        sns.lineplot(x="carat",y="price",data=data,estimator="mean",errorbar=None)
        st.pyplot(fig)
        st.divider()

if menu=="Price Prediction":
    st.title("Price Prediction of the Diamonds") 
    st.image("analysis.png",width=500)
    features=[["carat","depth"]]
    value1=st.number_input("Carat")
    value2=st.number_input("Depth")
    if st.button("Predict the Price($)"):
        with st.spinner("Predicting"):
            time.sleep(5)
            st.balloons()
        prediction=model.predict([[value1,value2]])[0]
        st.write(f"Price Prediction is {prediction:,.2f}")
