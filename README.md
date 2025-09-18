# Data Analysis and Visualization with Python 📊

This repository contains a Python script for a simple data analysis and visualization project using the Iris dataset. The script demonstrates key steps in a typical data analysis workflow, including loading a dataset, performing basic statistical analysis, and creating various data visualizations.

## Prerequisites 🛠️

To run this script, you need to have Python installed, along with the following libraries. You can install them using pip:
`````````
pip install pandas matplotlib seaborn scikit-learn

`````````


## How to Run the Script 💻

1. Make sure you have the required libraries installed.  
2. Save the provided Python code as `data_analysis.py`.  
3. Run the script from your terminal:
    `````
    python data_analysis.py

    `````



The script will print the analysis results to the console and display a window with the generated plots.

## Script Breakdown 📝

The script is organized into three main tasks:

### Task 1: Load and Explore the Dataset
- Loads the classic Iris dataset directly from ``scikit-learn``. ✅  
- Displays the first few rows to give a quick overview of the data. ✨  
- Provides a summary of the dataset's structure, including data types and non-null values. 🔎  
- Checks for and handles missing data (although the Iris dataset is clean). 🧹  

### Task 2: Basic Data Analysis
- Computes descriptive statistics for all numerical columns to understand the data's distribution. 📈  
- Groups the data by species and calculates the average sepal length for each group, highlighting key differences between species. 📊  

### Task 3: Data Visualization
Generates a 2x2 grid of four different plots to visualize the dataset:
- **Line Chart:** Shows the trend of sepal length across the samples. 📉  
- **Bar Chart:** Compares the mean sepal length across different species. 📊  
- **Histogram:** Visualizes the distribution of petal length. 📈  
- **Scatter Plot:** Illustrates the relationship between two numerical columns, with each data point colored by its species. 🧩  

All plots are customized with appropriate titles and labels for clarity. 🖼️
