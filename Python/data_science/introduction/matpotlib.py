"""
#data visulization
explore data
report insights

to install python libraries
https://www.lfd.uci.edu/~gohlke/pythonlibs/
"""

import matplotlib
from matplotlib import pyplot as plt 	#import library

#create list corresponding to axis of graph
year=[1950,1970,1990,2010]			#horizontal axis
pop=[2.519,3.692,5.263,6.972]		#verticle axis

plt.plot(year,pop)		#plot function
plt.show()		#build the plot

#scatter plot
plt.scatter(year,pop)
plt.show()

#histogram- idea about distribution
#divide data set to bins with width 

#help(plt.hist)

"""
hist(x,bins=10)		x is the list of vales to build histogram
second arg is number of bins
"""
values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values,bins=3)
plt.show()