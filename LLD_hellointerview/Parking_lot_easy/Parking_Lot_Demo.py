from vehicle_size import VehicleSize
from Parking_LOT import ParkingLot
from model.parking_floors import ParkingFloors
from strategies.hourly_fee_strategy import HourlyFeeStrategy
from strategies.nearest_first_strategy import NearestFirstStrategy
from strategies.best_fit_strategy import BestFitStrategy
from model.bike import Bike
from model.car import Car
from model.truck import Truck
from user_error_handling import UserErrorHandling

def main() -> None:
    floor1_counts = {VehicleSize.SMALL:2, VehicleSize.MEDIUM:3, VehicleSize.LARGE:1}
    floor2_counts = {VehicleSize.SMALL:3, VehicleSize.MEDIUM:2, VehicleSize.LARGE:1}
    
    floors = [
        ParkingFloors(1, floor1_counts),
        ParkingFloors(2, floor2_counts)
    ]
    
    lot = ParkingLot.get_instance()
    lot.initialize(floors, HourlyFeeStrategy(7.8), NearestFirstStrategy())
    
    lot.display_availability()
    
    # === Scenario 1: Park a few vehicles (nearest-first) ===
    print("============= SCENARIO 1: Park Vehicles (Nearest-First) ============= ")
    bike_ticket = lot.park_vehicle(Bike("KA-01-1111"))
    car_ticket = lot.park_vehicle(Car("KA-02-2222"))
    lot.park_vehicle(Truck("KA-03-3333"))
    
    print("=============  SCENARIO 2: Park with BEST Fit ============= ")
    
    lot.set_allocation_strategy(BestFitStrategy())
    lot.park_vehicle(Bike("KA-04-4444"))
    
    print("============= SCENARIO 3: Unpark Vehicles")  
    lot.unpark_vehicle(bike_ticket.ticket_id)
    lot.unpark_vehicle(car_ticket.ticket_id)
    
    lot.display_availability()
    
    print("=============== SCENARIO 4: NO Spot Available =============") 
    try:
        lot.park_vehicle(Truck("KA-58-9999"))
        lot.park_vehicle(Truck("KA-23-8787")) 
        lot.display_availability()
        
    except UserErrorHandling as e:
        print(f"Caught Unexpected error: {e}")   
    # Clean up the singleton so repeated runs start fresh
    ParkingLot.reset_instance()


if __name__ == "__main__":
    main()