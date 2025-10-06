import matplotlib.pyplot as plt
import seaborn as sns

# Hotspots by area
plt.figure(figsize=(10,5))
sns.countplot(x='area', data=df, order=df['area'].value_counts().index, palette='Reds')
plt.title("Crime Against Women by Area")
plt.xticks(rotation=45)
plt.show()

# Crime type trends
plt.figure(figsize=(8,5))
sns.countplot(x='crime_type', data=df, order=df['crime_type'].value_counts().index, palette='Oranges')
plt.title("Crime Type Distribution")
plt.show()

# Hourly pattern
plt.figure(figsize=(8,5))
sns.countplot(x='hour', data=df, palette='Purples')
plt.title("Crime Against Women by Hour of Day")
plt.show()
