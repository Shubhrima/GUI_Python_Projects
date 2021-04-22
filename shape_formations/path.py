import turtle
import random

timmy= turtle.Turtle()
timmy.shape('turtle')
turtle.colormode(255)

def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colours= (r, g, b)
    return colours

nums=[0,90,180,270]

def timmyshape(num):
    timmy.right(num)
    timmy.forward(20)


for i in range(3,500):
    timmy.color(randomcolor())
    timmy.pensize(10)
    timmy.speed("fastest")
    timmyshape(random.choice(nums))







myscreen = Screen()
myscreen.exitonclick()