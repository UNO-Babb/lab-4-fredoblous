#TurtleGraphics.py
#Name: Joshua
#Date: 9/18/24
#Assignment: Lab 4

hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(turtle, size, number_of_sides):
    exterior_angle = 360 / number_of_sides
    for i in range(number_of_sides):
        turtle.forward(size)
        turtle.right(exterior_angle)

def fillCorner(turtle, size, corner):
    drawSquare(turtle, size)
    
    if corner == "top_right":
        turtle.forward(size/2)
        turtle.begin_fill()
        drawSquare(turtle, size/2)
        turtle.end_fill()
    
    if corner == "bottom_left":
        turtle.right(90)
        turtle.forward(size/2)
        turtle.left(90)
        turtle.begin_fill()
        drawSquare(turtle, size/2)
        turtle.end_fill()
        
def squaresInSquares(turtle, number):
    for i in range(number):
        if i == 0:
            size = 50
            drawSquare(turtle, size)
            size += 20
        else:
            drawSquare(turtle, size)
            turtle.right(90)
            size *= .5
        
        
    

def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 50, 5)
    
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle, 80, 8)

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 50, "top_right")
    
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    # fillCorner(myTurtle, 50, "bottom_left")

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 5)
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
