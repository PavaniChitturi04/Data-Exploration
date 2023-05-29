#import pandas as pd

# create a DataFrame with null values
#df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [5, None, 7, None], 'C': [6, None, None, None]})
#print(df)

# drop rows with null values
#df = df.dropna()
#print(df)

# drop columns with null values
#df = df.dropna(axis=1)
#print(df)





import pandas as pd

# Create a sample DataFrame with null values
df = pd.DataFrame({'A': [1, 2, None, 4],
                   'B': [5, None, 7, 8],
                   'C': [9, 10, 11, 12]})

# Remove null values
df = df.dropna()
print('\n',df)
# Print the resulting DataFrame
#print(df)
# Remove columns with null values
df = df.dropna(axis=1)

# Print the resulting DataFrame
print('\n',df)
