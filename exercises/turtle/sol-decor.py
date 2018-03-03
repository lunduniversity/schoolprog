import turtle
 
t = turtle.Turtle()
t.color("blue")
t.speed(50)

def figur(h) :
  x = t.xcor()
  y = t.ycor()
  v = t.heading()
  t.fill(True)
  t.forward(100*h/100)
  t.right(100)
  t.forward(40*h/100)
  t.right(160)
  t.forward(40*h/100)
  t.right(100)
  t.fill(False)
  jumpTo(x,y)
  t.setheading(v)

def cluster(h):
  x = t.xcor()
  y = t.ycor()
  v = t.heading()
  for c in range(4):
    figur(h)
    t.right(20)
    hop(20)
    t.left(20)
  jumpTo(x,y)
  t.setheading(v)

def hop(length) :
  t.penup()
  t.forward(length)
  t.pendown()

def jumpTo(x, y) :
  t.penup()
  t.setpos(x,y)
  t.pendown()

t.setheading(90)
t.color("blue")
cluster(100)
jumpTo(50, 0)
t.color("red")
cluster(100)
jumpTo(100,0)
t.color("green")
cluster(100)


