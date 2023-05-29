import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Define a custom function to apply to each group
def my_function(group):
    return group.max() - group.min()

# Group the DataFrame by 'Category' and apply the custom function
result = df.groupby('Category')['Value'].apply(my_function)

print(result)
