import turtle
import time
import random

META=30

ventana = turtle.Screen()
ventana.title("Carrera de caracoles")
ventana.bgcolor("lightblue")
ventana.setup(width=800,height=600)

caracol1 = turtle.Turtle()
caracol1.color("red")
caracol1.shape("turtle")
caracol1.penup()
caracol1.goto(-300,50)

caracol2 = turtle.Turtle()
caracol2.color("blue")
caracol2.shape("turtle")
caracol2.penup()
caracol2.goto(-300,0)

time.sleep(0.5)

while True:
  a1 = random.randint(1,20)
  a2 = random.randint(1,20)

  caracol1.forward(a1)
  caracol2.forward(a2)

  if caracol1.xcor() >= META or caracol2.xcor() >= META:
    break

ventana.exitonclick()