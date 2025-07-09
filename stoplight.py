import turtle 

turtle.speed(1)

turtle.penup()
turtle.goto(-40, 100)
turtle.pendown()
turtle.color("black", "gray")
turtle.begin_fill()

for i in range(2):
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
turtle.end_fill()


turtle.penup()
turtle.goto(0, 40)
turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -20)
turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
