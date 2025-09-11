import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

# Display first few rows
print("📄 First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\n🔍 Data types:")
print(df.dtypes)

print("\n🧼 Missing values:")
print(df.isnull().sum())

# Basic statistics
print("\n📊 Descriptive statistics:")
print(df.describe())

# Grouping by species and computing mean
grouped = df.groupby('species').mean()
print("\n📈 Mean values grouped by species:")
print(grouped)

# Observations
print("\n🧠 Observations:")
print("• Setosa tends to have smaller petal lengths and widths.")
print("• Virginica has the largest average petal dimensions.")
print("• Sepal measurements vary less across species than petal measurements.")

# -----------------------------
# 📊 Data Visualizations
# -----------------------------

# Line chart: simulate time-series by plotting sepal length across index
plt.figure(figsize=(8, 4))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title("Simulated Time-Series of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart: average petal length per species
plt.figure(figsize=(6, 4))
grouped['petal length (cm)'].plot(kind='bar', color='skyblue')
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.tight_layout()
plt.show()

# Histogram: distribution of petal width
plt.figure(figsize=(6, 4))
plt.hist(df['petal width (cm)'], bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Scatter plot: sepal length vs petal length
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()