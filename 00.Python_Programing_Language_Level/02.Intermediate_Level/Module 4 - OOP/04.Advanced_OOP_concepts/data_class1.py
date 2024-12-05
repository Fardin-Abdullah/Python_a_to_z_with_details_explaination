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

# now make 5 car object put them in list and sort it
# sometimes we have to make the object of data class into dictionary or tuple we use method from dataclasses
car1 = Car("Camry","Toyot",2020,35000)
car_dt = asdict(car1)
car_tpl = astuple(car1)