'''racing game car,bike every types of vehicle'''

print("System 1")

#System 1
class Vehicle:
    '''Base class for all vehicle or parent class''' # this is called docstring
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    def drive(self):
        print("Driving",self.manufacturer,self.name)
    def turn(self,direction):
        print("Turning",self.name,"to",direction)
    def brake(self):
        print(self.name,"is stopping!")

if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 Ex","Walton","Black")
    v2 = Vehicle("Softail delux","Harley Davidson","Orange")
    v3 = Vehicle("Mustang 5.0","Ford","Red")
    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn("left")
    v2.turn("right")

    v1.brake()
    v2.brake()
    v3.brake()
#creating car class
class Car(Vehicle):  # it means the car class and it inherits vehicle class
    '''Car class'''
    def change_gear(self,gear_name):
        print(self.name,"is changing gear to",gear_name)

c = Car("Mustang 5.0 GT coupe","Ford","Red") # but there is not any constructor in car class so it will find in base class vehicle class and call the constructor of it

print("Systrm 2")

#System 2
class Vehicle:
    '''Base class for all vehicle or parent class''' # this is called docstring
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    def drive(self):
        print("Driving",self.manufacturer,self.name)
    def turn(self,direction):
        print("Turning",self.name,"to",direction)
    def brake(self):
        print(self.name,"is stopping!")
class Car(Vehicle):
    '''Car class'''
    def change_gear(self,gear_name):
        '''Method for changing gear'''
        print(self.name,"is changing gear to",gear_name)
    
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe","Ford","Red")
    c.drive()
    c.brake()
    c.change_gear("P")
