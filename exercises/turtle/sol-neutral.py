import turtle
 
t = turtle.Turtle()
t.color("blue")
t.speed(10)

def figur(h) :
  x = t.xcor()
  y = t.ycor()
  v = t.heading()
  t.forward(100*h/100)
  t.right(100)
  t.forward(40*h/100)
  t.right(160)
  t.forward(40*h/100)
  t.right(100)
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
figur(100)
t.right(20)
figur(90)
t.right(20)
figur(80)
t.right(20)
figur(70)




