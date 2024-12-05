class Car:
    def __init__(self,name,manufacturer,year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year 
if __name__ ==( "__main__"):
    car1 = Car("Carmy","Toyota",2022)
    print(car1)

# we will create __repr__ method  it is created like this so that it is understanable how is object created
# so if we send in eval() function the output of repr() function then there will be a car object
# the main aim of __str__() method is to give the meaningful and easy output to user
# while  printing object using print fuction if at first in the class __str__() method is implented,then
#this method will be called otherwise __repr__() method will be called
class Car:
    def __init__(self,name,manufacturer,year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
    def __repr__(self):
        return "Car('{}','{}',{})".format(self.name,self.manufacturer,self.year)
        #skip this method for now
    def __str__(self):
        return "{} {} {}".format(self.manufacturer,self.name,self.year)

if __name__ == "__main__":
    car1 = Car("Camry","Toyota",2022)
    print(car1)
    print(str(car1))
    car = Car("Camry","Toyota",2020)
    print(car)
    print(repr(car))
