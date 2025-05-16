import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    house_price_dataset = pd.read_csv("BostonHousing.csv")
    house_price_dataset = house_price_dataset.rename(columns={'medv': 'price'})
    return house_price_dataset

house_price_dataset = load_data()

def show_house_explore_page():
    st.title("Explore the statistics for the Boston House Prices")

    correlation = house_price_dataset.corr()

    fig1, ax1 = plt.subplots(figsize=(10,10))
    sns.heatmap(correlation, cbar=True, square=True,fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues')
    st.pyplot(fig1)

    st.write("#### Mean Price from different ")
    data = house_price_dataset.groupby(["age"])["price"].mean().sort_values(ascending=True)
    st.bar_chart(data)
