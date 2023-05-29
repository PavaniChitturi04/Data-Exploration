import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Create a crosstab that shows the frequency distribution of categories and values
cross_tab = pd.crosstab(index=df['Category'], columns=df['Value'])

print(cross_tab)
