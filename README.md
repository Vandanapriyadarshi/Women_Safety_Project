# Women Safety & Risk Prediction System

**AI-powered Women Safety & Risk Prediction System** is a data-driven project that predicts the likelihood of women’s safety incidents across different areas in India. The system leverages machine learning to identify high-risk zones based on historical incident data, area-specific characteristics, and socio-economic indicators.

---

## Features

- **Data Simulation & Analysis:**  
  - Generates a dataset simulating women safety incidents across Indian cities.
  - Includes features like area, crime type, population density, socio-economic index, and more.
  - Exploratory Data Analysis (EDA) visualizations to identify hotspots, crime trends, and temporal patterns.

- **Machine Learning Model:**  
  - Uses XGBoost classifier to predict the probability of an incident occurring in the next 24 hours in a given area.
  - Incorporates numerical and categorical features for accurate predictions.

- **Interactive Dashboard:**  
  - Built with Streamlit for real-time risk prediction.
  - Users can input area and incident parameters to get risk scores instantly.

- **Risk Visualization:**  
  - Highlights high-risk areas and trends.
  - Provides actionable insights for individuals and authorities to enhance women’s safety.

---

## Technologies Used

- Python (Pandas, NumPy)
- Scikit-learn, XGBoost
- Streamlit
- Matplotlib, Seaborn
- Joblib (for saving/loading model)

---

## Project Structure

Women_Safety_Project/
│
├── app.py # Streamlit dashboard
├── train_model.py # Model training script
├── eda_visualizations.py # Exploratory data analysis scripts
├── generate_dataset.py # Dataset simulation script
├── women_safety_india.csv # Sample dataset
├── women_safety_model.pkl # Trained ML model
├── requirements.txt # Required Python packages
└── README.md # Project documentation


---

## How to Run

1. Install dependencies:

```bash

pip install -r requirements.txt

### Run the Streamlit dashboard:

streamlit run app.py


Open your browser and navigate to http://localhost:8501 to use the interactive system.
http://localhost:8501/#women-safety-and-risk-prediction-system

Outcome

Predicts high-risk areas for women’s safety incidents.

Interactive dashboard for real-time insights.

Fully reproducible workflow including dataset simulation, model training, and deployment.

Author

Vandana Priyadarshi
GitHub: https://github.com/Vandanapriyadarshi
