import numpy as np 		# import numpy 

height=[1.73,1.68,1.71,1.89,1.79]		#create the list
weight=[65.4,59.2,63.6,88.4,68.7]

np_2d=np.array([height,weight])		#2d array

print(np.mean(np_2d[1,:]))			#mean function
print(np.median(np_2d[0,:]))		#median function

print(np.corrcoef(np_2d[:,0],np_2d[:,1]))		#to check all rows 0 and 1 element is corelated
print(np.std(np_2d[1,:]))				#standard deviation

#sum(), sort()


#data generation
a=np.round(np.random.normal(1.75,0.20,5000),2)	#(distribution mean, distribution std, number of samples)	
b=np.round(np.random.normal(60.32,15,5000),2)
np_city=np.column_stack((a,b))
print(np_city)

"""
sample of random distribution 5000 times to create the arrays a and b, 
then use column stack to paste them together as two columns
"""