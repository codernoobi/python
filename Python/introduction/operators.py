a=10
b=10;

print(10*10)

c=a+b;
print (c);

print(a/b)

if c!=a:
	print("c not equal to a")

if c>a:
	print("c is greater")

if 5 == 10 or 4 == 4:									#or
  print("At least one of the statements is true")

if 5 == 10 and 4 == 4:									#and
  print("Both of the statements is true")

fruits = ["apple", "banana"]
if "apple" in fruits:									#in
  print("Yes, apple is a fruit!")



"""
Arithematic
+		Addition			x + y	
-		Subtraction			x - y	
*		Multiplication		x * y	
/		Division			x / y	
%		Modulus				x % y	
**		Exponentiation		x ** y	 
//		Floor division		x // y

Assignment
=		x = 5		x = 5	
+=		x += 3		x = x + 3	
-=		x -= 3		x = x - 3	
*=		x *= 3		x = x * 3	
/=		x /= 3		x = x / 3	
%=		x %= 3		x = x % 3	
//=		x //= 3		x = x // 3	
**=		x **= 3		x = x ** 3	
&=		x &= 3		x = x & 3	
|=		x |= 3		x = x | 3	
^=		x ^= 3		x = x ^ 3	
>>=		x >>= 3		x = x >> 3	
<<=		x <<= 3		x = x << 3

Comparision
==		Equal						x == y	
!=		Not equal					x != y	
>		Greater than				x > y	
<		Less than					x < y	
>=		Greater than or equal to	x >= y	
<=		Less than or equal to		x <= y

Logical
and 	Returns True if both statements are true						x < 5 and  x < 10	
or		Returns True if one of the statements is true					x < 5 or x < 4	
not		Reverse the result, returns False if the result is true			not(x < 5 and x < 10)

Identity
is 			Returns true if both variables are the same object			x is y	
is not		Returns true if both variables are not the same object		x is not y

Membership
in 			Returns True if a sequence with the specified value is present in the object			x in y	
not in		Returns True if a sequence with the specified value is not present in the object		x not in y

Bitwise
& 		AND						Sets each bit to 1 if both bits are 1
|		OR						Sets each bit to 1 if one of two bits is 1
^		XOR						Sets each bit to 1 if only one of two bits is 1
~ 		NOT						Inverts all the bits
<<		Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>		Signed right shift		Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

