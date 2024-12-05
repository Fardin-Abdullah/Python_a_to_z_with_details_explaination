#Sometimes we want to make a class like which has not any relation with real class 
# suppose we want to keep two method in Car class kph to mph and reverse there will be some calculation but it has no relation with the property of certain car object
# then we can call it static method and we can use static method decorator

class Car():
    def __init__(self,name,manufacturer,color,year):
        print("Creating Car")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year 

    def change_gear(self,gear):
        print("Changing gear to",gear)
    
    @staticmethod
    def latest_price(location,manufacturer,name): # it is a static method we did not use self we dont need to create objetc to use this method
        #get theprice from a database or web api
        return 50000

if __name__ == "__main__":
    price = Car.latest_price("Australia","Toyota","Camry")
    print(price)
    # we can also do this by creating object
    mycar = Car("Camry","Toyota","White",2020)
    price = mycar.latest_price("Australia","Toyota","Camry")
    print(price)

# when we want to make an utility function or helper funtion then we use @staticmethod

# sometimes we need to create a type of method which has not a certain relation but it can use multiple 
#property and methodof classto do this we use @classmethod decorator

class Car:
    count = 0
    def __init__(self,name,manufacturer,color,year):
        print("Creating Car")
        self.name = name
        self.year = year 
        self.color = color 
        Car.count += 1
    def change_gear(self,gear):
        print("Changing gear to",gear)
    @classmethod
    def display_count(cls): # here in class method we sent the class as parameter in this method we can call any property or method by cls.
        print("Car count:",cls.count)
    @classmethod
    def reset_count(cls):
        cls.count = 0
    @classmethod
    def reset_display_count(cls):
        cls.reset_count()
        cls.display_count() 
if __name__=="__main__":
    mycar1 = Car("Camry","Toyota","White",2020)
    mycar2 = Car("Camry","Toyota","White",2020)
    mycar3 = Car("Camry","Toyota","White",2020)
    Car.display_count()
    Car.reset_count()
    Car.display_count()

x = dict()
print(type(x))
x = dict.fromkeys([1,2,3])
print(type(x))
# here fromkeys is an alternative way of creating dictionary
@classmethod
def fromtimestamp(cls,t):
    "Construct a date from a POSIX timestamp (like time.time())."
    y,m,d,hh,mm,ss,weekday,jday,dst = _time.localtime(t)
    return cls(y,m,d)
    