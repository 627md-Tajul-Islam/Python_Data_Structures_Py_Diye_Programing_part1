import turtle
import random

turtle.penup()

for i in range(100):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.set_position(x,y)
    turtle.dot()