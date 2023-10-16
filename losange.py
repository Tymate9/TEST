import turtle
for i in range(3):
    angle = 120
    for a in range(4):
        turtle.color("blue", "pink")
        turtle.forward(100)
        turtle.left(angle)
        angle = 180-angle
    turtle.right(120)
    turtle.hideturtle()
turtle.done()