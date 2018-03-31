# coding: euc-kr
import turtle  # 터틀 그래픽 모듈을 불러온다.
import random  # 난수 모듈을 불러온다.

screen = turtle.Screen()
image1 = "gif/rabbit.GIF"
image2 = "gif/turtle.GIF"
screen.addshape(image1)
screen.addshape(image2)

# 토끼
t1 = turtle.Turtle()
t1.shape(image1)
t1.pensize(5)  # 팬의 두께를 5로 한다.
t1.penup()  # 펜을 든다.
t1.goto(-300, 0)  # (-300, 0) 위치로 간다.

# 거북이
t2 = turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.penup()
t2.goto(-300, -200)  # (-300, -100) 위치로 간다.

# 그림이 그려짐
t1.pendown()
t2.pendown()

# https://docs.python.org/2/library/turtle.html#turtle.speed
t1.speed(10)
t2.speed(1)

for i in range(10):  # 10번 반복한다.
    d1 = random.randint(1, 60)  # 1부터 60 사이의 난수를 .
    t1.forward(d1)  # 난수만큼 .
    d2 = random.randint(1, 60)  # 1부터 60 사이의 난수를 .
    t2.forward(d2)
