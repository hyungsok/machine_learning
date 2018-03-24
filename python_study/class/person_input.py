class Person:

    def __init__(self):
        self.name = input("이름 : ")
        self.no = input("전화번호  : ")
        
    def display(self):
        print(">> 입력하신 결과입니다. ")
        print("이름 : ", self.name)
        print("전화번호 : " + self.no)

persons = []
for i in range(4):
    persons.append(Person())

for person in persons:
    person.display()

