from turtle import *
pensize(10)
pencolor('blue')

fillcolor('red')

begin_fill()

# loop for square
for i in range(5):
    forward(100)
    left(90)

end_fill()
    
# pick the pen up and move it to the right
penup()
right(90)
forward(150)

begin_fill()

# put the pen down and loop for triangle
pendown()
forward(120)
left(135)
forward(90)
left(90)
forward(90)
    
end_fill()
