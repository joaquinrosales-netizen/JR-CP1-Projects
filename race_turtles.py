#JR turtle race

import turtle as t
import random

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

t.done()