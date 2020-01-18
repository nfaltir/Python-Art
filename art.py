import turtle  
shape = turtle.Turtle() 
  
num_sides = 100
side_length = 10
angle = 360.0 / num_sides  
  
for i in range(num_sides): 
    shape.forward(side_length) 
    shape.right(angle) 

num_sides = 5
side_length = 50
angle = 360.0 / num_sides  
color = '#90EE90'
for i in range(num_sides): 
    shape.forward(side_length) 
    shape.right(angle)
    shape.color(color)
    shape.fillcolor('#90EE90')
    shape.fillcolor()
      
turtle.done() 

