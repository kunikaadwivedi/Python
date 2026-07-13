from typing import List, Optional
from model.parking_spots import ParkingSpot
from vehicle_size import VehicleSize
from spot_allocation_strategy import SpotAllocationStrategy
from model.parking_floors import ParkingFloors

class NearestFirstStrategy(SpotAllocationStrategy):
    def find_spot(self, floors: List['ParkingFloors'], size: VehicleSize) -> Optional['ParkingSpot']:
        for floor in floors:
            spot = floor.find_available_spot(size)
            if spot is not None:
                return spot
        return None