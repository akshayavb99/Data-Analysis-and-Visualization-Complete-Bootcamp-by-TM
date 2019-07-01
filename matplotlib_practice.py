import numpy as np
import matplotlib.pyplot as plt #For graphing data

axes_val=np.arange(-100,100,10)
dx,dy=np.meshgrid(axes_val,axes_val) #Maps values in pairs
#print("dx:")
#print(dx)
#print("dy:")
#print(dy)

function = 2*dx+3*dy #New array called function contains values derived from values of dx and dy. Has same dimensions as dx and dy
#print(function)

#Plotting data values
plt.imshow(function)
plt.title('Graph of 2*dx+3*dy')
plt.colorbar()
plt.savefig('my_fig.png')

