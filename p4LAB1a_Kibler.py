import turtle
drawAgain = "yes"
while drawAgain == "yes":
    answer = str(input("Draw a square and a triangle? (yes or no): "))
    if answer == "yes" or answer == "Yes":
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.penup()

        turtle.right(90)
        turtle.forward(100)
        turtle.right(60)
        turtle.pendown()
        turtle.forward(55)
        turtle.right(120)
        turtle.forward(55)
        turtle.right(120)
        turtle.forward(55)

        drawAgain = str(input("Would you like to run the program again? (yes or no): "))
        turtle.reset()
    else:
        drawAgain = "no"
        turtle.exitonclick()
print("Goodbye.")
