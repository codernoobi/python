a = 50
b = 10
c = 20
d = 30

if a > b:					
  print("Hello World")

if a != b:
  print("Hello World")

if a == b:						#iflese
  print("Yes")
else:
  print("No")

if a == b:						#if elseif else
  print("1")
elif a > b:
  print("2")
else:
  print("3")

if a == b and c == d:			#and
  print("Hello")

if a == b or c == d:			#or
  print("Hello")

if a > b: print("a is greater than b")		#one line if

print("A") if a > b else print("B")			#one line ifelse

print("A") if a > b else print("=") if a == b else print("B")		#one line many conditions