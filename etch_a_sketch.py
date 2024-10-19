from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    """ Move arrow forward by 10 steps. """
    turtle.forward(10)


def move_backward():
    """ Move arrow backward by 10 steps. """
    turtle.backward(10)


def turn_clockwise():
    """ Rotate arrow clockwise by 10 degrees. """
    turtle.right(10)


def turn_counterclockwise():
    """ Rotate arrow anti-clockwise by 10 degrees. """
    turtle.left(10)


def clear():
    """ Clear the screen. """
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


def main():
    """ Main method to implement Etch-A-Sketch Functionality. It uses event listener,
    to move and rotate arrow, and also to clear the screen. """
    screen.listen()
    print("Keys:")
    print("Press w to move forward.")
    print("Press s to move backward.")
    print("Press a to rotate clockwise.")
    print("Press d to rotate counterclockwise.")
    print("Press c to clear the screen.")
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=turn_clockwise)
    screen.onkey(key="d", fun=turn_counterclockwise)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()


if __name__ == "__main__":
    main()
