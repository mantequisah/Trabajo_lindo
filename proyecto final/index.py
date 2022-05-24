import turtle
import time
import random

delay = 0.1
score= 0
high_score =0


ventana = turtle.Screen()
ventana.title("juego")
ventana.bgcolor("white")
ventana.setup(width=600, height=600)
ventana.tracer(0)
ventana.bgpic('fondo.png')

# la wuea que se mueve
ser=turtle.Turtle()
ser.direccion = "stop"

# obtaculos
obstaculo1 = turtle.Turtle()
obstaculo2 = turtle.Turtle()
obstaculo3 = turtle.Turtle()
obstaculo4 = turtle.Turtle()
obstaculo5 = turtle.Turtle()
obstaculo6 = turtle.Turtle()
obstaculo7 = turtle.Turtle()
obstaculo8 = turtle.Turtle()
obstaculo9 = turtle.Turtle()


# comida

comida = turtle.Turtle()

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
    x = random.randint(-230-20, 230+20)
    y = random.randint(-230-20, 230+20)
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

def obstaculosrandom1 (ser, obstaculo1):
  obstaculo1.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo1.penup()
  obstaculo1.goto (x , y)

def obstaculosrandom2 (ser, obstaculo2):
  obstaculo2.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo2.penup()
  obstaculo2.goto (x , y)

def obstaculosrandom3 (ser, obstaculo3):
  obstaculo3.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo3.penup()
  obstaculo3.goto (x , y)

def obstaculosrandom4 (ser, obstaculo4):
  obstaculo4.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo4.penup()
  obstaculo4.goto (x , y)

def obstaculosrandom5 (ser, obstaculo5):
  obstaculo5.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo5.penup()
  obstaculo5.goto (x , y)

def obstaculosrandom6 (ser, obstaculo6):
  obstaculo6.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo6.penup()
  obstaculo6.goto (x , y)
def obstaculosrandom7 (ser, obstaculo7):
  obstaculo7.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo7.penup()
  obstaculo7.goto (x , y)
def obstaculosrandom8 (ser, obstaculo8):
  obstaculo8.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo8.penup()
  obstaculo8.goto (x , y)
def obstaculosrandom9 (ser, obstaculo9):
  obstaculo9.penup()
  x= random.randint(-230-20, 230+20)
  y = random.randint(-230-20, 230+20)
  obstaculo9.penup()
  obstaculo9.goto (x , y)


def colicionobstaculos (ser , obstaculo1 , obstaculo2 , obstaculo3 ,obstaculo4 , obstaculo5 , obstaculo6 , obstaculo7 , obstaculo8 , obstaculo9 ) :
  if (ser.distance(obstaculo1)<  20 or ser.distance(obstaculo2)< 20 or ser.distance(obstaculo3)<20 or ser.distance(obstaculo4)<20 or ser.distance(obstaculo5)< 20 or ser.distance(obstaculo6)<20 or ser.distance(obstaculo7)<20 or ser.distance(obstaculo8)<20 or ser.distance(obstaculo9)<20 ):
        obstaculosrandom1 (ser, obstaculo1)
        obstaculosrandom2 (ser, obstaculo2)
        obstaculosrandom3 (ser, obstaculo3)
        obstaculosrandom4 (ser, obstaculo4)
        obstaculosrandom5 (ser, obstaculo5)
        obstaculosrandom6 (ser, obstaculo6)
        obstaculosrandom7 (ser, obstaculo7)
        obstaculosrandom8 (ser, obstaculo8)
        obstaculosrandom9 (ser, obstaculo9)
        

        time.sleep(1)
        ser.reset()
        ser.direccion = "stop" 
        obstaculosrandom1 (ser, obstaculo1)
        obstaculosrandom2 (ser, obstaculo2)
        obstaculosrandom3 (ser, obstaculo3)
        obstaculosrandom4 (ser, obstaculo4)
        obstaculosrandom5 (ser, obstaculo5)
        obstaculosrandom6 (ser, obstaculo6)
        obstaculosrandom7 (ser, obstaculo7)
        obstaculosrandom8 (ser, obstaculo8)
        obstaculosrandom9 (ser, obstaculo9)
     
    
                  
titulo.goto(0 , 220)
titulo.write("Juego de la tortuga", align = "center", font = ("arial", 32 , "normal") )        
titulo.goto(0 , 160)
titulo.write ("Alimenta a la tortuga para que crezca", align = "center" , font = ("arial", 16 , "normal"))


time.sleep(3)
ventana.update()
titulo.clear()
texto.goto(0, 260)
comidarandom(comida)    
while True:
    
    ventana.update ();
    dibujo(ser , "turtle", "green", 1.5, 1.5)
    dibujo(comida,"circle", "red", 1.5, 1.5 )
    ventana.update ();
    dibujo(ser , "turtle", "green", 1.5, 1.5)
    dibujo(comida,"circle", "red", 1.5, 1.5 )
    dibujo(obstaculo1,"square", "black", 1 , 1 )
    dibujo(obstaculo2 ,"square", "black", 1 , 1)
    dibujo(obstaculo3,"square", "black", 1 , 1)
    dibujo(obstaculo4, "square", "black", 1 , 1)
    dibujo(obstaculo5 , "square", "black", 1 , 1)
    dibujo(obstaculo6 , "square", "black", 1 , 1) 
    dibujo(obstaculo7 , "square", "black", 1 , 1) 
    dibujo(obstaculo8 , "square", "black", 1 , 1) 
    dibujo(obstaculo9 , "square", "black", 1 , 1) 
      
    
    if colicionbordes(ser, comida) == 0 or colicioncuerpo(ser,comida) == 0 or colicionobstaculos(ser , obstaculo1 , obstaculo2 , obstaculo3 ,obstaculo4 , obstaculo5 , obstaculo6,obstaculo7,obstaculo8,obstaculo9) == 0 :
        if score > high_score :
            high_score = score
        score=0 
    if comer(ser, comida) == 10:
        score+= 10;
        
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