from typing import List, Dict, Optional
from vehicle_size import VehicleSize
from model.parking_spots import ParkingSpots

class ParkingFloors:
    def __init__(self, floor_number: int, spot_counts: Dict[VehicleSize, int]):
        self._floor_number = floor_number
        self._spots: List[ParkingSpots] = []
        self._initialize_spots(spot_counts)
        
    def _initialize_spots(self, spot_counts: Dict[VehicleSize, int]) -> None:
        for size in VehicleSize:
            count = spot_counts.get(size, 0)  # FIXED: Added default value and key
            prefix = self._get_size_prefix(size)
            for i in range(1, count + 1):
                spot_id = f"F{self._floor_number}-{prefix}{i:03d}"
                self._spots.append(ParkingSpots(spot_id, size))
                
    def _get_size_prefix(self, size: VehicleSize) -> str:
        prefixes = { 
            VehicleSize.SMALL: "S",
            VehicleSize.MEDIUM: "M",
            VehicleSize.LARGE: "L"
        }
        return prefixes.get(size, "X")
    
    def find_available_spot(self, size: VehicleSize) -> Optional[ParkingSpots]:
        for spot in self._spots:
            if spot.is_available() and spot.can_fit_vehicle(size):  # FIXED: Call method properly
                return spot
        return None   
    
    @property 
    def floor_number(self) -> int:
        return self._floor_number
    
    @property
    def spots(self) -> List['ParkingSpots']:
        return self._spots