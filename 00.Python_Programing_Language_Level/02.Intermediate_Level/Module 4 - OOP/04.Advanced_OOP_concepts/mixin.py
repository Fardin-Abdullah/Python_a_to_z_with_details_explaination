"We use multiple inheritance for creating mixin"
# Suppose we can not change our car class now for selling car the showroom is giving 30% discount and this calculation will
# be used in different places now if someone want to give 32 % discount then we have to change the calculated price
# here we can use mixin xlass
# 
class Car:
    def __init__(self,name,manufacturer,price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

class CarPriceMixin:# here this class can't be inherit directly or can't make object
# in Django mixin class is very important also in socket program but be careful it makes program complex
# sometimes we can use composition instead of inheritance 
 
    def clearance_price(self):
        return self.price * 0.7

class ShowroomCar(Car,CarPriceMixin):
    pass

if __name__ == "__main__":
    c = ShowroomCar("Camry","Toyota",38000)
    print("Clearance price:",c.clearance_price())