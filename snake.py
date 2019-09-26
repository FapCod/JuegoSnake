import turtle
import time
import random

posponer = 0.1

#Configuracion de pantalla
wn = turtle.Screen() #crear la ventana
wn.title("Juego Snake") #poner titulo
wn.bgcolor("black") #poner color de fondo
wn.setup(width=600, height=600) #redimencionar la ventana
wn.tracer(0) #hace las animaciones mas placenteras

#Cabeza de serpiente
cabeza = turtle.Turtle() #se crea objeto turtle
cabeza.speed(0) #cuando se inicie en la pantalla ya este el cuadrado ahi
cabeza.shape("square") #para que tenga forma de cuadrado
cabeza.color("white") #color de la cabeza blanco
cabeza.penup() #para que no deje rasto el comando turtle
cabeza.goto(0,0) #iniciar desde el centro
cabeza.direction = "stop" #el programa esperara la direccion

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
#cuerpo para la serpiente
segmentos = []

#funciones
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"



def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor() #almacenar la coordenada de la cabeza
        cabeza.sety(y+20) #cada vez que mueve aumenta 20px

    if cabeza.direction == "down":
        y = cabeza.ycor() #almacenar la coordenada de la cabeza
        cabeza.sety(y-20) #cada vez que mueve disminuye 20px

    if cabeza.direction == "left":
        x = cabeza.xcor() #almacenar la coordenada de la cabeza
        cabeza.setx(x-20) #cada vez que mueve dismunuye 20px

    if cabeza.direction == "right":
        x = cabeza.xcor() #almacenar la coordenada de la cabeza
        cabeza.setx(x+20) #cada vez que mueve aumenta 20px
#teclado
wn.listen()#para queeste atenta a los eventos del teclado
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
#para que la interfaz  se quede estatica
while True:
    wn.update() #se actualiza el programa
    #colisiones de bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #Esconder elementos de la cola
        for segmento in segmentos:
            segmento.goto(2000,2000)

        #limpiar lista de segmentos
        segmentos.clear()


    #colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle() #se crea objeto turtle
        nuevo_segmento.speed(0) #cuando se inicie en la pantalla ya este el cuadrado ahi
        nuevo_segmento.shape("square") #para que tenga forma de cuadrado
        nuevo_segmento.color("grey") #color de la cabeza blanco
        nuevo_segmento.penup() #para que no deje rasto el comando turtle
        segmentos.append(nuevo_segmento)

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos) #tamaño
    for index in range(totalSeg -1,0,-1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg>0:
        x= cabeza.xcor()
        y= cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #colisiones con el cuerpo
    for segmento in segmentos:
         if segmento.distance(cabeza) < 20:
             time.sleep(1)
             cabeza.goto(0,0)
             cabeza.direction = "stop"

            #Escondersegmentos
             for segmento in segmentos:
                 segmento.goto(1000,1000)

             segmentos.clear()

    time.sleep(posponer)
