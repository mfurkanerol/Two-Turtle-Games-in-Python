import turtle
from random import randint
import time

#oyun ekranını ayarlıyoruz
turtle.tracer(0) #turtle.tracer(0) kodu turtle objesinin hareketlerini bize göstermez, direkt olarak son aksiyonu gösterir, bu sayede yükleme kısmından kurtuluyoruz
ws2 = turtle.Screen()
ws2.bgcolor("#E3BDBD")
ws2.title("Catch The Hatched Turtle")
ws2.setup(450,450)

#Oyun başlangıç bayrağı
score = 0
game_duration = 18  #Oyun süremiz (saniye)
start_time = None #Hiçbir değer atamıyoruz çünkü bunu fonksiyon içinde değiştireceğiz
remaining_time = None #Hiçbir değer atamıyoruz çünkü bunu fonksiyon içinde değiştireceğiz

#oyun süresini gösteren yazıyı oluşturuyoruz
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()

#score yazısını gösteren yazıyı oluşturuyoruz
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("#DDA5A5")
score_display.setposition(0,-180)
score_display.write(f"{score}", align="center",font=("Arial",250,"bold"))

#toplayacağımız turtle'ın özelliklerini ayarlıyoruz
collect = turtle.Turtle()
collect.hideturtle() #oyunun başlangıcında collect nesnesini saklıyoruz
collect.shapesize(1.8)
collect.color("red")
collect.shape("turtle")
collect.speed(0)
collect.penup()
turtle.tracer(1)

def start_game():
    global start_time
    start_time = time.time()  #başlangıç zamanını kaydediyoruz
    move_turtle()  #turtle'ı rastgele bir yere taşıyoruz
    ws2.ontimer(move_turtle_periodically, 900)  #her 900 milisaniyede move_turtle_periodically fonksiyonunu çağırıyor
    update_timer()  #zaman göstergesini güncellemeye başlar

#turtle'ı hareket ettirme fonksiyonumuz: turtle'ı rastgele bir konuma taşıyor ve görünür yapıyor
def move_turtle():
    collectX = randint(-200, 200)
    collectY = randint(-200, 200)
    collect.setposition(collectX, collectY)
    collect.showturtle()

#mouse tıklamasını ve skorun artmasını işleyen fonksiyon
def on_click(x, y):
    global score
    if collect.distance(x, y) < 30:  #eğer tıklama turtle'ın yakınındaysa
        turtle.tracer(0)
        score += 1  #skoru arttırıyoruz
        score_display.clear()  #skor göstergesini önce temizliyoruz ki yazılar üst üste binmesin
        score_display.setposition(0, -180)
        score_display.write(f"{score}", align="center", font=("Arial", 250, "bold"))
        turtle.tracer(1)

#900 milisaniyede bir turtle'ı rastgele bir yere taşıyan ve oyun süresini kontrol eden fonksiyon
def move_turtle_periodically():
    if time.time() - start_time < game_duration:
        move_turtle()  #turtle'ı hareket ettir
        ws2.ontimer(move_turtle_periodically, 600)  #600 milisaniye sonra tekrar çağır
    else:
        end_game()  #oyun süresi dolduğunda bitir

#kalan süreyi güncelleyerek gösteren fonksiyon
def update_timer():
    remaining_time = game_duration - int(time.time() - start_time)
    turtle.tracer(0)
    if remaining_time >= 0:
        time_display.clear()
        time_display.setposition(0, 180)
        time_display.write(f"Time: {remaining_time}", align="center", font=("Arial", 20, "normal"))
        ws2.ontimer(update_timer, 1000)  #her saniye kalan süreyi güncelle
    else:
        end_game()  #zaman dolduysa oyunu bitir
    turtle.tracer(1)

#oyunu sonlandırır ve skoru gösterir
def end_game():
    turtle.tracer(0)
    collect.hideturtle()  #turtle'ı gizle
    score_display.clear()  #skor göstergesini temizle
    time_display.clear() #zaman göstergesini temizle
    time_display.color("red")
    time_display.setposition(0, 10)  #zamanı yeniden göster, ama bu sefer ekranın ortasında
    time_display.write("Oyun Bitti!", align="center", font=("Arial", 32, "bold"))
    score_display.color("red")
    score_display.setposition(0, -30)  #skoru yeniden göster, ama bu sefer ekranın ortasında
    score_display.write(f"Score: {score}", align="center", font=("Arial", 26, "bold"))
    turtle.tracer(1)

ws2.listen()
start_game()
collect.onclick(on_click) #collect nesnesinin üstüne dokunulduğunda on_click fonksiyonunu çağırıyoruz
ws2.mainloop()
