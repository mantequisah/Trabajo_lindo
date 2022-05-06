import turtle
import time 
import random



delay = 0.1



wn = turtle.Screen()
# Le agregamos un titulo
wn.title("Juego")
# Tamaño de la ventana
wn.setup(width=640, height=340)
# Agregamos un color
wn.bgpic('mar.gif')


# Representamiento

# Objeto turtle
head = turtle.Turtle()
# Para que se quede fijo:
head.speed(0)
# Forma 
head.shape("turtle")
# Color del objeto
head.color("black")
# Para no dejar rastro de la animación
head.penup()
# Para hacer que el programa espere a que se le de otra dir
head.direction = "center"

# Variable comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#4A1C6B")
food.penup()
food.direction = "down"




def mov():
    if head.direction == "up":
        # Almacenar el valor actual de la coordenada Y:
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        # Almacenar el valor actual de la coordenada Y:
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "right":
        # Almacenar el valor actual de la coordenada Y:
        y = head.xcor()
        head.setx(y + 10)

    if head.direction == "left":
        # Almacenar el valor actual de la coordenada Y:
        y = head.xcor()
        head.setx(y - 10)

def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"


# Reconocimiento de teclado:
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(dirLeft, "Left")
while True:
    wn.update()

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
    
        


    mov()
    time.sleep(delay)