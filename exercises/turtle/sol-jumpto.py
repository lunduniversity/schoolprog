import turtle
 
t = turtle.Turtle()
t.color("blue")
t.speed(10)

def figur(h) :
  t.forward(100*h/100)
  t.right(100)
  t.forward(40*h/100)
  t.right(160)
  t.forward(40*h/100)
  t.right(100)


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
t.right(10)
jumpTo(20,0)
figur(70)
t.right(10)
jumpTo(40,0)
figur(40)



