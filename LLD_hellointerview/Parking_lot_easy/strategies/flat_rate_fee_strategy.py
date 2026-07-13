from fee_strategy import FeesStrategy
from model.parking_ticket import ParkingTicket

class FlatRateFeeStrategy(FeesStrategy):
    
    def __init__(self, flat_rate: float):
        self._flat_rate = flat_rate
        
    def calculated_fee(self, ticket: ParkingTicket) -> float:
        return self._flat_rate
    