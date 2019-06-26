import mymodules				#define mymodules
#import mymodules as mx			#You can create an alias when you import a module, by using the as keyword

mymodules.greeting("Jonathan")		#call the function greeting

a = mymodules.person1["age"]		#The module can contain functions, as already described, but also variables of all types
print(a)

"""
a = mx.person1["age"]			#if alias is used while importing
print(a)
"""

import platform						#built_in modules
x = platform.system()
print(x)

"""x = dir(platform)				#built_in function to list all the functions/variables in a module
print(x)						#The dir() function can be used on all modules, also the ones you create yourself.
"""

from mymodules import person1	#Import only the person1 dictionary from the module:
print (person1["age"])

"""
When importing using the from keyword, do not use the module name when referring to elements in the module.
Example: person1["age"], not mymodule.person1["age"]
"""