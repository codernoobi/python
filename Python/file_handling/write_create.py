f = open("demofile.txt", "a")
f.write("Now the file has one more line!")		#append content to the file

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")		#overwrite the content

f = open("myfile.txt", "x")					#Create a file
f = open("myfile.txt", "w")				#Create a new file if it does not exist