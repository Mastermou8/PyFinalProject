import numpy as np
import matplotlib.pyplot as plt

#creates x axis with range and y axis with sine
#the function plots sin graphts
x = np.arange(0, 5*np.pi, 0.1)

y = np.sin(2 * x)

#plotting coine graph
plt.plot(x, y, color='blue')
plt.show()

#this code was taken from
#https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/