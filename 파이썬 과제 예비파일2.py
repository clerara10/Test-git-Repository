class Car:
    speed=0
    def upSpeed(self, value):
        self.speed+=value

        print("현재 속도(슈퍼 클래스): %d" %self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed+=value

        if self.speed>150:
            self.speed=150
        print("현재 속도(서브 클래스):%d" %self.speed)

class Sonata(Sedan):
    pass


class Truck(Car):
    pass

sonata1, sedan1, truck1=None, None, None

sonata1=Sonata()
truck1=Truck()
sedan1=Sedan()

print("소나타->", end="")
sonata1.upSpeed(150)

print("트럭->", end="")
truck1.upSpeed(200)

print("승용차->", end="")
sedan1.upSpeed(200)