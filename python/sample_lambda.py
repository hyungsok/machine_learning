# 파이썬 코딩 도장 : https://dojang.io/mod/page/view.php?id=1060

# lambda 매개변수1, 매개변수2: 식1 if 조건식 else 식2
f0 = lambda x: str(x) if x % 3 == 0 else x
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = list(map(f0, a))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
print(data)


f1 = lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10
data = list(map(f1, a))
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
print(data)


def f3(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
data = list(map(f3, a))
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
print(data)