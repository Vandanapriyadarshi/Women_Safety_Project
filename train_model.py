import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier  # faster than XGBoost for demo
import joblib

# Load dataset
df = pd.read_csv("women_safety_india.csv")

# Features and target
X = df[['area','crime_type','reporter_source','num_offenders','severity','population_density','socio_econ_index','hour','dayofweek']]
y = df['incident_next_24h']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Preprocessing
cat_features = ['area','crime_type','reporter_source']
num_features = ['num_offenders','severity','population_density','socio_econ_index','hour','dayofweek']
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features),
    ('num', 'passthrough', num_features)
])

# Model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42))
])

# Train
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "women_safety_model.pkl")

print("Model trained and saved successfully!")
