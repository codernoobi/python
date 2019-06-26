fruits = ("apple", "banana", "cherry")			#create tuple			
print(fruits[0])								#tuple object at index 0

print(len(fruits))								#number of objects in tuple

#fruits[1] = "blackcurrant"				# The values will remain the same:
# tuple does not support assignment

for x in fruits:			#loop through tuple
  print(x)

if "apple" in fruits:	#check condition
  print("Yes, 'apple' is in the fruits tuple")

#fruits[3] = "orange" 		# This will raise an error because cannot add new items

del fruits		#delete the tuple

fruits = tuple(("apple", "banana", "cherry")) 	#tuple constructor
print(fruits)

"""
count()		Returns the number of times a specified value occurs in a tuple
index()		Searches the tuple for a specified value and returns the position of where it was foun
"""