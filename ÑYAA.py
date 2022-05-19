import turtle
import time
import random

delay = 0.1
score= 0
high_score =0


ventana= turtle.Screen()
ventana.title("jueguito")
ventana.bgcolor("white")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# la wuea que se mueve
ser=turtle.Turtle()
ser.direccion = "stop"

# comida

comida = turtle.Turtle()

# obstaculos 
obstaculos = turtle.Turtle()

# titulo

titulo =turtle.Turtle()
titulo.penup()
titulo.hideturtle()

texto = turtle.Turtle()
texto.penup()
texto.hideturtle()

cola = []

def dibujo (cuerpo , forma , color , h , w) :
    cuerpo.speed(0)
    cuerpo.shape(forma) 
    cuerpo.color(color)
    cuerpo.shapesize(h , w)
    cuerpo.penup()

def mover():
    if (ser.direccion  == "up"):
        y = ser.ycor() #10
        ser.sety(y+20) #y=10+10
        
    if (ser.direccion  == "left"):
        x = ser.xcor() #10
        ser.setx (x-20) #y=10+10
            
    if (ser.direccion  == "down"):
        y = ser.ycor() #10
        ser.sety(y-20) #y=10+10
    
    if (ser.direccion  == "right"):
        x = ser.xcor() #10
        ser.setx(x+20) #y=10+10
        
def ar ():
    ser.direccion ="up"
    ser.setheading (90)
def iz ():
    ser.direccion = "left"
    ser.setheading (180)
def ab ():
    ser.direccion = "down"
    ser.setheading (270)
def de ():
    ser.direccion = "right"
    ser.setheading (0)

def comidarandom (comida) :
    comida.penup()
    x = random.randint(-260-20, 260+20)
    y = random.randint(-260-20, 260+20)
    comida.goto (x , y)
def comer (ser,comida):
    if (ser.distance(comida)<  20):
        comidarandom(comida)
        cuerpo = turtle.Turtle()
        dibujo(cuerpo,"turtle","blue", 0.5 , 0.5)
        cola.append(cuerpo)
        return 10

def movercuerpo (ser):
    total= len(cola)
    for i in range (total-1, 0,-1):
        x=cola[i-1].xcor()
        y=cola[i-1].ycor()
        cola[i].goto(x , y)
    if total > 0:
        x=ser.xcor()
        y=ser.ycor()
        cola[0].goto(x , y)
    
def colicionbordes(ser, comida) :
    if(ser.xcor() > 290 or ser.xcor() < -290 or ser.ycor() > 290 or ser.ycor() < -290 ):
        time.sleep(1)
        ser.reset()
        ser.direccion = "stop" 
        for i in cola :
            i.hideturtle()
        cola.clear()
        comidarandom(comida)

def colicioncuerpo (ser,comida) :
    for i in cola:
        if i.distance(ser) < 10 :
            time.sleep(1)
            ser.reset()
            ser.direccion = "stop" 
            for i in cola :
                i.hideturtle()
            cola.clear()
            comidarandom(comida)
            return 0

def marcador (texto, scores, high_score):
    texto.clear()
    texto.write("score: {}   high score: {}".format(score, high_score), 
                align ="center", font = ("arial", 12, "normal "))


def colicionobstaculos (ser, obstaculos):
  obstaculos.penup()
  x= random.randint(-260-20, 260+20)
  y = random.randint(-260-20, 260+20)
  obstaculos.goto (x , y)
  
  
    
                  
titulo.goto(0 , 220)
titulo.write("jueguinho de la serpiente", align = "center", font = ("arial", 32 , "normal") )        
titulo.goto(0 , 160)
titulo.write ("comete las bolas para crecer", align = "center" , font = ("arial", 16 , "normal"))


time.sleep(3)
ventana.update()
titulo.clear()
texto.goto(0, 260)
comidarandom(comida)    
while True:
    
    ventana.update ();
    dibujo(ser , "turtle", "green", 1.5, 1.5)
    dibujo(comida,"circle", "red", 1.5, 1.5 )
    dibujo(obstaculos,"triangle", "black", 1.5 , 1.5 )  
    
    if colicionbordes(ser, comida) == 0 or colicioncuerpo(ser,comida) == 0 :
        if score > high_score :
            high_score = score
        score=0 
    if comer(ser, comida) == 10:
        score+= 10;
    if colicionobstaculos (ser, obstaculos) == 0:
      time.sleep(1)
      ser.reset()
      ser.direccion = "stop" 
      for i in cola :
          i.hideturtle()
      cola.clear()
    
      
        
    comer(ser,comida)
    movercuerpo(ser)
    marcador(texto, score, high_score)
    
    ventana.listen()
    ventana.onkeypress(ar , "Up")
    ventana.onkeypress(iz , "Left")
    ventana.onkeypress(ab , "Down")
    ventana.onkeypress(de , "Right")
    
    mover()

      
    time.sleep(delay)
    
