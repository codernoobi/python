"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks
"""

try:
  print(x)
except:
  print("An exception occurred")		

"""
The try block will generate an exception, because x is not defined
Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error
"""

try:					#Print one message if the try block raises a NameError and another for other errors
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")		#the else keyword to define a block of code to be executed if no errors were raised

try:							#The finally block, if specified, will be executed regardless if the try block raises an error or not
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:						#Try to open and write to a file that is not writable
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()