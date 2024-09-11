from vehicle import Car,Motorcycle
from parking_lot import ParkingLot

carh1 = Car("BMW123")
carh2 = Car("BMW123")
carh3 = Car("BMW123")
moto1 = Motorcycle("Suzuki")
moto2 = Motorcycle("Suzuki")

appletown = ParkingLot(3,1)


appletown.park_vehicle(carh1)
appletown.park_vehicle(carh2)
appletown.park_vehicle(moto1)
appletown.park_vehicle(moto2)
appletown.park_vehicle(carh3)

appletown.get_parked_vehicles()
# appletown.remove_vehicle(carh1)