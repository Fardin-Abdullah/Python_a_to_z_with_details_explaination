'''Class = Common Noun and Object = Proper Noun
Suppose we want to make a car class now all the characteristics a car has are called data attribute of the car and 
what it can does is called method 
Now for the car class data attributes will be name,manufacturer,color,year,cc etc and methods can be start,brake,left_right
etc. Let's create the class'''

print("System 1")

#System 1
class Car:
    name = "Premio"  # name and color two attributes
    color = "white"

    def start(): #method
        print("Starting the engine")

print("Name of the car:",Car.name)
print("Color of the car:",Car.color)
Car.start()

print("System 2")

#System 2
class Car:
    name = ""
    color = ""
    def start ():
        print("Starting the engine")

Car.name = "Axio"
Car.color = "Black"
print("Name of the car:",Car.name)
print("Color of the car:",Car.color)
Car.start()
print(dir(Car))

print("System 3")

#System 3 (creating object or instance or doing instantiate)
class Car:
    name = " "
    color = " "
    
    def start ():
        print("Starting the engine")

# creating a car object
my_car = Car() 
my_car.name = "Allion"
print(my_car.name)
#my_car.start() # when we do this the object automatically enters as argument to  the method for this case we will get error 

print("System 4")

#System 4 (solving previous problem)
class Car:
    name = " "
    color = " "
    
    def start (self): # here by giving a parameter the previous problem is solve because now it takes 1 argument 
        print("Starting the engine")

# creating a car object
my_car = Car() 
my_car.name = "Allion"
print(my_car.name)
my_car.start()

print("System 5")

#System 5 (__init__ structure allowing us to give the attribute of objects while we are creating objects)
class Car:
    name = " "
    color = " "  # name, color are class attribute

    def __init__(self,name,color): # when objects are created it is called automatically here 3 names all of them are different      
        self.name = name    
        self.color = color
    def start(self):
        print("Starting the engine")

my_car = Car("BMW","Black")
print(my_car.name,my_car.color)
my_car.start()

print("System 6")

#System 6 (clear concept)
class Car:
    def __init__(self,n,c):  
        self.name = n    # self.name , self.color are instance attribute
        self.color = c
    def start(self):
        print("Starting the engine")

my_car = Car("BMW","Black")  # it is sending the object my_car in self, BMW in n and black in c then when the line 
print(my_car.name,my_car.color) # self.name = n is executed an attribute of my_car object is createde which name is name and n is assigning there
my_car.start()
# print(Car.name) wrong for this system because Car has no attibute named name

print("System 7 ")

#System 7 (if the methods of the class wants to access the attributes of object then)


class Car:
    def __init__(self,n,c):  
        self.name = n    # self.name , self.color are instance attribute
        self.color = c
    def start(self):
        print("name:",self.name)
        print("color:",self.color)
        print("Starting the engine")
my_car = Car("BMW","Black")
my_car.start()

print("System 8")
 
#System 8  (proof that object is sent in self)
class Car :
    def __init__(self,n,c):
        self.name = n
        self.color = c 

    def start(self):
        print("name:",self.name)
        print("color:",self.color)
        print("Starting the engine")

my_car = Car("BMW","Black")
Car.start(my_car)

print("System 9")

#System 9 (creatingmultiple objects)
class Car :
    def __init__(self,n,c):
        self.name = n
        self.color = c 

    def start(self):
        print("name:",self.name)
        print("color:",self.color)
        print("Starting the engine")

my_car1 = Car("Corolla","BLack")   # every objects have different attributes the huge benefits of oop
my_car1.start()
my_car2 = Car("Range Rover","BLack")
my_car2.start()
my_car3 = Car("BMW","BLack")
my_car3.start()

print("System 10")

#System 10 ()
class Car :
    def __init__(self,n,c):
        self.name = n
        self.color = c
    def start(self):
        print("Starting the engine")

car = Car("BMW","White")
car.year = 2017   # when we want to add a data attribute but dont want to change the class
print(car.name,car.color,car.year)