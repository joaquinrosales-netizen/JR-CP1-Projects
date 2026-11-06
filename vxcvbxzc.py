import turtle as t

t.hideturtle()

t.color("#f78205")
radius = 100

while radius > 0:
    t.circle(radius)
    t.left(90)
    t.up()
    t.forward(5)
    t.down()
    t.right(90)
    radius -= 5

t.done()