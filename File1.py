import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams                   



rcParams['figure.figsize']=5,4  #used for length and width of the slide of the plot 
x=range(1,10)
y=[1,3,5,6,8,4,3,2,3]


#Line Plot between x,y 
plt.plot(x,y)
plt.show()

#Bar plot between x,y
plt.bar(x,y)
plt.show()

#Pie plot between x,y
plt.pie(x)
plt.show()



