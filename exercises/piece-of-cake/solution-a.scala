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

// set constants
setAnimationDelay(0)
setHeading(0)
val cakeWidth = 300
val cakeHeight = 50
val cake1pos = (-50, 75)
val cake2pos = (-50, 0)

// Draw the two cakes
setPenThickness(3)
setPenColor(brown)
setFillColor(pink)
jumpToPos(cake1pos)
drawRect(cakeWidth,cakeHeight)
jumpToPos(cake2pos)
drawRect(cakeWidth, cakeHeight)

// Cut cakes in 3 and 4 pieces
setPenColor(red)
setPenThickness(5)
jumpToPos(cake1pos)
sliceRect(cakeWidth, cakeHeight, 3)
jumpToPos(cake2pos)
sliceRect(cakeWidth, cakeHeight, 4)

// Eat one piece from each cake
setPenColor(brown)
setFillColor(brown)
setPenThickness(1)
jumpToPos(cake1pos)
drawRect(cakeWidth/3, cakeHeight)
jumpToPos(cake2pos)
drawRect(cakeWidth/4, cakeHeight)

// Slice each piece in 4 and 3 slices
setPenColor(blue)
setPenThickness(1)
jumpToPos(cake1pos)
slicePieces(cakeWidth, cakeHeight, 3, 4)
jumpToPos(cake2pos)
slicePieces(cakeWidth, cakeHeight, 4, 3)