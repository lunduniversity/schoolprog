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

t.setheading(90)
figur(100)
t.right(150)
hop(70)
t.left(120)
figur(70)
t.right(150)
hop(70)
t.left(120)
figur(40)



