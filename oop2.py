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
auto1= Auto(10, '600', 'mercedes')

