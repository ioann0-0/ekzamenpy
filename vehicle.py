class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: str):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Car")
        
    def __str__(self):
        return self.license_plate
class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Motorcycle")

    def __str__(self):
        return self.license_plate
