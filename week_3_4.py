import pandas as pd

# Load the dataset
data = pd.read_csv('data.csv')

# view the first rows
print(data.head())

# Check data types and non-null counts
print(data.info())

# Get summary statistics
print(data.describe())

# Mean
print(data.mean(numeric_only=True))

# Median
print(data.median(numeric_only=True))

# Mode
print(data.mode(numeric_only=True).iloc[0])

# Standard Deviation
print(data.std(numeric_only=True))

# Calculate Correlation Between Features
print(data.corr(numeric_only=True))
