import pandas as pd

# create a sample DataFrame
data = {'name': ['John', 'Emma', 'Peter', 'Mary','bunny','sunny'],
        'age': [25, 30, 28, 32,26,40],
        'gender': ['M', 'F', 'M', 'F','M','M']}
df = pd.DataFrame(data)

# display the top 2 rows of the DataFrame
print(df.head(2))
