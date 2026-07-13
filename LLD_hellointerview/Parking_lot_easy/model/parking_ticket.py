from datetime import datetime
from typing import Optional

class ParkingTicket:
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: 'ParkingSpot'):
        self._ticket_id = ticket_id
        self._vehicle = vehicle
        self._spot = spot
        self._entry_time = datetime.now()
        self._exit_time: Optional[datetime] = None
        
    def set_exit_time(self, exit_time: datetime) -> None:
        self._exit_time  = exit_time
        
    def get_duration_in_hours(self) -> int:
        end = self._exit_time if self._exit_time else datetime.now()
        datetime.now()
        duration = end - self._entry_time
        total_seconds = int(duration.total_seconds())
        hours = (total_seconds +3599) // 3600
        return max(1, hours)
        
    @property
    def ticket_id(self) -> str:
        return self._ticket_id
    
    @property
    def vehicle(self) -> Vehicle:
        return self._vehicle
        