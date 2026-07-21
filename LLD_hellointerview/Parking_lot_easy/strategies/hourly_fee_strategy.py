from strategies.fee_strategy import FeesStrategy
from model.parking_ticket import ParkingTicket

class HourlyFeeStrategy(FeesStrategy):
    def __init__(self, rate_per_hour: float):
        self._rate_per_hour = rate_per_hour
    def calculated_fee(self, ticket: ParkingTicket) -> float:
        return ticket.get_duration_in_hours() * self._rate_per_hour