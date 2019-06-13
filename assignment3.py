import turtle
import time

from turtle import*

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



bb.hideturtle()
time.sleep(1)
bb.showturtle()
bb.clear()

aa.hideturtle()
time.sleep(1)
aa.showturtle()
aa.clear()



def square(t,n):
  t.fd(n)
  t.rt(90)
  t.fd(n)
  t.rt(90)
  

bb=Turtle()
bb.color("blue")
bb.shape("turtle")
square(bb,100)


for i in range (1):
  square(bb,100)
  bb.rt(90)

bb.hideturtle()
time.sleep(1)
bb.showturtle()
bb.clear()

def octagon(t,n):
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)
  t.fd(n)
  t.rt(45)

bb=Turtle()
bb.color("blue") 
bb.shape("turtle")
octagon(bb,100)

bb.hideturtle()
time.sleep(1)
bb.showturtle()
bb.clear()

def pentagon(t,n):
  t.fd(n)
  t.rd(72)
  t.fd(n)
  t.rd(72)

def square(t,n):
  t.fd(n)
  t.rt(60)
  t.fd(n)
  t.rt(60)
  t.fd(n)
  t.rt(60)
  t.fd(n)
  t.rt(60)
  t.fd(n)
  t.rt(60)
  t.fd(n)
  t.rt(60)


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
