import turtle

def draw_square(some_tuttle):
  for i in range (1,5):
      some_tuttle.forward(100)
      some_tuttle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #create the turtle brand - Draw a sqaure
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    #create the turtle Angie - Draws a circle
    
    #angie = turtle.Turtle()
    #brad.shape("arrow")
    #brad.color("blue")
    #brad.circle(100)

    window.exitonclick()

draw_art()
