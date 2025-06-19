# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand       # Encapsulation
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started.")

    def stop_engine(self):
        print(f"{self.brand} {self.model}'s engine stopped.")

# Derived class (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    # Method Overriding (Polymorphism)
    def start_engine(self):
        print(f"{self.brand} {self.model} car's engine is now running with {self.seats} seats.")

# Another Derived class
class Motorcycle(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self.cc = cc

    # Method Overriding
    def start_engine(self):
        print(f"{self.brand} {self.model} motorcycle's engine ({self.cc}cc) is roaring!")

# Create objects
car = Car("Toyota", "Corolla", 5)
bike = Motorcycle("Yamaha", "R15", 155)

# Call methods
car.start_engine()          # Polymorphism
car.stop_engine()

bike.start_engine()         # Polymorphism
bike.stop_engine()
