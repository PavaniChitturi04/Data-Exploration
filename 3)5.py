import pandas as pd

# Creating a sample dataset
data = {'category': ['A', 'B', 'B', 'C', 'C', 'C']}
df = pd.DataFrame(data)

# Counting the number of observations per category
counts = df['category'].value_counts()
print('\n',counts)

# Counting the number of observations per category using groupby
counts = df.groupby('category').size()
print('\n',counts)
