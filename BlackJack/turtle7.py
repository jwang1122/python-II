"""
Display cards on turtle screen
"""
from turtle import *

screen = Screen()
imgClub2 = r"images/club2.gif"
screen.addshape(imgClub2)
imgheartQ = r"images/heartQ.gif"
screen.addshape(imgheartQ)
clubK = Turtle()
clubK.shape(imgClub2)
clubK.pu()
clubK.goto(100, 200)
clubK.showturtle()

heartQ = Turtle()
heartQ.shape(imgheartQ)
heartQ.pu()
heartQ.goto(130, 200)
heartQ.showturtle()
id = heartQ.stamp()

heartQ.goto(130, -200)

pen = Turtle()
pen.hideturtle()

for i in range(2):
    pen.fd(80)
    pen.left(90)
    pen.fd(30)
    pen.left(90)

pen.penup()
pen.goto(7, 6)
pen.write("Hit", font=("Arial", 12, "normal"))
pen.hideturtle()

def btnclick(x, y):
    if x > 0 and x < 81 and y > 0 and y < 31:
        print("Hi, the button is clicked.")
        clearstamps()


onscreenclick(btnclick, 1)
listen()


mainloop()