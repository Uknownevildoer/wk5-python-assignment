# ASSIGNMENT 1
class vehicle:
  def __init__(self, color, model):
    self.color= color #instance variable
    self.model= model #instance variable

  def description(self):
    print(f"This vehicle is a {self.model} colored {self.color}")

# class inheriting from vehicle
class Electricvehicle(vehicle):
    def __init__(self, color, model, battery_capacity):
        super().__init__(color, model)  # Call the constructor of vehicle
        self.battery_capacity = battery_capacity
    
    #Method overriding (polymorphism)
    def description(self):
        print(f"This vehicle is a {self.model} colored {self.color} with a {self.battery_capacity}kWh battery.")

my_vehicle= vehicle("silver","Mercedes Benz")
my_vehicle.description()

my_electric= Electricvehicle("Blue", "Tesla", 70)
my_electric.description()

#ACTIVITY 2
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # Each object calls its own version of move()
