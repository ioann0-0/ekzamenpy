from vehicle import Vehicle,Car,Motorcycle

class ParkingLot:
    def __init__(self, car_spots: int, motorcycle_spots: int,):
        self.car_spots = car_spots
        self.motorcycle_spots = motorcycle_spots
        self.parked_vehicles = []
    def park_vehicle(self, vehicle: str):
# Реализация метода для парковки автомобиля или мотоцикла
        self.vehicle = vehicle
        maxSize = self.car_spots + self.motorcycle_spots
        if self.parked_vehicles != maxSize:
            if isinstance(vehicle,Car):
                if self.parked_vehicles != self.motorcycle_spots:
                    self.parked_vehicles.append(vehicle)
                    print("карш припаркован")
                else:
                    print("Нету местa")
            

            elif isinstance(vehicle,Motorcycle):
                if self.parked_vehicles != self.motorcycle_spots:
                    self.parked_vehicles.append(vehicle)
                    print("moto припаркован")
                elif self.parked_vehicles == self.motorcycle_spots:
                    for i in range(self.car_spots):
                        if i != self.car_spots:
                            self.parked_vehicles.append(vehicle)
                            print("мотик был успешно припаркован")
                else:
                    print("Орын жок")
        else:
            print("Парковка полная")
    def remove_vehicle(self, license_plate: str):
# Реализация метода для удаления транспортного средства с парковки
        self.license_plate = license_plate

        self.parked_vehicles.remove(license_plate)
        print("ТС уехало")
    def get_parked_vehicles(self):
        if self.parked_vehicles != []:
           for id,item in enumerate(self.parked_vehicles):
             print(id,item)
        else: 
            print("парковка пуста")