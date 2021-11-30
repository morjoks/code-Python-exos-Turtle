"""importation du module 'turtle' """
import turtle

"""appel des tortues et assignation d'une couleur"""
turtle1=turtle.Turtle()
turtle1.pencolor("red")
turtle2=turtle.Turtle()
turtle2.pencolor("blue")
turtle3=turtle.Turtle()
turtle3.pencolor("green")
turtle4=turtle.Turtle()
turtle4.pencolor("cyan")

"""forme de mes tortues"""
turtle1.shape("circle")
turtle2.shape("circle")
turtle3.shape("circle")
turtle4.shape("circle")


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

"""définir une position aléatoire pour l'apparition de mes tortues"""
def posTurtle(tortue):
    X=random.randint(-200,200)
    Y=random.randint(-200,200)
    tortue.penup()
    tortue.goto(X, Y)
    tortue.pendown()

"""appel de la fonction position aléatoire pour que mes tortues aient une position aléatoire lors de leur apparition"""
posTurtle(turtle1)
posTurtle(turtle2)
posTurtle(turtle3)
posTurtle(turtle4)

"""cette partie du code permet de faire se déplacer les tortues de manière aléatoire et infini"""
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