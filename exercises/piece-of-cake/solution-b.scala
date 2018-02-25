// Helper function for coding repetition
def repeat(n: Int)(f: => Unit) { 
  if (n > 0) {
    f
    repeat(n-1)(f)
  }
}

// Jump to position with x and y values
def jumpTo(x: Int, y: Int) = {
  setPosition(x,y);
}

// Jump to position with (x,y) value
def jumpToPos(pos:(Int, Int)) = {
  val (x,y) = pos
  setPosition(x,y)
}

// Draw a rectangle
def drawRect(width:Int, height:Int) = {
  forward(width)
  right(90)
  forward(height)
  right(90)
  forward(width)
  right(90)
  forward(height)
  right(90)
}

// Slice a rectangle in a number of pieces
def sliceRect(width:Double, height:Double, pieces:Int) = {
  val pieceWidth = width/pieces
  repeat (pieces-1) {
    hop(pieceWidth)
    right(90)
    forward(height)
    hop(-height)
    left(90)
  }
  hop(-(pieceWidth)*(pieces-1)) // hop back to initial position
}

// Slice each piece into a number of slices
def slicePieces(width:Double, height:Double, pieces:Int, slices:Int) = {
  val pieceWidth = width/pieces
  repeat (pieces) {
    sliceRect(pieceWidth, height, slices)
    hop(pieceWidth)
  }
  hop(-(pieceWidth)*(pieces))
}

def showFractionAdd(n:Int, m:Int) = {
  // set constants
  setAnimationDelay(0)
  setHeading(0)
  val cakeWidth = 300
  val cakeHeight = 50
  val cake1pos = (-50, 75)
  val cake2pos = (-50, 0)
  val writepos = (-50, -75)
  
  // Draw the two cakes
  setPenThickness(3)
  setPenColor(brown)
  setFillColor(pink)
  jumpToPos(cake1pos)
  drawRect(cakeWidth,cakeHeight)
  jumpToPos(cake2pos)
  drawRect(cakeWidth, cakeHeight)

  // Cut cakes in n and m pieces
  setPenColor(red)
  setPenThickness(5)
  jumpToPos(cake1pos)
  sliceRect(cakeWidth, cakeHeight, n)
  jumpToPos(cake2pos)
  sliceRect(cakeWidth, cakeHeight, m)
  
  // Eat one piece from each cake
  setPenColor(brown)
  setFillColor(brown)
  setPenThickness(1)
  jumpToPos(cake1pos)
  drawRect(cakeWidth/n, cakeHeight)
  jumpToPos(cake2pos)
  drawRect(cakeWidth/m, cakeHeight)
  
  // Slice each piece in m and n slices
  setPenColor(blue)
  setPenThickness(1)
  jumpToPos(cake1pos)
  slicePieces(cakeWidth, cakeHeight, n, m)
  jumpToPos(cake2pos)
  slicePieces(cakeWidth, cakeHeight, m, n)

  // Write equation
  jumpToPos(writepos)
  setHeading(90)
  val s1 = "1/"+n.toString
  val s2 = "1/"+m.toString
  val s3 = (n+m).toString + "/" + (n*m).toString
  val s4 = s1 + " + " + s2 + " = " + s3
  write(s4)

}

// Example call
showFractionAdd(2,5)