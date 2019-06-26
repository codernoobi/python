class MyClass:		#create class
  x = 5

p1 = MyClass()		#create object
print(p1.x)

class Person:		#Create a class named Person, use the __init__() function to assign values for name and age
  def __init__(self, name1, age1):		#__init__() function
    self.name = name1
    self.age = age1

p1 = Person("John", 36)
print(p1.name)
print(p1.age)			# The __init__() function is called automatically every time the class is being used to create a new object.


class Person:		
  def __init__(self, name1, age1):		
    self.name = name1
    self.age = age1

  def myfunc(self):				#creating a new function in class
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()			

# The self parameter is a reference to the class instance itself, and is used to access variables that belongs to the class.

"""The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print(p1.age)
p1.age = 40		#modify object properties
print(p1.age)

del p1.age		#delete object property
del p1		#delete object

