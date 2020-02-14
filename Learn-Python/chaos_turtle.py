import turtle

turtle = turtle.Turtle()


# square
def square_one(length, direction, color):
  turtle.pencolor(color)
  turtle.forward(length)
  turtle.left(direction)
  turtle.forward(length)
  turtle.left(direction)
  turtle.forward(length)
  turtle.left(direction)
  turtle.forward(length)
turtle.speed(100)
direction = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180]
length = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101, 102, 103, 104, 105]
color = ['orange', 'red', 'blue', 'green', 'yellow']
for i in range(500):
    for c in color:
      for l in length:
        for d in direction:
          square_one(l, d, c)
