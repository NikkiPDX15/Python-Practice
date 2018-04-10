# Importing a single class
# and multi classes 

from car import Car

my_new_car = Car('mercedes', 'e-class', 2018)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 42
my_new_car.read_odometer()



from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# or you can just import Car but then would need
# to specify car.ElectricCar and car.Car
