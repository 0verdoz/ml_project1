import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
  categorical_map = {}
  for i in range(len(categories)):
    if categories.values[i] >= cutoff:
      categorical_map[categories.index[i]] = categories.index[i]
    else:
      categorical_map[categories.index[i]] = 'Other'
  return categorical_map

def shorten_brands(brands, cutoff):
  brands_map = {}
  for i in range(len(brands)):
    if brands.values[i] >= cutoff:
      brands_map[brands.index[i]] = brands.index[i]
    else:
      brands_map[brands.index[i]] = 'Other'
  return brands_map

def shorten_models(models, cutoff):
  models_map = {}
  for i in range(len(models)):
    if models.values[i] >= cutoff:
      models_map[models.index[i]] = models.index[i]
    else:
      models_map[models.index[i]] = 'Other'
  return models_map


@st.cache_data
def load_data():
  mobile_price_dataset = pd.read_csv('Mobile-Phones.csv')
  mobile_price_dataset = mobile_price_dataset.drop(columns=['sd_card', 'main_camera', 'resolution', 'display', 'sim_card', 'os', 'color', 'region', 'screen_size(inch)', 'battery(mAh)', 'ram(GB)', 'selfie_camera(MP)'], axis=1)
  mobile_price_dataset.loc[mobile_price_dataset['location'] == 'Accra Metropolitan', 'location'] = 'Accra'
  mobile_price_dataset.loc[mobile_price_dataset['location'] == 'Tema Metropolitan', 'location'] = 'Tema'
  mobile_price_dataset.loc[mobile_price_dataset['location'] == 'Kumasi Metropolitan', 'location'] = 'Kumasi'
  mobile_price_dataset = mobile_price_dataset.dropna()
  location_map = shorten_categories(mobile_price_dataset['location'].value_counts(), 90)
  mobile_price_dataset['location'] = mobile_price_dataset['location'].map(location_map)
  brand_map = shorten_brands(mobile_price_dataset['brand'].value_counts(), 100)
  mobile_price_dataset['brand'] = mobile_price_dataset['brand'].map(brand_map)
  model_map = shorten_models(mobile_price_dataset['model'].value_counts(), 30)
  mobile_price_dataset['model'] = mobile_price_dataset['model'].map(model_map)
  return mobile_price_dataset


mobile_price_dataset = load_data()

def show_explore_page():
  st.title("Explore the Statistics")

  st.write("##### Mobile Phones Prices in Ghana")

  data = mobile_price_dataset['brand'].value_counts()

  fig1, ax1 = plt.subplots()
  ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
  ax1.axis("equal") # Equal aspect ration ensures that pie is drawn as a circle.

  st.write("##### Number of Data from different Brands")

  st.pyplot(fig1)

  st.write("#### Mean Price from different Brands")

  data = mobile_price_dataset.groupby(["brand"])["price(¢)"].mean().sort_values(ascending=True)
  st.bar_chart(data)


  st.write("#### Price based on location")

  data = mobile_price_dataset.groupby(['location'])["price(¢)"].mean().sort_values(ascending=True)
  st.line_chart(data)

