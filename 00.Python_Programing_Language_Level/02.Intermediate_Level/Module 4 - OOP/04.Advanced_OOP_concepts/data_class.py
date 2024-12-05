"IF we want to make an web application where we will sell car there in the class of car there will be only attribute not any method"
"We can do this work easily by using data class "
# know type hinting
# to make data class have to use @dataclass decorator
from dataclasses import dataclass

@dataclass
class Car :
    name: str
    manufacturer : str
    year : int
    price : int
if __name__ == "__main__":
    car1 = Car("Camry","Toyota",2020,35000)
    print(car1)
# here we dont need to create __init__ method or __repr__() method
if __name__ == "__main__":
    car1 = Car("Camry","Toyota",2020,35000)
    car2 = Car("Camry","Toyota",2020,35000)
    car3 = Car("Camry","Toyota",2020,35000)
    print(car1 == car2)
    print(car2 == car3)
# we can sort the car according to price first have to send in decorator order= True then have to tell according to which atteibute has to sort
# have to use sort_index field and post_init have to assign price in sort_index watcgh example

from dataclasses import dataclass,field
@dataclass(order = True)
class Car:
    sort_index : int = field(init=False,repr=False)
    name: str
    manufacturer: str
    year: int
    price: int

    def __post__init__(self):
        self.sort_index = self.price

if __name__== "__main__":
    car1 = Car("Camry","Toyota",2020,38000)
    car2 = Car("Prado","Toyota",2021,70000)
    car3 = Car("Corolla","Toyota",2021,32000)
    print(car1)
    print(car2)
    print(car3)
    print(car1 > car2)
    print(car2 > car3)
