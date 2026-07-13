from typing import Dict
from fee_strategy import FeesStrategy
from vehicle_size import VehicleSize
from model.parking_ticket import ParkingTicket
class VehicleBasedFeeStrategy(FeesStrategy):
    def __init__(self, rate_per_hour: Dict[VehicleSize, float]):
        self._rate_per_hour = rate_per_hour
        
    def calculate_fee(self, ticket: ParkingTicket) -> float:
        size = ticket.vehicle.size
        rate = self._rate_per_hour.get(size, 0)
        return ticket.get_duration_in_hours() * rate