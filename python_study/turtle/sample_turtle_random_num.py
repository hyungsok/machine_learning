# coding: euc-kr
import turtle  # ��Ʋ �׷��� ����� �ҷ��´�.
import random  # ���� ����� �ҷ��´�.

screen = turtle.Screen()
image1 = "gif/rabbit.GIF"
image2 = "gif/turtle.GIF"
screen.addshape(image1)
screen.addshape(image2)

# �䳢
t1 = turtle.Turtle()
t1.shape(image1)
t1.pensize(5)  # ���� �β��� 5�� �Ѵ�.
t1.penup()  # ���� ���.
t1.goto(-300, 0)  # (-300, 0) ��ġ�� ����.

# �ź���
t2 = turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.penup()
t2.goto(-300, -200)  # (-300, -100) ��ġ�� ����.

# �׸��� �׷���
t1.pendown()
t2.pendown()

# https://docs.python.org/2/library/turtle.html#turtle.speed
t1.speed(10)
t2.speed(1)

for i in range(10):  # 10�� �ݺ��Ѵ�.
    d1 = random.randint(1, 60)  # 1���� 60 ������ ������ .
    t1.forward(d1)  # ������ŭ .
    d2 = random.randint(1, 60)  # 1���� 60 ������ ������ .
    t2.forward(d2)
