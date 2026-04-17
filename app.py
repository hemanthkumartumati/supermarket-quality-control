import streamlit as st
import pandas as pd
import joblib

# Load the "brain" (model) and the column names
model = joblib.load('model.pkl')
model_columns = joblib.load('columns.pkl')

st.title("Supermarket Quality Control: Satisfaction Predictor")
st.write("Enter the transaction details below to predict customer satisfaction (1-10).")

# Create input fields for the user
branch = st.selectbox("Branch", ["A", "B", "C"])
customer_type = st.selectbox("Customer Type", ["Member", "Normal"])
gender = st.selectbox("Gender", ["Female", "Male"])
product_line = st.selectbox("Product line", ["Health and beauty", "Electronic accessories", "Home and lifestyle", "Sports and travel", "Food and beverages", "Fashion accessories"])
total = st.number_input("Total Bill ($)", min_value=0.0, value=50.0)

# What happens when the button is clicked
if st.button("Predict Rating"):
    # 1. Capture the user's input
    user_input = {
        "Total": total,
        f"Branch_{branch}": 1 if branch != "A" else 0, 
        f"Customer type_Normal": 1 if customer_type == "Normal" else 0,
        f"Gender_Male": 1 if gender == "Male" else 0,
        f"Product line_{product_line}": 1
    }
    
    # 2. Convert to a DataFrame 
    input_df = pd.DataFrame([user_input])
    
    # 3. Add any missing columns (filled with 0) that the model expects
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    # 4. Make the prediction
    prediction = model.predict(input_df)[0]
    
    # 5. Show the result!
    st.success(f"Predicted Satisfaction Rating: {prediction:.2f} / 10")