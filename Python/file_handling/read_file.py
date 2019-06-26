f = open("demofile.txt", "r")		#The open() function returns a file object, which has a read() method for reading the content of the file
print(f.read())

f = open("demofile.txt", "r")		#By default the read() method returns the whole text, but you can also specify how many character you want to return
print(f.read(2))				#Return the 2 first characters of the file

f = open("demofile.txt", "r")
print(f.readline())				#return one line by using the readline() method
								#readlines() reads all the lines

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

f = open("demofile.txt", "r")
for x in f:
  print(x)						#Loop through the file line by line