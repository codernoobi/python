import json			#import jsn module
#if you have a JSON string, you can parse it by using the json.loads() method.

#Convert from JSON to Python
x =  '{ "name":"John", "age":30, "city":"New York"}'		# some JSON
y = json.loads(x)			# parse x
print(y["age"])				# the result is a Python dictionary

#Convert from Python to JSON
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}							## a Python object (dict)
y = json.dumps(x)			# convert into JSON
print(y)					# the result is a JSON string

"""
You can convert Python objects of the following types, into JSON strings:

Python		JSON
dict		Object
list		Array
tuple		Array
str			String
int			Number
float		Number
True		true
False		false
None		null
"""

#Convert Python objects into JSON strings, and print the values
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert a Python object containing all the legal data types
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

json.dumps(x, indent=4)		#The json.dumps() method has parameters to make it easier to read the result
json.dumps(x, indent=4, separators=(". ", " = "))		#use of seperators parameter
json.dumps(x, indent=4, sort_keys=True)		#sort_keys parameter to sort output