"""
an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator
"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)			#Return a iterator from a tuple
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"		#Strings are also iterable objects
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")		#loop to iterate through an iterable object
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)


class MyNumbers:					#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:				#limit the iteration to 20 using stop iteration
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)