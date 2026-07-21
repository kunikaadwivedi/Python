from model.vehicle import Vehicle
from vehicle_size import VehicleSize

class Bike(Vehicle):
    def __init__(self, license_plate:str):
        super().__init__(license_plate, VehicleSize.SMALL)