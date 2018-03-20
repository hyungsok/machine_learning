# coding: utf-8
score = int(input("총점을 입력하시오: "))

if score >= 90:
    print("수")
elif 80 <= score < 90:
    print("우")
elif 70 <= score < 80:
    print("미")
elif 60 <= score < 70:
    print("양")
else:
    print("가")
