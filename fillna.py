
import pandas as pd
import numpy as np

# create a sample dataframe with missing values
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 6, 7, None],
    'C': [9, None, 11, 12]
})

# display the original dataframe
print('Original DataFrame:')
print(df)

# fill missing values with a constant value
df_filled_constant = df.fillna(0)

# display the resulting dataframe after filling with constant value
print('\nResulting DataFrame after filling with constant value:')
print(df_filled_constant)

# fill missing values with mean of the column
df_filled_mean = df.fillna(df.mean())

# display the resulting dataframe after filling with mean
print('\nResulting DataFrame after filling with mean:')
print(df_filled_mean)

# fill missing values with forward fill method
df_filled_ffill = df.fillna(method='ffill')

# display the resulting dataframe after filling with forward fill
print('\nResulting DataFrame after filling with forward fill:')
print(df_filled_ffill)

# fill missing values with backward fill method
df_filled_bfill = df.fillna(method='bfill')

# display the resulting dataframe after filling with backward fill
print('\nResulting DataFrame after filling with backward fill:')
print(df_filled_bfill)
