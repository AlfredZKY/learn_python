from collections import namedtuple
from dataclasses import dataclass
# 以前简单的类可以使用namedtuple实现
Car = namedtuple('Car','color mileage')

my_car = Car('red',3812.4)
print(my_car.color)
print(my_car)

@dataclass
class Car1:
    color:str
    mileage:float

my_car = Car1('red',3812.4)
print(my_car.color)
print(my_car)