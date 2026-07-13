from typing import List, Optional
from model.parking_spots import ParkingSpots
from vehicle_size import VehicleSize
from spot_allocation_strategy import SpotAllocationStrategy
from model.parking_floors import ParkingFloors

class BestFitStrategy(SpotAllocationStrategy):
    def find_spot(self, floors: List['ParkingFloors'], size: VehicleSize) -> Optional['ParkingSpot']:
        for spot_size in VehicleSize:
            if spot_size < size:
                continue
            for floor in floors:
                for spot in floor.spots:
                    if spot.is_available() and spot.size == spot_size:
                        return spot
        return None