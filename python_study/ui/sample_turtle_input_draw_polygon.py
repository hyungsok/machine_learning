# coding: euc-kr
import turtle

t = turtle.Turtle()
t.shape("turtle")

angle = int(turtle.textinput("?", "���ڸ� �Է��Ͻÿ�: "))
for i in range(angle):
    t.forward(100)
    t.left(360 / angle)

for i in range(angle):
    t.circle(100)
    t.left(360 / angle)
