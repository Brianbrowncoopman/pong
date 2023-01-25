import turtle

#ventana
wn = turtle.Screen()
wn.title("Pong by BBC")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


#jugadar A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid = 5, stretch_len = 1)

#jugadar B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid = 5, stretch_len = 1)

#pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 3
pelota.dy = 3

#linea division
division = turtle.Turtle()
division.color("white")
division.goto(0, 400)
division.goto(0, -400)


#funciones
    #jugadorA
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)
    
    #jugadorB
def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")     #boton arriba jugadorA
wn.onkeypress(jugadorA_down, "z")   #boton abajo jugadorA
wn.onkeypress(jugadorB_up, "u")     #boton arriba jugadorB
wn.onkeypress(jugadorB_down, "n")   #boton abajo jugadorB


#motor del juego
while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #bordes
    if pelota.ycor() > 270:
        pelota.dy *= -1
    if pelota.xcor() < -270:
        pelota.dy *= -1

    #bordes deerecha/izquierda
    if pelota.xcor() > 380:
        pelota.goto(0, 0)
        pelota.dx *= -1
        
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
            and (pelota.ycor() < jugadorB.ycor() + 50
            and pelota.ycor() > jugadorB.ycor() - 50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350)
            and (pelota.ycor() < jugadorA.ycor() + 50
            and pelota.ycor() > jugadorA.ycor() - 50)):
        pelota.dx *= -1




        
  
