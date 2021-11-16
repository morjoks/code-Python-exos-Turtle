import turtle

turtle1=turtle.Turtle()
turtle1.pencolor("red")
turtle2=turtle.Turtle()
turtle2.pencolor("blue")
turtle3=turtle.Turtle()
turtle3.pencolor("green")
turtle4=turtle.Turtle()
turtle4.pencolor("purple")


"""vitesse des tortues"""
turtle.delay(0)

"""faire un carré
for i in range (4):
    turtle1.forward(100)
    turtle1.left(90)
"""

"""faire un cercle
turtle1.circle(100)
"""

"""faire un escargot rond
r=1
for i in range(300):
    turtle1.circle(r + i,45)
"""

"""faire un escargot carré
for i in range(500):
    turtle1.left(90)
    turtle1.forward(+i*3)
"""

"""faire une marche aléatoire"""
import random

while 1:
    turtle1.forward(10)
    angle = random.randint(-90,90)
    turtle1.left(angle)
    turtle2.forward(10)
    angle = random.randint(-90,90)
    turtle2.left(angle)
    turtle3.forward(10)
    angle = random.randint(-90,90)
    turtle3.left(angle)
    turtle4.forward(10)
    angle = random.randint(-90,90)
    turtle4.left(angle)
input()
