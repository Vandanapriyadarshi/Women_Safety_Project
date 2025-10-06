# Save as app.py
import streamlit as st
import pandas as pd
import joblib

# Load data and model
df = pd.read_csv("women_safety_india.csv")
model = joblib.load("women_safety_model.pkl")

st.title("Women Safety & Risk Prediction System")
st.sidebar.header("Select Features")

area = st.sidebar.selectbox("Area", df['area'].unique())
crime_type = st.sidebar.selectbox("Crime Type", df['crime_type'].unique())
reporter_source = st.sidebar.selectbox("Reporter Source", df['reporter_source'].unique())
num_offenders = st.sidebar.number_input("Number of Offenders", 1, 10, 1)
severity = st.sidebar.slider("Severity", 2, 5, 3)
population_density = st.sidebar.number_input("Population Density", 1000, 50000, 12000)
socio_econ_index = st.sidebar.slider("Socio-Economic Index", 0, 100, 50)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
dayofweek = st.sidebar.slider("Day of Week", 0, 6, 3)

if st.button("Predict Risk"):
    input_df = pd.DataFrame([[area,crime_type,reporter_source,num_offenders,severity,population_density,socio_econ_index,hour,dayofweek]],
                            columns=['area','crime_type','reporter_source','num_offenders','severity','population_density','socio_econ_index','hour','dayofweek'])
    risk = model.predict(input_df)[0]
    st.write("🚨 High Risk!" if risk==1 else "✅ Low Risk")
