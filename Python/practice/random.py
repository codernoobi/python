import random			#import only random module
import numpy as np

#print(random.randint(1,101))		#print once

l=list(("0"))
x=len(l)
while x <57:
  a=random.randint(1,56)		#print multiple
  if a not in l:
    l.append(a)               #if it is not repeating add to list
    x+=1
      
print(len(l))
myarray = np.asarray(l)
#print(myarray)
for x in myarray:
  print(x)
