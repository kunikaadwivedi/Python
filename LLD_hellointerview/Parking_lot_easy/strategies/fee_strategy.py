from abc import ABC, abstractmethod
from model.parking_ticket import ParkingTicket

class FeesStrategy(ABC):
    @abstractmethod
    def calculated_fee(self, ticket: 'ParkingTicket')-> float:
        pass