import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.cumsum(np.random.normal(0,1,100))
plt.fill_between(x,y,color='skyblue',alpha=0.6)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Area plot Example')
plt.show()
