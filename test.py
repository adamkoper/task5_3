class Car:

   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0

   def __str__(self):
       return f'{self.color} {self.make} {self.model_name}'

   def __repr__(self):
       return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

   def accelerate(self, step=10):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step

class Truck(Car):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
bubu = isinstance(truck, Car)
print(bubu)

print(truck.current_speed)
truck.accelerate()
truck.current_speed

print(truck.current_speed)