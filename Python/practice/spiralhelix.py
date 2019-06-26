# Python program to draw 
# Spiral Helix Pattern 
# using Turtle Programming 

import turtle 
loadWindow = turtle.Screen() 
turtle.speed(2) 

for i in range(100): 
	turtle.circle(5*i) 
	turtle.circle(-5*i) 
	turtle.left(i) 

turtle.exitonclick() 


#rainbow benzene
# import turtle 
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# t = turtle.Pen() 
# turtle.bgcolor('black') 
# for x in range(360): 
# 	t.pencolor(colors[x%6])                 #divides the color to 6 pens
# 	t.width(x/100 + 1)              #width of the pen
# 	t.forward(x) 
# 	t.left(59)              #59 is the gap between each strands, also decides the shape
