import pandas as pd

# Define a series
s = pd.Series([1, 2, 3, 4, 5])

# Define a function to apply
def square(x):
    return x**2

print("Apply the function to the series using map()")
new_s = s.map(square)

print(new_s)
