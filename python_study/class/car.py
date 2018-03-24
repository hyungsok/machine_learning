class Car:
    def __init__(self, speed=0, color="", model="", year=""):
        self.speed = speed
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        self.speed = 10

    def display(self):
        print(">> 자동차 정보입니다.")
        print("\t 속도 : ", self.speed)
        print("\t 컬러 : ", self.color)
        print("\t 모델 : ", self.model)
        print("\t 연식 : ", self.year)


print(">> 자동차 객체가 생성하였습니다. ------------")
myCar = Car()
myCar.speed = 0
myCar.color = "blue"
myCar.model = "Sonata"
myCar.year = "2017"
myCar.display()

print(">> 자동차가 주행합니다.")
myCar.drive()
print("\t 속도 : ", myCar.speed)

print(">> 자동차 객체가 생성하였습니다.------------")
yourCar = Car(30, "red", "E-class", "2018")
yourCar.display()

print(">> 자동차 객체가 생성하였습니다.------------")
monCar = Car(30, year="2022")
monCar.display()
