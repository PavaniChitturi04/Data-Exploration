import pandas as pd

# Create a data frame
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

print("Calculate the correlation matrix for the entire data frame")
print(df.corr())


print("Calculate the correlation between columns A and B")
print(df['A'].corr(df['B']))

# Output:
# 1.0

