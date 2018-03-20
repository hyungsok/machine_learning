import turtle

def draw_square(w, h):
    print("\t>> draw_square : %d, %d" %(w, h))
    t = turtle.Turtle()
    t.shape("turtle")
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)

s = turtle.textinput("?", "도형을 입력하시오: ")
print("도형 : %s" %(s))
if s == "사각형":
    w = int(turtle.textinput("!", "가로: "))
    h = int(turtle.textinput("!", "세로: "))
    draw_square(w, h)
