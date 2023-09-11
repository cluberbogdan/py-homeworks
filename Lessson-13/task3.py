class Car:
    def __init__(self, brand: str, model: str, year: int, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed


    def accelerate(self):
        self.speed = min(self.speed + 5, 200)
    

    def brake(self):
        self.speed = max(self.speed - 5, 0)
    

    def display_speed(self):
        return f'speed car now {self.brand} {self.model} {self.speed} km/h'


my_car = Car("Ford", "Focus", 2016)
print(my_car.display_speed())

my_car.accelerate()
print(my_car.display_speed())

my_car.brake()
print(my_car.display_speed())