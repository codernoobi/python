#numeric python
import numpy as np 		# import numpy 

height=[1.73,1.68,1.71,1.89,1.79]		#create the list
weight=[65.4,59.2,63.6,88.4,68.7]

#bmi=weight/height**2		#throws error as the list contains multiple values
#looping through the list gives big code

#numpy array calculates for entire array
np_height=np.array(height)			#create a nump array and assign the list
np_weight=np.array(weight)

bmi=np_weight/np_height ** 2

print(bmi)
bmi[1]			#print with index, numpy subsetting

a=bmi>23		#gives boolean values, numpy subsetting
print(a)

b=bmi[bmi>23]		#gives >23 values, numpy subsetting
print(b)

#numpy array should contain single type
#if multiple types then it is converted to str

python_list=[1,2,3]
np_array=np.array([1,2,3])

a=python_list+python_list		#concats
b=np_array+np_array				#adds
print(a)
print(b)

#type of numpy arrays
print(type(np_weight))
print(type(np_height))

np_2d=np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,68.7]])		#2d array
print(np_2d)			#it is of single type
print(np_2d.shape)		#number of rows and columns

print(np_2d[0][2])		#print using index
print(np_2d[0,2])

print(np_2d[:,1:3])		#select all rows, column 1 and 2
print(np_2d[1,:])		#first row all columns