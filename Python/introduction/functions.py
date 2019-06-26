x=10
a=1

def my_function():					#define function
  print("Hello from a function")

my_function()						#function call

def my_function(fname, lname):
  print(fname)						#print first parameter

my_function("akash", "hr")

def my_function(country = "Norway"):			#default parameter
  print("I am from " + country)
my_function("India")
my_function()
my_function("Brazil")

def my_function(x):
  return 5 * x						#return statement
print(my_function(3))
print(my_function(5))
print(my_function(9))


#lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression

x = lambda a : a + 10
print(x(5))					#adds 10 to the number passed in as an argument

x = lambda a, b : a * b
print(x(5, 6))				#multiplies argument a with argument b 
				
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))			#sums argument a, b, and c

def myfunc(n):					# The power of lambda is better shown when you use them as an anonymous function inside another function.
	return lambda a : a * n		# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number

mydoubler = myfunc(2)				#Use that function definition to make a function that always doubles the number you send in
print(mydoubler(11))

mytripler = myfunc(3)				#Use that function definition to make a function that always triples the number you send in
print(mytripler(11))

mydoubler = myfunc(2)
mytripler = myfunc(3)				#use the same function definition to make both functions, in the same program
print(mydoubler(11)) 
print(mytripler(11))