import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data=np.random.normal(0,1,1000)
sns.kdeplot(data)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('KDE plot example')
plt.show() 
