import turtle

painter = turtle.Turtle()

def large_blue_spiral():
    painter.pencolor("blue")
    for i in range(50):
        painter.forward(500)
        painter.left(123)

def small_red_spiral():
    painter.pencolor("red")
    for i in range(50):
        painter.forward(50)
        painter.left(123)

def reorient_turtle_right():
    painter.right(123)
    painter.forward(100)

def reorient_turtle_left():
    painter.left(237)
    painter.forward(100)

def end_turtle():
    turtle.done()

def pickup_pen():
    painter.penup()
 
def putdown_pen():
    painter.pendown()

def main():

    for i in range(30):
        painter.speed(100)
        putdown_pen()
        large_blue_spiral()
        pickup_pen()
        reorient_turtle_left()
        putdown_pen()
        small_red_spiral()
        pickup_pen()
        reorient_turtle_left()
    
main()
end_turtle()

