from vehicle_size import VehicleSize
from abc import ABC
class Vehicle(ABC):
    def __init__(self, license_plate:str, size: VehicleSize):
        if not license_plate or not license_plate.strip():
            raise ValueError("License plate cannot be empty or whitespace.")
        self._license_plate = license_plate
        self._size = size
        
    @property
    def license_plate(self) -> str:
        return self._license_plate
    
    @property
    def size(self) -> VehicleSize:
        return self._size
    
    def __str__(self):
        return f"{self.__class__.__name__}[{self._license_plate}]"