class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def update_odometer(self, mileage):
        self.odometer_reading += mileage
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def red_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
my_used_car = Car('subaru', 'outvack', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.odometer_reading = 23500
my_used_car.red_odometer()
my_used_car.update_odometer(100)
my_used_car.red_odometer()
