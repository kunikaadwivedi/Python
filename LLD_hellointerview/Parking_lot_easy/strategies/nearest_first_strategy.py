from typing import List, Optional
from model.parking_spots import ParkingSpots
from vehicle_size import VehicleSize
from strategies.spot_allocation_strategy import SpotAllocationStrategy
from model.parking_floors import ParkingFloors

class NearestFirstStrategy(SpotAllocationStrategy):
    def find_spot(self, floors: List['ParkingFloors'], size: VehicleSize) -> Optional['ParkingSpots']:
        for floor in floors:
            spot = floor.find_available_spot(size)
            if spot is not None:
                return spot
        return None