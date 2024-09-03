import turtle
from random import randint

#oyun ekranını ayarlıyoruz
turtle.tracer(0) #turtle.tracer(0) kodu turtle objesinin hareketlerini bize göstermez, direkt olarak son aksiyonu gösterir, bu sayede yükleme kısmından kurtuluyoruz
ws1 = turtle.Screen()
ws1.bgcolor("#7fd7ed")
ws1.title("Catch the Bean: A Turtle Game")
ws1.setup(450,450)

#oyun başlangıç ayarları
score = 0
boundary = 215
gameOverValue = False

#ana karakterimizi oluşturuyoruz
goForward = 1.5
speedyTurtle = turtle.Turtle()
speedyTurtle.penup()
speedyTurtle.speed(0.5)
speedyTurtle.shapesize(1.2)
speedyTurtle.shape("turtle")
speedyTurtle.color("#927d52")

ws1.listen()
ws1.onkeypress(lambda: speedyTurtle.left(90), "Left")
ws1.onkeypress(lambda: speedyTurtle.right(90), "Right")

#toplayacağımız şeyi oluşturuyoruz
bean = turtle.Turtle()
bean.penup()
bean.shape("circle")
bean.speed(0)
bean.color("#548817")
bean.shapesize(0.5)
beanX = randint(-200, 200)
beanY = randint(-200, 200)
bean.setposition(beanX, beanY)

#scoreboard oluşturuyoruz
ourScore = turtle.Turtle()
ourScore.hideturtle()
ourScore.penup()
ourScore.color("#61CCE1")
ourScore.setposition(0,-180)
ourScore.write(f"{score}", align="center",font=("Arial",250,"bold"))
turtle.tracer(1)

def playGame():
    global speedyTurtle, goForward, ws, gameOverValue
    if gameOverValue == False:
        screenConrtol()
        collectTheBean()
        speedyTurtle.forward(goForward)
        ws1.ontimer(playGame, 1)  #her 1ms'de bir turtle'ı hareket ettir
    else:
        gameOver()

def collectTheBean():
    global score, goForward
    if speedyTurtle.distance(bean) < 20:
        newBean()
        goForward = goForward + 0.3
        score += 1
        scoreControl()

def newBean():
    global bean
    turtle.tracer(0)
    bean.clear()
    beanX = randint(-200, 200)
    beanY = randint(-200, 200)
    bean.setposition(beanX, beanY)
    turtle.tracer(1)

def scoreControl():
    global ourScore, score
    turtle.tracer(0)
    ourScore.clear()
    ourScore.setposition(0, -180)
    ourScore.write(f"{score}", align="center",font=("Arial",250,"bold"))
    turtle.tracer(1)

def screenConrtol():
    global speedyTurtle, boundary
    if abs(speedyTurtle.xcor()) > boundary or abs(speedyTurtle.ycor()) > boundary:
        gameOver()

def gameOver():
    global gameOverValue
    gameOverValue = True
    turtle.tracer(0)
    ourScore.clear()
    speedyTurtle.clear()
    speedyTurtle.hideturtle()
    bean.hideturtle()
    gameOverTurtle = turtle.Turtle()
    gameOverTurtle.hideturtle()
    gameOverTurtle.penup()
    gameOverTurtle.color("blue")
    gameOverTurtle.write("Game Over!", align="center", font=("Arial", 32, "bold"))
    ourScore.color("blue")
    ourScore.setposition(0,-30)
    ourScore.write(f"Score: {score}", align="center", font=("Arial", 26, "bold"))
    turtle.tracer(1)

playGame()
ws1.mainloop()