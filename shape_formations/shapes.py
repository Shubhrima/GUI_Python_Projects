from turtle import Turtle, Screen
import random

timmy= Turtle()
timmy.shape('turtle')

colors=["coral","aqua","black","green","magenta","red","orange"]
def timmyshape(num):
    for i in range(0,num):
        timmy.forward(100)
        timmy.right(360/num)


for i in range(3,10):
    timmy.color(random.choice(colors))
    timmy.pensize(10)
    timmyshape(i)







myscreen = Screen()
myscreen.exitonclick()