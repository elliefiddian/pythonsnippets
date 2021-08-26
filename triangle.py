import turtle

side_length = 100
angle = 120

turtle.color('blue', 'green')
turtle.begin_fill()

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.forward(side_length)
turtle.right(angle)

turtle.speed('fastest')

turtle.end_fill()
turtle.done()
