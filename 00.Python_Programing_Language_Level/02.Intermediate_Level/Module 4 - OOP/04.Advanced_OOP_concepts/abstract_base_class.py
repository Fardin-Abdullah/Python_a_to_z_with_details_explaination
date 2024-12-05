# Sometimes we need to make a class like this we can not make object directly then we have to declare that 
# class as abstract class we can inherit it but can not make object directly there can be multiple abstract method in abstract class
# in abstract method we just have to give the method signature those class which will inherit the abstract class #
# will implement the method 

"If we want to make abstract class we have to use abc module"
from abc import ABC, abstractmethod # abc is short form of abstractbase class
class Vehicle(ABC): # we are importing ABC and the vehicle class will inherit ABC class
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    def turn (self,direction):
        print("Turning",self.name,"to",direction)

    @abstractmethod
    def change_gear(self,direction):
        pass


# creating abstract method is easy we can use @abstractmethod decorator it is also created in abc module   
# a = Vehicle()
# a.turn() not possible error

class Car(Vehicle):

    def __init__(self,name,manufacturer,color,year):
        print("Creating a Car")
        super().__init__(name,manufacturer,color)
        self.year = year
    
#a = Car() error
# our python interpreter is also considering Car class as abstract class
# because we did not implement all abstract methods of Vehicle class in Car class
# if all the abstract class of vehicle class is also implemented in the car class , car class will not considered as abstract class
# otherwise it will be consider as abstract class

class Car(Vehicle):
    def __init__(self,name,manufacturer,color,year):
        print("Creating car")
        super().__init__(name,manufacturer,color)
        self.year = year
    
    def change_gear(self,gear):
        print("Changing gear to",gear)
    
if __name__ == "__main__":
    my_car = Car("Camry","Toyota","White",2020)
    print(my_car.name)
    my_car.turn("left")
    my_car.change_gear("D")