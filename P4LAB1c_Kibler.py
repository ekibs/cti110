import turtle
turtle.colormode(255)
turtle.color(0, 0, 255)
turtle.width(3)
turtle.left(90)

for i in range(0,9):
    turtle.forward(100)
    turtle.backward(40)
    turtle.left(40)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(80)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(20)
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(40)
    turtle.forward(30)
    turtle.backward(30)
    turtle.left(40)
    turtle.backward(60)

    turtle.right(60)


turtle.exitonclick()