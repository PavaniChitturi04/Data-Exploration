import pandas as pd

# Create a data frame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print(df)
# Define a function
def multiply_by_two(x):
    return x * 2

print("Apply the function to a column")
d = df.apply(multiply_by_two)
df['A'] = df['A'].apply(multiply_by_two)
print(d) 
