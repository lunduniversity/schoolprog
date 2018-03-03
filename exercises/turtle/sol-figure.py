import turtle
 
t = turtle.Turtle()
t.color("blue")
t.speed(10)

def vimpel() :
  t.forward(100)
  t.right(100)
  t.forward(40)
  t.right(160)
  t.forward(40)
  t.right(100)


t.setheading(90)
vimpel()
t.right(150)
t.penup()
t.forward(60)
t.pendown()
t.left(150)
t.right(50)
vimpel()
t.right(150)
t.penup()
t.forward(60)
t.pendown()
t.left(150)
t.right(50)
vimpel()