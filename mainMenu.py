import turtle
import subprocess
import time

ws = turtle.Screen()
ws.bgcolor("#EFEFEF")
ws.title("Two Turtle Games")
ws.setup(450,450)

gameSelect = turtle.Turtle()
gameSelect.hideturtle()
gameSelect.penup()
gameSelect.setposition(0,35)
gameSelect.color("#747474")
gameSelect.write("Oynamak için butonlardan birine tıklayınız.",align="center",font=("Arial",14,"bold"))

#birinci oyun butonu
button1 = turtle.Turtle()
button1.shape("square")
button1.shapesize(stretch_wid=2, stretch_len=6)
button1.color("#7fd7ed")
button1.penup()
button1.goto(-100, 0)
button1.write("1. OYUN",align="center",font=("Arial",14,"bold"))
button1.goto(-100, -20)

#ikinci oyun butonu
button2 = turtle.Turtle()
button2.shape("square")
button2.shapesize(stretch_wid=2, stretch_len=6)
button2.color("#E3BDBD")
button2.penup()
button2.goto(100, 0)
button2.write("2. OYUN",align="center",font=("Arial",14,"bold"))
button2.goto(100, -20)

def readyGame():
    turtle.tracer(0)
    gameSelect.clear()
    button1.clear()
    button2.clear()
    button1.hideturtle()
    button2.hideturtle()
    ready = turtle.Turtle()
    ready.hideturtle()
    ready.penup()
    ready.write("Oyununuz açılıyor... Hazırlıklı olun.", align="center", font=("Arial", 14, "bold"))
    turtle.tracer(1)
    time.sleep(1.5)
    ws.bye()

def startFirstGame(x,y):
    if button1.distance(x, y) < 30:  # eğer tıklama turtle'ın yakınındaysa
        readyGame()
        subprocess.run(["python", "firstGame.py"])
    else:
        pass

def startSecondGame(x,y):
    if button2.distance(x, y) < 30:  # eğer tıklama turtle'ın yakınındaysa
        readyGame()
        subprocess.run(["python", "secondGame.py"])
    else:
        pass

ws.listen()
button1.onclick(startFirstGame)  # collect nesnesinin üstüne dokunulduğunda on_click fonksiyonunu çağırıyoruz
button2.onclick(startSecondGame)
ws.mainloop()