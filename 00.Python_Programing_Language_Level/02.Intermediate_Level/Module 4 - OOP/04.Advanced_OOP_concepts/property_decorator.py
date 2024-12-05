"Many programming languages have 3 types of class instance variables.(a)public(b)private(c)protected"
"Private variable of any class is not accessable through outside and protected variables are accessable only"
"Through the class or thr subclasss of that class"
"But in python everything is public.But if someone wants to make private variable he can use a symbol to"
"tell that it is a private variable"

class Car:
    def __init__(self,name,manufacturer,year,price=None):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self._price = price # this underscore previous the price is telling that it is a private variable 
        # and also telling that no one should access it directly
        # in maximum programming language there is one method to read the value and one to change the value of private variable
        # getter() and setter
        # if price is private then get_price() and set_price() two method have to create but in pythowe dont need
        # to create it we can use directly property decorator

class Car:
    def __init__(self,name,manufacturer,year,price=None):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self._price = price
    @property # which method is getter method we have to use property decorater before it 
    def price(self):
        return self._price
    #another way to right
    @property
    def price(self):
        return '${:.2f}'.format(self._price)
    
    @price.setter # if the method name is fnc instead of price we would right fnc
    def price(self,new_price):
        if not isinstance(new_price,(float,int)):
            print("invalid data for price")
        elif new_price < 0 :
            print("price can't be negative")
        else:
            self._price = new_price
    
    @price.deleter
    def price(self):
        self._price = None
    # note that here we have three method all have the same name but the decorators are different
if __name__ == "__main__":
    car = Car("Carmy","Toyota",2022,35000)
    car.price = 38000
    print(car.price)
    car.price = "100"
    print(car.price)   

