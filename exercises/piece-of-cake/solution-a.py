# Code tested on Python 2.7 in http://repl.it/languages/python-turtle

import turtle

t = turtle.Turtle()


# Jump to a position without drawing anything
def jumpTo(x,y):
  t.penup()
  t.setx(x)
  t.sety(y)
  t.pendown()

# Jump to a position given as a pair of coordinates
def jumpToPos(pos):
  (x,y) = pos
  jumpTo(x,y)

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
  hop(-pieceWidth*(pieces-1)) # Go back to original pos

# Slice each piece into a number of slices
def slicePieces(width, height, pieces, slices):
  pieceWidth = float(width)/pieces
  for p in range(pieces):
    sliceRect(pieceWidth, height, slices)
    hop(pieceWidth)
  hop(-(pieceWidth)*(pieces)) # Go back to original pos

# set constants
t.speed(0)
t.setheading(0)
cakeWidth = 300
cakeHeight = 50
cake1pos = (-150, 100)
cake2pos = (-150, 25)

# Draw the two cakes
t.width(3)
t.color('brown')
t.fillcolor('pink')
jumpToPos(cake1pos)
drawRect(cakeWidth, cakeHeight)
jumpToPos(cake2pos)
drawRect(cakeWidth, cakeHeight)

# Cut cakes in 3 and 4 pieces
t.color('red')
t.width(5)
jumpToPos(cake1pos)
sliceRect(cakeWidth, cakeHeight, 3)
jumpToPos(cake2pos)
sliceRect(cakeWidth, cakeHeight, 4)

# Eat one piece from each cake
t.color('brown')
t.fillcolor('brown')
t.width(1)
jumpToPos(cake1pos)
drawRect(cakeWidth/3, cakeHeight)
jumpToPos(cake2pos)
drawRect(cakeWidth/4, cakeHeight)

# Slice each piece in 4 and 3 slices
t.color('blue')
t.width(1)
jumpToPos(cake1pos)
slicePieces(cakeWidth, cakeHeight, 3, 4)
jumpToPos(cake2pos)
slicePieces(cakeWidth, cakeHeight, 4, 3)
