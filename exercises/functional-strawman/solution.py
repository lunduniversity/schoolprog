import turtle
import math

t = turtle.Turtle()
t.speed(5)
t.getscreen().tracer(10)

def jumpTo(x, y):
  t.penup()
  t.setpos(x,y)
  t.pendown()

# Gubbe
def gubbe():
  jumpTo(0,5)
  t.right(90)
  t.forward(30)
  t.left(30)
  t.forward(120)
  t.left(180)
  t.forward(120)
  t.left(180)
  t.right(60)
  t.forward(120)
  t.right(180)
  t.forward(120)
  t.setheading(90)
  t.forward(50)
  t.right(90)
  t.forward(20)
  t.left(90)
  t.forward(40)
  t.left(90)
  t.forward(40)
  t.left(90)
  t.forward(40)
  t.left(90)
  t.forward(20)

def armar(f):
  for i in range(-100,100):
    plot(i, f(i))

def f(x):
  return 50*math.sin(x* math.pi/200)

def g(x):
  return x / 2.0

def h(x):
  return 50 * math.exp(x/100.0) - 50.0

def plot(x,y):
  jumpTo(x,y)
  t.dot(1)

t.color("green")
gubbe()
t.color("red")
armar(h)
print h(0), h(3), h(-5)
