import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Shivam = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    Shivam.shape('turtle')
    # Set your turtle's speed using .speed(2)
    Shivam.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Shivam.color('green')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    Shivam.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    Shivam.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square
    for i in range(1,4):
        Shivam.forward(100)
        Shivam.right(90)

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Shivam.goto(150 ,150)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Shivam.begin_fill()
    Shivam.circle(50, 130)
    Shivam.end_fill()

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    Shivam.penup()
    Shivam.forward(50)
    Shivam.begin_fill()
    Shivam.pendown()
    Shivam.right(60)
    Shivam.forward(50)
    Shivam.right(60)
    Shivam.forward(50)
    Shivam.right(60)
    Shivam.forward(50)
    Shivam.right(60)
    Shivam.forward(50)
    Shivam.right(60)
    Shivam.forward(50)
    Shivam.right(60)
    Shivam.forward(50)
    Shivam.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
