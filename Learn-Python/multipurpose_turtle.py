import turtle

turtle = turtle.Turtle()


# Square Turtle
def square_turtle(length, direction, color):
  turtle.pencolor(color)
  turtle.forward(length)
  turtle.left(direction)
  turtle.forward(length)
  turtle.left(direction)
  turtle.forward(length)
  turtle.left(direction)
  turtle.forward(length)

# Star Turtle
def star_turtle(length, direction, color):
  for i in range(5):
      turtle.pencolor(color)
      turtle.forward(length)
      turtle.right(direction) #144 is default star.


# Color Array
colors = ("#1FDE3D", "#DE1F9F", "#1F2FDE", "#DE851F", "#9D0F17")

# Direction Array
directions = (77, 144, 288)

# Length Array
lengths = (50, 100, 150)

# Give the Turtle some coffee
turtle.speed(200)


# Get to work Turtle - Main
# Increase sugar <= to further the design.
def main():
  sugar = int()
  while sugar <= 100:
    sugar += 1 # Feed another cube of sugar.
    for c in colors:
      for l in lengths:
        for d in directions:
          star_turtle(l, d, c)
          turtle.setposition(0,0)
          square_turtle(l, d, c)
          sugar += 1 # Feed another cube of sugar.
          print(sugar) # Print how many sugars turtle has eaten to console.
          if sugar == 100: # Exit function at 100 sugars.
            return


main()
turtle.done()
