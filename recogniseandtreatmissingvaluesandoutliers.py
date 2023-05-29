
import pandas as pd
import numpy as np

# create a sample dataframe with missing values and outliers
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [3, 6, 7, None, 9],
    'C': [9, None, 11, 12, 15]
})

# display the original dataframe
print('Original DataFrame:')
print(df)

# count missing values in each column
print('\nCount of missing values in each column:')
print(df.isnull().sum())

# remove rows with missing values
df = df.dropna()

# display the resulting dataframe after removing rows with missing values
print('\nResulting DataFrame after removing rows with missing values:')
print(df)

# calculate mean and standard deviation of each column
means = df.mean()
stds = df.std()

# identify outliers as values more than 3 standard deviations away from the mean
outliers = ((df - means).abs() > 3 * stds).any(axis=1)

# remove outliers from the dataframe
df = df[~outliers]

# display the resulting dataframe after removing outliers
print('\nResulting DataFrame after removing outliers:')
print(df)
