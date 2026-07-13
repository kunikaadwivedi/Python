import threading
import uuid
from datetime import datetime
from typing import List, Dict, Optional
from model.parking_floors import ParkingFloors
from strategies.fee_strategy import FeesStrategy
from strategies.spot_allocation_strategy import SpotAllocationStrategy
from model.parking_ticket import ParkingTicket


class ParkingLot:
    _instance = Optional['ParkingLot'] = None
    _lock = threading.Lock()
    
    
    def __init__(self):
        self._floors: List[ParkingFloors] = []    
        self._active_tickets: Dict[str, ParkingTicket] = {}
        self._fee_strategy: Optional[FeesStrategy] = None
        self._
        