class Person:

    def __init__(self, _name, _no):
        self.name = _name
        self.no = _no

    def display(self):
        print(">> 입력하신 결과입니다. ")
        print("이름 : ", self.name)
        print("전화번호 : " + self.no)

print("================================")
print("= 예제 =")
p1 = Person("홍길동1", "222-221")
p2 = Person("홍길동2", "222-222")
p3 = Person("홍길동3", "222-223")
persons = []
persons.append(p1)
persons.append(p2)
persons.append(p3)

for person in persons:
    print(person.name, person.no)
print("================================")

