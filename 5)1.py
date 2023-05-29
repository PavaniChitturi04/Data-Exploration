print("Using a dictionary")
import pandas as pd

data = {'name': ['John', 'Emma', 'Peter', 'Mary'],
     'age': [25, 30, 28, 32],
     'gender': ['M', 'F', 'M', 'F']}

df = pd.DataFrame(data)
print(df)

#Using a list of lists

#import pandas as pd

#data = [['John', 25, 'M'],
#        ['Emma', 30, 'F'],
 #       ['Peter', 28, 'M'],
 #       ['Mary', 32, 'F']]

#columns = ['name', 'age', 'gender']

#df = pd.DataFrame(data, columns=columns)
#print(df)

print('\n',"Using a NumPy array")

import pandas as pd
import numpy as np

data = np.array([['John', 25, 'M'],
                 ['Emma', 30, 'F'],
                 ['Peter', 28, 'M'],
                 ['Mary', 32, 'F']])

columns = ['name', 'age', 'gender']

df = pd.DataFrame(data, columns=columns)
print(df)
