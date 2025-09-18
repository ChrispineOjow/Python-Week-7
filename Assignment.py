import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import sys

# --- Task 1: Load and Explore the Dataset ---
print("--- Task 1: Loading and Exploring the Dataset ---")
try:
    # Load the Iris dataset from scikit-learn
    iris_data = load_iris()
    df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df['species'] = [iris_data.target_names[i] for i in iris_data.target]

    print("\nDataset loaded successfully!")

    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Explore the structure and data types
    print("\nDataset information (data types and non-null counts):")
    df.info()

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    # The Iris dataset has no missing values, so no cleaning is necessary here.
    # If it did, you could use df.dropna() or df.fillna()

except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(1)


# --- Task 2: Basic Data Analysis ---
print("\n\n--- Task 2: Basic Data Analysis ---")

# Compute basic statistics
print("\nDescriptive statistics of numerical columns:")
print(df.describe())
print("\nBased on the statistics, we can see the range and distribution of features.")
print("For instance, petal length has a wide range, from 1.0 to 6.9 cm.")

# Group by 'species' and compute the mean of a numerical column
print("\nMean sepal length for each species:")
species_mean_sepal_length = df.groupby('species')['sepal length (cm)'].mean()
print(species_mean_sepal_length)

print("\nAnalysis of Grouped Data:")
print("The data shows a clear difference in sepal length between species.")
print("The 'setosa' species has the shortest average sepal length, while 'virginica' has the longest.")


# --- Task 3: Data Visualization ---
print("\n\n--- Task 3: Data Visualization ---")
sns.set_style("whitegrid") # Set a visually appealing style

# Create a figure with subplots for all four charts
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Iris Dataset: Data Visualizations', fontsize=20, y=1.02)

# Plot 1: Line Chart to show trend across samples
axes[0, 0].plot(df.index, df['sepal length (cm)'], color='teal', label='Sepal Length')
axes[0, 0].set_title('Line Chart of Sepal Length', fontsize=14)
axes[0, 0].set_xlabel('Sample Index')
axes[0, 0].set_ylabel('Sepal Length (cm)')
axes[0, 0].legend()

# Plot 2: Bar Chart to compare mean sepal length by species
sns.barplot(x=species_mean_sepal_length.index, y=species_mean_sepal_length.values, ax=axes[0, 1], palette="viridis")
axes[0, 1].set_title('Mean Sepal Length by Species', fontsize=14)
axes[0, 1].set_xlabel('Species')
axes[0, 1].set_ylabel('Mean Sepal Length (cm)')

# Plot 3: Histogram of petal length
sns.histplot(df['petal length (cm)'], kde=True, ax=axes[1, 0], color='purple')
axes[1, 0].set_title('Distribution of Petal Length', fontsize=14)
axes[1, 0].set_xlabel('Petal Length (cm)')
axes[1, 0].set_ylabel('Frequency')

# Plot 4: Scatter Plot of sepal length vs. petal length, colored by species
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, ax=axes[1, 1], s=80)
axes[1, 1].set_title('Sepal Length vs. Petal Length', fontsize=14)
axes[1, 1].set_xlabel('Sepal Length (cm)')
axes[1, 1].set_ylabel('Petal Length (cm)')
axes[1, 1].legend(title='Species')

# Adjust layout to prevent titles and labels from overlapping
plt.tight_layout()

# Show the plots
print("\nDisplaying the generated plots.")
plt.show()

print("\nAnalysis complete.")
