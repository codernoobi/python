#turtle is graphics module
import turtle 				#import

"""
turtle.speed(666)
turtle.color(0,0,0)			#color that is used to draw
wn = turtle.Screen()		#defining the screen
wn.bgcolor("light green")	#color of the output window
wn.title("Turtle")			#title of output window
while True:
	turtle.left(185.5)		#rotates aticlockwise
	turtle.forward(200)		#the movement of the pen
"""

"""
#hexagon 
polygon = turtle.Turtle() 

num_sides = 6
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides): 
	polygon.forward(side_length) 
	polygon.right(angle) 
	
turtle.done() 
"""

"""
#star
star = turtle.Turtle() 

for i in range(50): 
	star.forward(50) 
	star.right(144) 
	
turtle.done() 
"""

"""
#square 
skk = turtle.Turtle() 

for i in range(4): 
	skk.forward(50) 
	skk.right(90) 
	
turtle.done() 
"""

# Spiral Square Outside In and Inside Out 
wn = turtle.Screen() 
wn.bgcolor("light green") 
wn.title("Turtle") 
skk = turtle.Turtle() 
skk.color("blue") 

#outside in
"""
def sqrfunc(size): 
	for i in range(4): 
		skk.fd(size) 
		skk.left(90) 
		size = size-5

sqrfunc(146) 
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
"""
#inside out
def sqrfunc(size): 
	for i in range(4): 
		skk.fd(size) 
		skk.left(90) 
		size = size + 5

sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46) 
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146) 

sqrfunc(26) 
