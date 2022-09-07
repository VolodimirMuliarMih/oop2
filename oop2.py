#OOP1
class Auto():
    brand = None
    age = None
    color = "Red"
    mark = True
    weigt = True
    def __init__ (self, age, mark, brand):
        self.age = age
        self.mark = mark
        self.brand = brand
    def move(self):
        print('move')
    def birthday(self):
        self.age=self.age+1
    def stop(self):
        print('stop')
class Truck(Auto):
    max_load = None
    def __init__(self, age, mark, brand, max_load):
        super().__init__(age, mark, brand)
        self.max_load = max_load
    def move(self):
        print("Attention")
        super().move()
    def load(self):
        import time
        time.sleep(1)
        print('Load')
        time.sleep(1)
class Car(Auto):
    max_speed = True
    def __init__(self, age, mark, brand, max_speed):
        super().__init__(age, mark, brand)
        self.max_speed = max_speed
    def move(self):
        super().move()
        print(f'Max Speed is {self.max_speed}')
Truck_1 = Truck(10, '600', 'mercedes',200)
print(Truck_1.brand)
print(Truck_1.max_load)
print(Truck_1.age)
print(Truck_1.color)
Truck_1.load()
Truck_1.move()
Car_1=Car(10, '600', 'mercedes',300)
print(Car_1.max_speed)
print(Car_1.brand)
print(Car_1.age)
Car_1.move()