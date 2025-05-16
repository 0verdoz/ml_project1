import streamlit as st
import pickle
import numpy as np
import pandas as pd



def load_model():
    with open('save_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
ohe = data["ohe"]
te_model = data["te_model"]
le_location = data["le_location"]
# brand_encoded = data["brand_encoded"]
# model_encoded = data["model_encoded"]
# location_encoded = data["location_encoded"]
# storage = data["storage"]

def show_predict_page():
    st.title("📱 Mobile Price Predictor.")

    brands = (
        "Samsung",
        "Apple",
        "Huawei",
        "Google",
        "LG",
        "Tecno",
        "Infinix",
        "Itel",
        "Oppo",
        "Xiaomi",
        "Nokia",
        "Motorola",
        "Vivo",
        "Realme",
        "OnePlus",
        "HTC",
        "X-Tigi",
        "Honor",
    )

    storage_options = (
        64,
        128,
        256,
        512,
        1024,
    )

    # User Inputs
    brand = st.selectbox("Brands", brands)
    model = st.text_input("Enter Model (e.g., Galaxy S20 Ultra)", value="Galaxy S20 Ultra")
    storages = st.select_slider("Phone Storage (GB)", storage_options)
    location = st.text_input("Enter your location (e.g., Tema)", value="Tema")

    ok = st.button("Display Price")
    if ok:
        x = np.array([[brand, model, location, storages]])

        brand_input = pd.DataFrame(x[:, 0], columns=['brand'])
        brand_encoded = ohe.transform(brand_input).toarray()

        model_input = pd.Series(x[:, 1], name='model')  
        model_encoded = te_model.transform(model_input).to_numpy().reshape(-1, 1)

        location_input = pd.Series(x[:, 2])
        location_encoded = le_location.transform(location_input).reshape(-1, 1)

        storage_input = np.array([[x[0, 3]]], dtype=float)
        x = np.hstack([brand_encoded, model_encoded, location_encoded, storage_input])

        price = regressor.predict(x)
        st.subheader(f"The estimated price is Ghs(¢){price[0]:.2f}")



# if st.button("Predict Price"):
#     try:
#         # --- Step 1: Encode brand (OneHot)
#         brand_input = pd.DataFrame([[brand]], columns=['brand'])
#         brand_encoded = ohe.transform(brand_input).toarray()

#         # --- Step 2: Encode model (TargetEncode)
#         model_input = pd.Series([model], name='model')
#         model_encoded = te_model.transform(model_input).reshape(-1, 1)

#         # --- Step 3: Encode location (LabelEncode)
#         location_input = pd.Series([location])
#         location_encoded = le_location.transform(location_input).reshape(-1, 1)

#         # --- Step 4: Format storage
#         storage_input = np.array([[float(storage)]])

#         # --- Step 5: Combine all features
#         x_final = np.hstack([brand_encoded, model_encoded, location_encoded, storage_input])

#         # --- Predict
#         prediction = regressor.predict(x_final)[0]
#         st.success(f"📱 Estimated Price: ¢{prediction:,.2f}")
    
#     except Exception as e:
#         st.error(f"Error: {e}")