from abc import ABC, abstractmethod
from typing import List, Optional
from model.parking_spots import ParkingSpot
from vehicle_size import VehicleSize
from model.parking_floors import ParkingFloors
class SpotAllocationStrategy(ABC):

    @abstractmethod
    def find_spot(self, floors: List['ParkingFloors'], size: 'VehicleSize') -> Optional['ParkingSpot']: