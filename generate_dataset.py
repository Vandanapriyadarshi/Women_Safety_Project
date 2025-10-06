import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# Simulate data
N = 5000
areas = ["Delhi Central", "Mumbai South", "Kolkata North", "Bengaluru East", "Chennai Central",
         "Hyderabad West", "Pune North", "Jaipur South", "Lucknow Central", "Bhopal North"]

crime_types = ["Harassment", "Assault", "Abduction", "Domestic Violence", "Rape", "Molestation"]
reporter_sources = ["Police_Report", "Social_Media", "News"]

dates = [datetime(2023,1,1) + timedelta(minutes=int(x)) for x in np.random.randint(0, 60*24*365, size=N)]

data = {
    "incident_id": [f"WOM{100000+i}" for i in range(N)],
    "datetime": dates,
    "area": np.random.choice(areas, size=N),
    "crime_type": np.random.choice(crime_types, size=N, p=[0.3,0.2,0.15,0.15,0.1,0.1]),
    "reporter_source": np.random.choice(reporter_sources, size=N, p=[0.6,0.25,0.15]),
    "num_offenders": np.random.poisson(1.2, size=N) + 1,
    "severity": np.random.randint(2,6,size=N),  # 2 to 5
    "population_density": np.round(np.random.normal(12000, 4000,size=N)).astype(int),
    "socio_econ_index": np.round(np.random.normal(50,15,size=N),1)
}

df = pd.DataFrame(data)

# Feature engineering
df['hour'] = df['datetime'].dt.hour
df['dayofweek'] = df['datetime'].dt.dayofweek

# Simulate target: 1 = high-risk area incident next 24h, 0 = low risk
area_risk_score = {a: random.uniform(0.2, 0.8) for a in areas}
df['incident_next_24h_prob'] = df['area'].map(area_risk_score)
df['incident_next_24h'] = (np.random.rand(N) < df['incident_next_24h_prob']).astype(int)
df = df.drop(columns=['incident_next_24h_prob'])

# Save CSV
df.to_csv("women_safety_india.csv", index=False)
df.head()
