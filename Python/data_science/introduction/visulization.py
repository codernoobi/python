from matplotlib import pyplot as plt

__name__ == "__main__"
"""
different plot types
many customiztions

depends on: data, waht is to be projected
"""
year=[1950,1970,1990,2010]			#horizontal axis
pop=[2.519,3.692,5.263,6.972]		#verticle axis

#plt.plot(year,pop)		#plot function
plt.fill_between(year,pop,0,color='green')		#fill up area under graph
					#so replace plot function with fill_between function

plt.xlabel('year')		#labeling axis
plt.ylabel('population')
plt.title('world population projection')	#set title
plt.yticks([0,2,4,6,8,10],			#change ticks of y and list of ticks as arg
			['0','2B','4B','6B','8B','10B'])	#second arg to yticks, which is display names

plt.show()		#build the plot