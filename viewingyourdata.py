import pandas as pd

# Read in your data
data = pd.read_csv(r'C:\Users\Bhavani Balijireddi\Desktop\month.csv')

print('\n', "View the first 5 rows of your data")
print(data.head())

print('\n',"View the last 5 rows of your data")
print(data.tail())

print('\n',"View summary statistics of your data")
print(data.describe())

print('\n',"View a specific column of your data")
print(data['Name'])
