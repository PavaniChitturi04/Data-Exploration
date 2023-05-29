import pandas as pd

# Read in your data
data = pd.read_csv(r'C:\Users\Bhavani Balijireddi\Desktop\month.csv')

# Describe your categorical variable
print(data['Name'].describe(include='Name'))

# Get a frequency count of each category
print(data['Name'].value_counts())
