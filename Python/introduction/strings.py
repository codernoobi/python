txt="  Hello, world"

print(len(txt))	#string length

x=txt[1]	#character in the index
print(x)

x=txt[2:4]	#substring
print(x)

print(txt.strip())	#trim spaces

print(txt.upper())	 #to upper case

print(txt.lower())	 #to lower case

print(txt.replace("H","j"))	#to replace

print(txt.split("e")) 	#splits at e

txt = "Hello World"[::-1]		#reverse string
#Slice the String
print(txt)

def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)