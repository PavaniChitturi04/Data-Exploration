import pandas as pd

# Create a data frame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Define a function
def multiply_by_two(x):
    return x * 2

print("Apply the function to every element in the data frame")
df = df.applymap(multiply_by_two)
print(df) 
