import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(0,1,100)
y=np.random.normal(0,1,100)
plt.scatter(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter plot Example')
plt.show()
