import streamlit as st
import pickle
import numpy as np

main_brands = ['Samsung','Apple','Other','Huawei','Google','LG']
main_models = ['iPhone X','iPhone 8 Plus','Galaxy S6 edge','Galaxy S7 edge','iPhone XR','iPhone 7 Plus','Galaxy S21 Ultra']

def clean_brand(brand):
    return brand if brand in main_brands else 'Others'

def clean_model(model):
    return model if model in main_models else 'Others'

def load_model():
    with open('prices.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

xgb_model = data["model"]
le_brand = data["le_brand"]
le_model = data["le_model"]

# The Encoders below cause errors.
# regressor = data["model"]
# ohe = data["ohe"]
# te_model = data["te_model"]   
# le_location = data["le_location"]
# brand_encoded = data["brand_encoded"]
# model_encoded = data["model_encoded"]
# location_encoded = data["location_encoded"]
# storage = data["storage"]

def show_predict_page():
    st.title("📱 Mobile Price Predictor.")

    # brands = (
    #     "Samsung",
    #     "Apple",
    #     "Huawei",
    #     "Google",
    #     "LG",
    #     "Tecno",
    #     "Infinix",
    #     "Itel",
    #     "Oppo",
    #     "Xiaomi",
    #     "Nokia",
    #     "Motorola",
    #     "Vivo",
    #     "Realme",
    #     "OnePlus",
    #     "HTC",
    #     "X-Tigi",
    #     "Honor",
    # )

    # storage_options = (
    #     64,
    #     128,
    #     256,
    #     512,
    #     1024,
    # )

    # User Inputs
    brand = st.text_input("Brands", value="Samsung")
    model = st.text_input("Enter Model (e.g., Galaxy S20 Ultra)", value="Galaxy S20 Ultra")
    storage = st.number_input("Phone Storage (GB)")
    # location = st.text_input("Enter your location (e.g., Tema)", value="Tema")

    ok = st.button("Predict Price")

    if ok:
        # x = np.array([[brand, model, location, storages]])
        brand_cleaned = clean_brand(brand)
        model_cleaned = clean_model(model)

        try:
          encoded_brand = le_brand.transform([brand_cleaned])[0]
          encoded_model = le_model.transform([model_cleaned])[0]
        except ValueError:
            st.error("Nan")
            return


        x = np.array([[encoded_brand, encoded_model, storage]])

        price = xgb_model.predict(x)
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