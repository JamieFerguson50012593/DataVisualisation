# -*- coding: utf-8 -*-
"""DataCleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j2DybJLQLZ-fZxlf2xyhJw2IWPvHc-Bs
"""

import pandas as pd

# Load the CSV file
df = pd.read_csv('/content/foodhygienedatav2 (1).csv', encoding='latin-1')

# Explore the data
print(df.head())
print(df.isnull().sum())
print(df.dtypes)

# Clean the data
# For example, remove duplicates and fill missing values with 0
df = df.drop_duplicates()
df = df.fillna(0)

# Identify irrelevant columns
irrelevant_columns = ['establishmentaddressline1', 'establishmentaddressline2', 'Column1', 'Column2', 'Column3', 'Column4' ]  # Replace with actual column names

# Drop irrelevant columns
df_cleaned = df.drop(irrelevant_columns, axis=1)

# Check the resulting DataFrame
print(df_cleaned.head())


# Save the cleaned data to a new CSV file
df.to_csv('cleaned_file.csv', index=False)