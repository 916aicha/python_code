import turtle 
import time

t = turtle.Turtle()
t.clear()
t.color("blue")
t.shape("turtle")
t.speed(20) 

from turtle import *
def triangle(t , n):
	t.fd(n)
	t.rt(120)
	t.fd(n)
	t.rt(120)
	t.fd(n)
	t.rt(120)


bb = Turtle()
bb.color("blue")
bb.shape("turtle")
triangle(bb,100)

aa = Turtle()
aa.color("red")
aa.shape("classic")
aa.right(30)
triangle(aa,100)

for i in range(10):
	triangle(bb,100)
	bb.rt(36)


t.hideturtle()
time.sleep(1)
bb.hideturtle()
bb.clear()

from turtle import*
import time

def square(t , n):
  fd(n)
  rt(60)
  fd(n)
  rt(60)
  fd(n)
  rt(60)
  fd(n)
  rt(60)
  fd(n)
  rt(60)
  fd(n)
  rt(60)


bb = Turtle()
bb.color("blue") 
bb.shape("turtle")
square(bb,100)

for i in range(2):
  bb.rt(60)
  bb.fd(100)

bb.penup()
bb.rt(180)
bb.fd(100)
bb.pendown()

bb.rt(60)
bb.fd(100)

bb.hideturtle()
time.sleep(1)
bb.hideturtle()
t.clear()

Assignment 3


def triangle (t,n):
  t.fd(n)
  t.rt(120)
  t.fd(n)
  t.rt(120)
  t.fd(n)
  t.rt(120)



bb=Turtle()
bb.color("blue")
bb.shape("turtle")
triangle(bb,100)

aa=Turtle
aa.color("red")
aa.shape("classic")
aa.right(30)
triangle(aa,100)

for i in range (10):
  triangle(bb,100)
  bb.rt(36)


'''
Assigment 3.1
'''

shape("circle")
shapesize(5,1,2)
fillcolor("red")
pencolor("darkred")

penup()
goto(0,-100)

for i in range(72):
  forward(10)
  left(5)
  tilt(7.5)
  stamp()

exitonclick()

from turtle import *

# set a shape and colour
shape("circle")
shapesize(5,1,2)
fillcolor("red")
pencolor("darkred")

penup() # no drawing
goto(0, -100)

# main draw loop
for i in range(72):
  forward(10)
  left(5)
  tilt(7.5)
  stamp()

exitonclick()

Assigment 3.1


shape("circle")
shapesize(5,1,2)
fillcolor("red")
pencolor("darkred")

penup()
goto(0,-100)

for i in range(72):
  forward(10)
  left(5)
  tilt(7.5)
  stamp()

exitonclick()

from turtle import *

# set a shape and colour
shape("circle")
shapesize(5,1,2)
fillcolor("red")
pencolor("darkred")

penup() # no drawing
goto(0, -100)

# main draw loop
for i in range(72):
  forward(10)
  left(5)
  tilt(7.5)
  stamp()

exitonclick()
