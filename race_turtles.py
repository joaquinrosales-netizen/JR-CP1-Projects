#JR turtle race

import turtle as t
import random

#creates every turtle
turtle_green = t.Turtle()
turtle_green.color('green')
turtle_green.shape('turtle')
turtle_green_speed = random.randint(1, 5)

turtle_green.speed(turtle_green_speed)

turtle_blue = t.Turtle()
turtle_blue.color("blue")
turtle_blue.shape('turtle')
turtle_blue_speed = random.randint(1, 5)
turtle_blue.goto(0, 100)

turtle_blue.speed(turtle_blue_speed)

turtle_red = t.Turtle()
turtle_red.color("red")
turtle_red.shape('turtle')
turtle_red_speed = random.randint(1, 5)
turtle_red.goto(0, -100)

turtle_red.speed(turtle_red_speed)

turtle_yellow = t.Turtle()
turtle_yellow.color("yellow")
turtle_yellow.shape('turtle')
turtle_yellow_speed = random.randint(1, 5)
turtle_yellow.goto(0, 200)

turtle_yellow.speed(turtle_yellow_speed)

turtle_purple = t.Turtle()
turtle_purple.color("purple")
turtle_purple.shape('turtle')
turtle_purple_speed = random.randint(1, 5)
turtle_purple.goto(0, -200)

turtle_purple.speed(turtle_purple_speed)

turtle_orange = t.Turtle()
turtle_orange.color("orange")
turtle_orange.shape('turtle')
turtle_orange_speed = random.randint(1, 5)
turtle_orange.goto(0, -300)

turtle_orange.speed(turtle_orange_speed)

#creates the finish line
finish_line = t.Turtle()
finish_line.hideturtle()
finish_line.speed(0)
finish_line.penup()
finish_line.goto(500, -400)
finish_line.pendown()
finish_line.goto(500, 400)

#Sets the turtles to start running
while True:
    turtle_green.forward(turtle_green_speed)
    turtle_blue.forward(turtle_blue_speed)
    turtle_red.forward(turtle_red_speed)
    turtle_yellow.forward(turtle_yellow_speed)
    turtle_purple.forward(turtle_purple_speed)
    turtle_orange.forward(turtle_orange_speed)

#checks who is the winner
    if turtle_green.xcor() >= 500:
        print("Green turtle wins!")
        break
    elif turtle_blue.xcor() >= 500:
        print("Blue turtle wins!")
        break
    elif turtle_red.xcor() >= 500:
        print("Red turtle wins!")
        break
    elif turtle_yellow.xcor() >= 500:
        print("Yellow turtle wins!")
        break
    elif turtle_purple.xcor() >= 500:
        print("Purple turtle wins!")
        break
    elif turtle_orange.xcor() >= 500:
        print("Orange turtle wins!")
        break
t.done()