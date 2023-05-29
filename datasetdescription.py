import pandas as pd

# Read in your data
data = pd.read_csv(r'C:\Users\Bhavani Balijireddi\Desktop\month.csv')
# Describe your data
#print(data.describe())

# Describe your data, including non-numerical columns
print(data.describe(include='all'))


# Get an overview of your data
print(data.info())
