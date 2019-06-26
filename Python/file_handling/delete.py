import os
os.remove("demofile.txt")			#To delete a file, you must import the OS module, and run its os.remove() function

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")			#Check if file exist, then delete it

os.rmdir("myfolder")				#Remove the folder "myfolder"