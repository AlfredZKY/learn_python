from collections import namedtuple

# 以前简单的类可以使用namedtuple实现
Car = namedtuple('Car','color mileage')

my_car = Car('red','3812.4','Auto')
print(my_car.color)
print(my_car)