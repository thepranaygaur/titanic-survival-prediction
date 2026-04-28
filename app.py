import streamlit as st
import pickle
import numpy as np

# Title
st.title("🚢 Titanic Survival Prediction App")

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# ===== USER INPUTS =====
st.header("Enter Passenger Details")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 1, 80)

sibsp = st.number_input("Siblings/Spouses", 0, 10, 0)
parch = st.number_input("Parents/Children", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)

embarked = st.selectbox("Embarked", ["S", "C", "Q"])

# ===== FEATURE ENGINEERING (same as training) =====
sex = 0 if sex == "Male" else 1

family_size = sibsp + parch + 1
is_alone = 0 if family_size > 1 else 1

# One-hot encoding for embarked
embarked_S = 1 if embarked == "S" else 0
embarked_Q = 1 if embarked == "Q" else 0

# ===== PREDICTION =====
if st.button("Predict"):

    input_data = np.array([[pclass, sex, age, sibsp, parch, fare,
                            family_size, is_alone, embarked_Q, embarked_S]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Passenger Survived")
    else:
        st.error("💀 Passenger Did Not Survive")