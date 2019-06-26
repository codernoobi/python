'''
list-array with integers index; contains homogenous(integer, boolean, etc) data;start and end []
dictionary-start and end {};hash map;
tupple-used when no need of change(immutable array); used for threads; start and end ();at the end of tupple there should be , (1,)
'''


#list
'''mylist=["Hello",False,1.21,1] 
print(mylist)		#print all
print(mylist[0])	#print based on index
mylist.sort()		#sort; can be used if same data types are in list
mylist.append("Superman")  # append
print(mylist)'''

#generators  	#gives one value at a time(one by one); stores the state
mylist=[2,3,1,3,4,5,3,45,6,]

'''for x in range(0,10,2):		#x takes the value with in range; third parameter is for print with skip
	print(x)'''

#dictionary
dict_a={"name":mylist}	#key:value; value should be string; key can be any variable
print(dict_a["name"])	#Prints the value at name
print(dict_a["name"][1])	#prints value at index

