import matplotlib.pyplot as plt
import numpy as np
data=np.random.normal(0,1,1000)
plt.hist(data,bins=30)
plt.xlabel('value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
