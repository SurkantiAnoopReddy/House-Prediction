import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_filename = "linear_regression_model.pkl"  # Replace with your model file path
loaded_model = joblib.load(model_filename)

# Set custom CSS for background color
st.markdown("""
    <style>
        body {
            background-color: #f0f0f0;  /* Light gray background */
            color: #333;  /* Dark text color */
        }
        .stButton>button {
            background-color: #b0b0b0;
            color: white;
        }
        .stTextInput>input {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Define the input fields for the application
st.title("🏠 House Price Prediction App 🏡")
st.write("Enter the details of the house to predict its price:")

# Collect user input
square_footage = st.number_input("Square Footage", min_value=500, max_value=10000, value=2000)
num_bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
num_bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)

# Adjust the year_built to allow for future years
current_year = 2023  # Update with the current year or use datetime to get the current year dynamically
year_built = st.number_input("Year Built", min_value=1800, max_value=2100, value=current_year)  # Now up to 2100

lot_size = st.number_input("Lot Size (in acres)", min_value=0.1, max_value=100.0, value=1.5)
garage_size = st.number_input("Garage Size (number of cars)", min_value=0, max_value=5, value=1)
neighborhood_quality = st.number_input("Neighborhood Quality (1 to 10)", min_value=1, max_value=10, value=7)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    "Square_Footage": [square_footage],
    "Num_Bedrooms": [num_bedrooms],
    "Num_Bathrooms": [num_bathrooms],
    "Year_Built": [year_built],
    "Lot_Size": [lot_size],
    "Garage_Size": [garage_size],
    "Neighborhood_Quality": [neighborhood_quality]
})

# Predict the price
if st.button("🔮 Predict Price"):
    prediction = (loaded_model.predict(input_data)[0])*8.8
    st.success(f"The predicted price of the house is: 🏠 Rupees:{prediction:,.2f} 💰")
