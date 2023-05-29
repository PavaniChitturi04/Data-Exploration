
import pandas as pd

# create a sample dataframe with missing values
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, None],
    'C': [9, None, 11, 12]
})

# display the original dataframe
print('Original DataFrame:')
print(df)

# drop any row that has missing values
df_dropped_rows = df.dropna()

# display the resulting dataframe after dropping missing rows
print('\nResulting DataFrame after dropping rows:')
print(df_dropped_rows)

# drop any column that has missing values
df_dropped_cols = df.dropna(axis=1)

# display the resulting dataframe after dropping missing columns
print('\nResulting DataFrame after dropping columns:')
print(df_dropped_cols)
