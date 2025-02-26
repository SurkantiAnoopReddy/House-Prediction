# 🏠 House Price Prediction Using Machine Learning  

This repository contains a machine learning project that predicts house prices based on various input features. The model is deployed using **Streamlit** for an interactive user interface.

## 📂 Project Structure  

- `app.py` - Streamlit application for predicting house prices.  
- `house_price_regression_dataset.csv` - Dataset used for training the model.  
- `linear_regression_model.pkl` - Pre-trained Linear Regression model.  
- `Untitled.ipynb` - Jupyter Notebook containing data preprocessing, model training, and evaluation steps.  
- `How to Complete a Machine Learning Project.pptx` - Presentation explaining the steps followed in the project.  

## 🔧 Setup Instructions  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
Install dependencies

sh
Copy
Edit
pip install -r requirements.txt
Run the Streamlit App

sh
Copy
Edit
streamlit run app.py
📊 Dataset
The dataset contains 7 attributes:

Square Footage
Number of Bedrooms
Number of Bathrooms
Year Built
Lot Size (in acres)
Garage Size
Neighborhood Quality
Source: Kaggle

🚀 Model Training
The model was trained using Linear Regression, achieving high accuracy in predicting house prices. Data preprocessing includes handling missing values, outlier removal, feature scaling, and train-test splitting.

📈 Deployment
The trained model is deployed using Streamlit, allowing users to enter house details and get real-time price predictions.

🎯 Future Enhancements
Improve accuracy with ensemble models (Random Forest, XGBoost).
Add location-based pricing for better predictions.
Implement a web API for wider usability.
