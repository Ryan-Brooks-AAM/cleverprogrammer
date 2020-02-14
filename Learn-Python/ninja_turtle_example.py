import turtle

ninja = turtle.Turtle()

ninja.speed(200)

def ninja_turtle():
    
    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)

        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()

        ninja.right(2)

colors = ['red', 'blue', 'orange']

for c in colors:
    ninja.color(c)
    ninja_turtle()



turtle.done()
