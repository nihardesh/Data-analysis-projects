import streamlit as st
import pandas as pd
import numpy as np

# 1. Setup the Title and Text
st.title("My First Professional App 🚀")
st.write("Welcome! This app was built entirely in Python.")

# 2. Add an Interactive Slider
st.subheader("Interactive Settings")
points = st.slider("Select number of data points", 10, 100, 50)

# 3. Generate some random data based on the slider
data = pd.DataFrame(
    np.random.randn(points, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

# 4. Display a Map and a Table
st.map(data)
st.write("Here is the raw data used for the map:")
st.dataframe(data)