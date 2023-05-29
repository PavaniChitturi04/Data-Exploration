
#corr():
import pandas as pd

# Create a sample DataFrame with numerical variables
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

# Print the correlation matrix
print(df.corr())

#scatter_matrix()
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame with numerical variables
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

# Plot the scatter matrix
pd.plotting.scatter_matrix(df, figsize=(6, 6))
plt.show()

#pairplot():

import pandas as pd
import seaborn as sns

# Create a sample DataFrame with numerical variables
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

# Plot the pairplot
sns.pairplot(df)
plt.show()
