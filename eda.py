import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display first 5 rows
print(df.head()) 
print("\nDataset Information:")
df.info()
# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumns:")
print(df.columns)

# Survival Count
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

# Gender Count
sns.countplot(x="Sex", data=df)
plt.title("Gender Count")
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.show()

# Passenger Class
sns.countplot(x="Pclass", data=df)
plt.title("Passenger Class")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

