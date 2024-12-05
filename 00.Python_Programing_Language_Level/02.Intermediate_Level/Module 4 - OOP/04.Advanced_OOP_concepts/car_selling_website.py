class Car:
    def __init__(self,name,manufacturer,year,price):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year 
        self.price = price 
    
    def __add__(self,other):
        return self.price + other.price

if __name__ == "__main__":
    car1 = Car("Carmy","Toyota",2020,32000)
    car2 = Car("Carmy","Toyota",2020,38000)
    print(car1 + car2)

# if we use same operator for many operations it is called operator overloading