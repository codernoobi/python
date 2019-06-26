car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}								#create dictioary
print(car.get("model"))			#get method, key model
x = car["model"]
print(x)

car["year"] = 2018				#change year value
print(car)

car["color"] = "red"			#adding new key value pair
print(car)

for x in car:					#for
  print(x)

for x, y in car.items():		#Loop through both keys and values, by using the items() function
  print(x, y)

if "model" in car:				#Check if "model" is present in the dictionary
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(len(car))					#number of elements

car.pop("model")				#pop method to remove model
print(car)

car.popitem()					#popitem method
print(car)

car.clear()						#clear method to empty the dictionary
print(car)

del car["model"]
print(car)					#The del keyword removes the item with the specified key name

del car 					#delete the dictionary

car =	dict(brand="Ford", model="Mustang", year=1964)			# note that keywords are not string literals
																	# note the use of equals rather than colon for the assignment
print(car)


"""
Method			Description
clear()			Removes all the elements from the dictionary
copy()			Returns a copy of the dictionary
fromkeys()		Returns a dictionary with the specified keys and values
get()			Returns the value of the specified key
items()			Returns a list containing the a tuple for each key value pair
keys()			Returns a list contianing the dictionary's keys
pop()			Removes the element with the specified key
popitem()		Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()		Updates the dictionary with the specified key-value pairs
values()		Returns a list of all the values in the dictionary
"""