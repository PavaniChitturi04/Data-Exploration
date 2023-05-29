import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Create a pivot table that shows the sum of values for each category
pivot_table = pd.pivot_table(df, values='Value', index='Category', aggfunc='sum')

print(pivot_table)
