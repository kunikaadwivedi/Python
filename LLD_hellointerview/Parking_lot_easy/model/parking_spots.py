import threading 
from typing import Optional
from vehicle_size import VehicleSize
from vehicle import Vehicle
from user_error_handling import UserErrorHandling

class ParkingSpots:
    def __init__(self, spot_id: int, size: VehicleSize):
        self._spot_id = spot_id
        self._size = size
        self._parked_vehicle: Optional[Vehicle] = None
        self._lock = threading.Lock()
    
    def is_available(self) -> bool:
        return self._parked_vehicle is None 
    
    def can_fit_vehicle(self, vehicle_size: VehicleSize) -> bool:
        return self._size>= vehicle_size
    
    def park_vehicle(self, vehicle:Vehicle) -> None:
        with self._lock:
            if not self.is_available():
                raise UserErrorHandling(f"spot {self._spot_id} is already occupied.")
            if not self.can_fit_vehicle(vehicle.get_size()):
                raise UserErrorHandling(f"Vehicle size {vehicle.size.name} cannot fit in spot size {self._size.name}.")
            self._parked_vehicle = vehicle
            
    def unpark_vehicle(self) -> Vehicle:
        with self._lock:
            if self.is_available():
                raise UserErrorHandling(f"spot {self._spot_id} is already empty.")
            vehicle = self._parked_vehicle
            self._parked_vehicle = None
            return vehicle
    @property
    def spot_id(self) -> str:
        return self._spot_id
    
    @property
    def size(self) -> VehicleSize:
        return self._size
    
    @property
    def parked_vehicle(self) -> Optional[Vehicle]:
        return self._parked_vehicle