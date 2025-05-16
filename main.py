import streamlit as st

from predict import show_predict_page
from explore import show_explore_page
from home import show_house_page
from explore_house import show_house_explore_page

page = st.sidebar.selectbox("Phone Prices, Phone statistics, House Price, Explore House statistics", ("Predict", "Phone Statistics", "House Prediction", "House Statistics"))

if page == "Predict":
    show_predict_page()
elif page == "Phone Statistics":
    show_explore_page()
elif page == "House Prediction":
    show_house_page()
elif page == "House Statistics":
    show_house_explore_page()
