import turtle
import random
import colorgram

'''
colors = colorgram.extract('OIP.jpg', 20)
def randomcolor():
    for i in colors:
        clr = i.rgb
        red=clr.r
        green=clr.g
        blue=clr.b
        color=(red, blue, green)
        print(color)

randomcolor()
'''

turtle.colormode(255)

color_list=[(172, 7, 173),(184, 75, 2),(7, 62, 146),(250, 10, 74),(87, 90, 3),(6, 201, 127),(44, 233, 190),(245, 150, 20),(237, 8, 62),(239, 37, 162),(246, 40, 220),(190, 3, 6),(221, 132, 20),(252, 0, 225),(254, 3, 7),(21, 129, 166)]


timmy= turtle.Turtle()
timmy.shape('turtle')
turtle.speed("fastest")
timmy.penup()
for i in range(10):
    for j in range(10):
        timmy.dot(20,random.choice(color_list))
        if(j!=9):
            timmy.forward(50)
    if i%2==0:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
    else:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)







myscreen = turtle.Screen()
myscreen.exitonclick()