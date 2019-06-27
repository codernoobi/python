import numpy as np
import matplotlib.pyplot as plt

#degree 1
x = np.arange(-5.0, 5.0, 0.1)
##You can adjust the slope and intercept to verify the changes in the graph

y = 2*(x) + 3
y_noise = 2 * np.random.normal(size=x.size)
ydata = y + y_noise
#plt.figure(figsize=(8,6))
plt.plot(x, ydata,  'bo')
plt.plot(x,y, 'r') 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

#cubic function's graph.
y = 1*(x**3) + 1*(x**2) + 1*x + 3
y_noise = 20 * np.random.normal(size=x.size)
ydata = y + y_noise
plt.plot(x, ydata,  'bo')
plt.plot(x,y, 'r') 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

#Quadratic
#𝑌=𝑋2
y = np.power(x,2)
y_noise = 2 * np.random.normal(size=x.size)
ydata = y + y_noise
plt.plot(x, ydata,  'bo')
plt.plot(x,y, 'r') 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

# Exponential
# An exponential function with base c is defined by
# 𝑌=𝑎+𝑏𝑐𝑋 
# where b ≠0, c > 0 , c ≠1, and x is any real number. The base, c, is constant and the exponent, x, is a variable.
 
Y=np.exp(X)
plt.plot(X,Y) 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

# Logarithmic
# The response  𝑦  is a results of applying logarithmic map from input  𝑥 's to output variable  𝑦 . It is one of the simplest form of log(): i.e.
# 𝑦=log(𝑥) 
# Please consider that instead of  𝑥 , we can use  𝑋 , which can be polynomial representation of the  𝑥 's. In general form it would be written as
# 𝑦=log(𝑋)

# X = np.arange(-5.0, 5.0, 0.1)
# Y = np.log(X)​
# plt.plot(X,Y) 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()

# # Sigmoidal/Logistic
# # 𝑌=𝑎+𝑏1+𝑐(𝑋−𝑑)
# ​
# Y = 1-4/(1+np.power(3, X-2))​
# plt.plot(X,Y) 
# plt.ylabel('Dependent Variable')
# plt.xlabel('Indepdendent Variable')
# plt.show()
