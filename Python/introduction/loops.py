i = 1
while i < 6:				#while
  print(i)
  i += 1


i = 1
while i < 6:
	print(i)
	if i == 3:  
	    break
	i+= 1

"""
i = 1
while i < 6:
	print(i)
	if i == 3:  
	    continue
	i+= 1
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:			#in, for
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
  	continue					#contiue
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
  	break					#break
  print(x)

for x in "Banana":
	print(x)

i=1
for x in range(6):			#range
  print(x)

for x in range(2, 6):		#using start paameter
  print(x)

for x in range(2, 30, 3):		#increment of 3
  print(x)

for x in range(6):					#else in for loop
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]			#nested loops
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

n = int(input())
i = 1
a=1
while a < n:
    a+=1
    i=str(i)+str(a)   
    
print(i)