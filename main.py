import streamlit as st

from predict import show_predict_page
from explore import show_explore_page
from home import show_house_page

page = st.sidebar.selectbox("Explore statistics, Predict, House Price", ("Predict", "Explore", "House Prediction"))

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
elif page == "House Prediction":
    show_house_page()
