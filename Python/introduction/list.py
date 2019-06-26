fruits = ["apple", "banana", "cherry"]		#create list
print(fruits[1])							# object at index 1

fruits = ["apple", "banana", "cherry"]
fruits[0] ="kiwi"							#replace apple with kiwi

fruits.append("orange")						#append
print(fruits)					

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")					#insert at second position

"""
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana)"						#remove item from list

fruits= list(("apple", "banana", "cherry")) # list constructor
print(fruits)

fruits.pop()								#removes last item or secified index
print(fruits)

del fruits[2]								#removes specified index
print(fruits)

del fruits									#delets the list
print(fruits) 

fruits.clear()								#clears the list
print(fruits)			

for x in fruits:							#loop through list
	print(x)

if "apple" in fruits:						#check the loop element
  print("Yes, 'apple' is in the fruits list")

print(len(fruits))							#length of list

"""
#Remove any duplicates from a list
mylist = ["a", "b", "a", "c", "c"]		#A List with Duplicates
mylist = list(dict.fromkeys(mylist))		#Create a Dictionary, Convert Into a List
print(mylist)					#Print the List

def my_function(x):				#Create a Function
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)

"""
append()	Adds an element at the end of the list
clear()		Removes all the elements from the list
copy()		Returns a copy of the list
count()		Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()		Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()		Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()		Sorts the list
"""