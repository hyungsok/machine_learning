# coding: euc-kr
import turtle

x1 = int(input("ū ���� �߽���ǥ x1: "))
y1 = int(input("ū ���� �߽���ǥ y1: "))
r1 = int(input("ū ���� ������: "))
x2 = int(input("���� ���� �߽���ǥ x2: "))
y2 = int(input("���� ���� �߽���ǥ y2: "))
r2 = int(input("���� ���� ������: "))

t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(x1, y1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(x2, y2)
t.pendown()
t.circle(r2)

dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
if dist <= r1 - r2:
    turtle.write("�ι�° ���� ù��° ���� ���ο� �ֽ��ϴ�.")
elif dist <= r1 + r2:
    turtle.write("�ι�° ���� ù��° ���� ��Ĩ�ϴ�.")
else:
    turtle.write("�ι�° ���� ù��° ���� ��ġ�� �ʽ��ϴ�.")
