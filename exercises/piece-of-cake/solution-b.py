import turtle

t = turtle.Turtle()
t.speed(0)
cakeWidth = 300
cakeHeight = 50

# Jump to a position without drawing
def jumpTo(x,y):
  t.penup()
  t.setx(x)
  t.sety(y)
  t.pendown()

# Draw a filled rectangle
def drawFilledRect(width, height):
  savex = t.xcor()
  savey = t.ycor()
  t.setheading(0)
  t.fill(True)
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.forward(width)
  t.right(90)
  t.forward(height)
  t.right(90)
  t.fill(False)
  t.setpos(savex, savey)

# Slice a rectangle in a number of pieces
def sliceRect(width, height, pieces):
  savex = t.xcor()
  savey = t.ycor()
  pieceWidth = float(width)/pieces
  for i in range(pieces-1):
    t.penup()
    t.setheading(0)
    t.forward(pieceWidth)
    t.right(90)
    t.pendown()
    t.forward(height)
    t.penup()
    t.backward(height)
  t.setpos(savex, savey)

# Slice each piece into a number of slices
def slicePieces(width, height, pieces, slices):
  savex = t.xcor()
  savey = t.ycor()
  pieceWidth = float(width)/pieces
  for p in range(pieces):
    sliceRect(pieceWidth, height, slices)
    t.penup()
    t.setheading(0)
    t.forward(pieceWidth)
  t.setpos(savex, savey)

# Illustrate addition of fractions
def showFractionAdd(n, m):
  # Draw the two cakes
  t.width(3)
  t.color('brown')
  t.fillcolor('pink')
  jumpTo(-150, 100)
  drawFilledRect(cakeWidth, cakeHeight)
  jumpTo(-150, 25)
  drawFilledRect(cakeWidth, cakeHeight)
  # Cut cakes in n and m pieces
  t.color('red')
  t.width(5)
  jumpTo(-150, 100)
  sliceRect(cakeWidth, cakeHeight, n)
  jumpTo(-150, 25)
  sliceRect(cakeWidth, cakeHeight, m)
  # Eat one piece from each cake
  t.color('brown')
  t.fillcolor('brown')
  t.width(1)
  jumpTo(-150, 100)
  drawFilledRect(cakeWidth/n, cakeHeight)
  jumpTo(-150, 25)
  drawFilledRect(cakeWidth/m, cakeHeight)
  # Slice each piece in m and n slices
  t.color('blue')
  t.width(1)
  jumpTo(-150, 100)
  slicePieces(cakeWidth, cakeHeight, n, m)
  jumpTo(-150, 25)
  slicePieces(cakeWidth, cakeHeight, m, n)
  # Write equation
  jumpTo(-150, -50)
  s1 = "1/"+str(n)
  s2 = "1/"+str(m)
  s3 = str(n+m)+"/"+str(n*m)
  s4 = s1 + " + " + s2 + " = " + s3
  t.write(s4, font=("Arial", 12, "normal"))
  jumpTo(-150, 50)

# Example call
showFractionAdd(2,5)
