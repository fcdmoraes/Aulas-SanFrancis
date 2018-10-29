import turtle
import random

leo = turtle.Turtle()
leo.shape('turtle')
leo.color('blue','red')


##leo.begin_fill()
###leo.penup()
##leo.goto(100,100)
###leo. pendown()
##leo.goto(100,0)
##leo.goto(0,0)
##
##leo.end_fill()
leo.speed(-1)
leo.pu()
leo.goto(-250,-100)
leo.pd()
leo.left(90)
for j in range(10):
    leo.begin_fill()
    for i in range(4):
        leo.fd(10)
        leo.left(90)
    leo.end_fill()
    leo.fd(10)
    leo.begin_fill()
    for i in range(4):
        leo.fd(10)
        leo.right(90)
    leo.end_fill()
    leo.fd(10)
leo.ht()

t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('purple')
t1.pu()
t1.goto(-260,50)

t2 = turtle.Turtle()
t2.shape('turtle')
t2.color('green')
t2.pu()
t2.goto(-260,0)

t3 = turtle.Turtle()
t3.shape('turtle')
t3.color('orange')
t3.pu()
t3.goto(-260,-50)

for i in range(200):
    r = random.randint(1,6)
    t1.fd(r)
    r = random.randint(1,6)
    t2.fd(r)
    r = random.randint(1,6)
    t3.fd(r)
    if t1.xcor() >= 260:
        break
    if t2.xcor() >= 260:
        break
    if t3.xcor() >= 260:
        break

turtle.mainloop()
