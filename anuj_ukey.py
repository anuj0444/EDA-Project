# -*- coding: utf-8 -*-
"""Anuj_Ukey.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TZg0nCOM85WauEBBt-3FBlsTAmv3lmHH
"""

import pandas as pd
nba = pd.read_csv('/content/nba.csv')
missing_values = nba.isnull().sum()
print(missing_values)

# Drop the row with missing values across multiple columns
nba.dropna(how='all', inplace=True)

# Drop the 'College' column
nba.drop('College', axis=1, inplace=True)

# Impute missing 'Salary' values with the median
median_salary = nba['Salary'].median()
nba['Salary'].fillna(median_salary, inplace=True)

# Verify that there are no more missing values in the relevant columns
missing_values_after_cleaning = nba[['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'Salary']].isnull().sum()
print("Missing values after cleaning:")
print(missing_values_after_cleaning)

nba.info()

def convert_height_to_inches(height):
    if pd.isna(height):
        return np.nan
    feet, inches = map(int, height.split('-'))
    return feet * 12 + inches

nba['Height'] = nba['Height'].apply(convert_height_to_inches)
nba['Number'] = nba['Number'].astype(int)

nba.info()

# Check for duplicate rows
duplicates_before = nba.duplicated().sum()
print(f"Number of duplicate rows before removing: {duplicates_before}")

# Remove duplicate rows if they exist
if duplicates_before > 0:
    nba.drop_duplicates(inplace=True)

# Verify that duplicates have been removed
duplicates_after = nba.duplicated().sum()
print(f"Number of duplicate rows after removing: {duplicates_after}")

unique_teams = nba['Team'].unique()
unique_positions = nba['Position'].unique()

print("Unique Teams:")
print(unique_teams)

print("\nUnique Positions:")
print(unique_positions)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(data=nba, x='Salary', bins=50, kde=True)
plt.title('Distribution of Player Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.histplot(data=nba, x='Height', ax=axes[0], kde=True)
axes[0].set_title('Distribution of Player Heights')
axes[0].set_xlabel('Height (inches)')
axes[0].set_ylabel('Frequency')

sns.histplot(data=nba, x='Weight', ax=axes[1], kde=True)
axes[1].set_title('Distribution of Player Weights')
axes[1].set_xlabel('Weight (lbs)')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.scatterplot(data=nba, x='Age', y='Salary', ax=axes[0])
axes[0].set_title('Salary vs. Age')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Salary')

sns.scatterplot(data=nba, x='Height', y='Salary', ax=axes[1])
axes[1].set_title('Salary vs. Height')
axes[1].set_xlabel('Height (inches)')
axes[1].set_ylabel('Salary')

sns.scatterplot(data=nba, x='Weight', y='Salary', ax=axes[2])
axes[2].set_title('Salary vs. Weight')
axes[2].set_xlabel('Weight (lbs)')
axes[2].set_ylabel('Salary')

plt.tight_layout()
plt.show()