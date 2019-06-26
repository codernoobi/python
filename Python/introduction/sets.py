fruits = {"apple", "banana", "cherry"}		#create set
print(fruits)

if ("apple" in fruits):						#check if apple is in set
  print("Yes, apple is a fruit!")

for x in fruits:							#for
	print(x)

print("banana" in fruits)					#chcek condition

#Once a set is created, you cannot change its items, but you can add new items.

fruits.add("orange")						#add net set element

more_fruits = ["orange", "mango", "grapes"]	#multiple items list
fruits.update(more_fruits)					#update fruits set with list
print(fruits)

print(len(fruits))							#number of elements in fruits

fruits.remove("banana")						#remove item from set
print(fruits)

fruits.discard("cherry")					# remove using discard

x = thisset.pop()
print(x)									#remove last element using pop

fruits.clear()								#empties the set

del fruits 									#delets the set

fruits = set(("apple", "banana", "cherry")) #set constructor
print(fruits)

"""
Method							Description

add()							Adds an element to the set
clear()							Removes all the elements from the set
copy()							Returns a copy of the set
difference()					Returns a set containing the difference between two or more sets
difference_update()				Removes the items in this set that are also included in another, specified set
discard()						Remove the specified item
intersection()					Returns a set, that is the intersection of two other sets
intersection_update()			Removes the items in this set that are not present in other, specified set(s)
isdisjoint()					Returns whether two sets have a intersection or not
issubset()						Returns whether another set contains this set or not
issuperset()					Returns whether this set contains another set or not
pop()							Removes the specified element
remove()						Removes the specified element
symmetric_difference()			Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()							Return a set containing the union of sets
update()						Update the set with the union of this set and others
"""