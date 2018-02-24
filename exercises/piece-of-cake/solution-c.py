# Code tested on Python 2.7 in http://repl.it/languages/python-turtle

import turtle

t = turtle.Turtle()

# Jump to a position without drawing
def jumpToPos(pos):
  (x,y) = pos
  t.penup()
  t.setx(x)
  t.sety(y)
  t.pendown()

# Hop forward without drawing
def hop(x):
  t.penup()
  t.forward(x)
  t.pendown()

# Draw a filled rectangle
def drawRect(width, height):
  t.begin_fill()
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.end_fill()

# Slice a rectangle in a number of pieces
def sliceRect(width, height, pieces):
  pieceWidth = float(width)/pieces
  for i in range(pieces-1):
    hop(pieceWidth)
    t.right(90)
    t.forward(height)
    hop(-height)
    t.left(90)
  hop(-pieceWidth*(pieces-1))

# Slice each piece into a number of slices
def slicePieces(width, height, pieces, slices):
  pieceWidth = float(width)/pieces
  for p in range(pieces):
    sliceRect(pieceWidth, height, slices)
    hop(pieceWidth)
  hop(-pieceWidth*(pieces-1))


# Compute the greatest common divisor
def gcd(a, b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a


# Illustrate addition of fractions
def showFractionAdd(n, m):
  # set constants
  t.speed(0)
  t.setheading(0)
  cakeWidth = 300
  cakeHeight = 50
  cake1pos = (-150, 100)
  cake2pos = (-150, 25)
  writepos = (-150, -50)

  # Draw the two cakes
  t.width(3)
  t.color('brown')
  t.fillcolor('pink')
  jumpToPos(cake1pos)
  drawRect(cakeWidth, cakeHeight)
  jumpToPos(cake2pos)
  drawRect(cakeWidth, cakeHeight)

  # Cut cakes in n and m pieces
  t.color('red')
  t.width(5)
  jumpToPos(cake1pos)
  sliceRect(cakeWidth, cakeHeight, n)
  jumpToPos(cake2pos)
  sliceRect(cakeWidth, cakeHeight, m)

  # Eat one piece from each cake
  t.color('brown')
  t.fillcolor('brown')
  t.width(1)
  jumpToPos(cake1pos)
  drawRect(cakeWidth/n, cakeHeight)
  jumpToPos(cake2pos)
  drawRect(cakeWidth/m, cakeHeight)

  # Compute greatest common divisor
  d = gcd(n,m)

  # Slice each piece in m/d and n/d slices
  t.color('blue')
  t.width(1)
  jumpToPos(cake1pos)
  slicePieces(cakeWidth, cakeHeight, n, m/d)
  jumpToPos(cake2pos)
  slicePieces(cakeWidth, cakeHeight, m, n/d)

  # Write equation
  jumpToPos(writepos)
  s1 = "1/"+str(n)
  s2 = "1/"+str(m)
  s3 = str((n+m)/d)+"/"+str((n*m)/d)
  s4 = s1 + " + " + s2 + " = " + s3
  t.write(s4, font=("Arial", 12, "normal"))


# Example call
showFractionAdd(4,6)
