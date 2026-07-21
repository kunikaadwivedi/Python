import threading
import uuid
from datetime import datetime
from typing import List, Dict, Optional
from model.parking_floors import ParkingFloors
from strategies.fee_strategy import FeesStrategy
from strategies.spot_allocation_strategy import SpotAllocationStrategy
from model.parking_ticket import ParkingTicket
from model.vehicle import Vehicle
from vehicle_size import VehicleSize
from user_error_handling import UserErrorHandling

class ParkingLot:
    _instance : Optional['ParkingLot'] = None
    _lock = threading.Lock()
    
    
    def __init__(self):
        self._floors: List[ParkingFloors] = []    
        self._active_tickets: Dict[str, ParkingTicket] = {}
        self._fee_strategy: Optional[FeesStrategy] = None
        self._allocation_strategy: Optional[SpotAllocationStrategy] = None
        
    @classmethod
    def get_instance(cls) -> 'ParkingLot':
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None: #double-checked locking
                    cls._instance = ParkingLot()
                    
        return cls._instance
    
    def initialize(self, floors: List[ParkingFloors], fee_strategy: FeesStrategy, allocation_strategy: SpotAllocationStrategy) -> None:
        self._floors = floors
        self._fee_strategy = fee_strategy
        self._allocation_strategy = allocation_strategy
        
    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        while True:
            spot = self._allocation_strategy.find_spot(self._floors, vehicle.size)
            if spot is None:
                raise UserErrorHandling(f"No available parking spot for the {vehicle.size}.")
            
            try:
                spot.park_vehicle(vehicle)
                break
            except UserErrorHandling:
                pass # Spot was taken by another thread, try again
            
        ticket_id = str(uuid.uuid4())[:8]
        ticket = ParkingTicket(ticket_id, vehicle, spot)
        self._active_tickets[ticket_id] = ticket
            
        print(f"Parked {vehicle} at spot {spot.spot_id}. Ticket: {ticket_id}")
        return ticket
    
    def unpark_vehicle(self, ticket_id:str)-> float:
        ticket = self._active_tickets.pop(ticket_id, None)
        if ticket is None:
            raise UserErrorHandling(f"Invalid ticket: {ticket_id}")
        ticket.set_exit_time(datetime.now())
        fee = self._fee_strategy.calculated_fee(ticket)
        
        ticket.spot_.unpark_vehicle()
        print(f"Unparked {ticket.vehicle} from spot {ticket.spot.spot_id}. Fee: ${fee:.2f}")
        
        return fee
    
    def display_availability(self) -> None:
        print("==== PARKING AVAILABILITY ====")
        for floor in self._floors:
            parts = []
            for size in VehicleSize:
                count = 0
                for spot in floor.spots:
                    if spot.is_available() and spot.size == size:
                        count+=1
                        
                parts.append(f"{size.name} = {count}")
            print(f"Floor {floor.floor_number}:{', '.join(parts)}")
        print("================================\n")
        
    def set_fee_strategy(self, fee_strategy:FeesStrategy):
        self._fee_strategy = fee_strategy
    
    def set_allocation_strategy(self, allocation_strategy: SpotAllocationStrategy):
        self._allocation_strategy = allocation_strategy
        
    @classmethod
    def reset_instance(cls) -> None:
        with cls._lock:
            cls._instance = None
                
        
            
        
    