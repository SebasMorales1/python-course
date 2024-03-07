import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")

tortuga = turtle.Turtle()
# tortuga.color("red")
tortuga.speed(1)

for _ in range(5):
  tortuga.forward(200)
  tortuga.right(144)

ventana.exitonclick()