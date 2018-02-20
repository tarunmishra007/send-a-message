import turtle
def draw_square(obj):
    for i in range(4):
        obj.forward(100)
        obj.right(90)
def draw_shapes():
    turtle.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(36):
        draw_square(brad)
        brad.right(10)
   # tarun=turtle.Turtle()
    #tarun.shape("arrow")
    #tarun.color("blue")
    #tarun.circle(100)
    turtle.exitonclick()
draw_shapes()
