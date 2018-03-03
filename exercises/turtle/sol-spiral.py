import turtle
 
t = turtle.Turtle()
t.color("blue")
t.speed(10)

for c in range(16):
  t.forward(50+c*10)
  t.left(90)
