import streamlit as st
import numpy as np
import pickle

# Load the saved model directly
with open('xgb_model.pkl', 'rb') as model_file:
    regressor = pickle.load(model_file)  # Load the XGBRegressor object

# Streamlit interface for input collection
def show_house_page():
    st.title('House Price Prediction')

    # Creating 13 number inputs for each feature
    CRIM = st.number_input('CRIM: Crime rate', value=0.00632)
    ZN = st.number_input('ZN: Proportion of residential land zoned for large lots', value=18.0)
    INDUS = st.number_input('INDUS: Proportion of non-retail business acres per town', value=2.31)
    CHAS = st.number_input('CHAS: Charles River dummy variable', value=0)
    NOX = st.number_input('NOX: Nitrogen oxide concentration (parts per 10 million)', value=0.538)
    RM = st.number_input('RM: Average number of rooms per dwelling', value=6.575)
    AGE = st.number_input('AGE: Proportion of owner-occupied units built before 1940', value=65.2)
    DIS = st.number_input('DIS: Weighted distance to employment centers', value=4.0900)
    RAD = st.number_input('RAD: Index of accessibility to radial highways', value=1)
    TAX = st.number_input('TAX: Property tax rate', value=296)
    PTRATIO = st.number_input('PTRATIO: Pupil-teacher ratio by town', value=15.3)
    B = st.number_input('B: Proportion of people of African American descent', value=396.90)
    LSTAT = st.number_input('LSTAT: Percentage of lower status population', value=4.98)

    # Button to trigger prediction
    if st.button('Calculate House Price'):
        # Create an array from the input features
        input_data = (CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT)

        # Convert the input data into a numpy array and reshape for prediction
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Predict using the loaded model
        prediction = regressor.predict(input_data_reshaped)

        # Display the predicted price
        st.write(f"The predicted price for the house is: ${prediction[0]:,.2f}")
