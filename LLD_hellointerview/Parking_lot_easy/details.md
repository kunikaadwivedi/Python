## Functional Requirements
- Support multiple parking floors, each with a configurable number of parking spots.
- Support multiple vehicle types, including bikes, cars, and trucks
- Classify parking spots by size (e.g., Small, Medium, Large) and match them with appropriate vehicle types
- Automatically assign parking spots based on availability
- Issue a parking ticket upon vehicle entry and track entry and exit times
- Calculate parking fees based on duration of stay and support different pricing strategies, such as flat-rate or vehicle-type-based pricing.
- Support querying and displaying real-time availability of parking spots, grouped by floor and spot size.
- Parking requests can be hardcoded in a driver/demo class for simulation purposes.

Non-Functional Requirements
- The design should follow object-oriented principles with clear separation of concerns
- The system should handle concurrent entry/exit events without race conditions
- The system should be modular and extensible to support future enhancements
- The code should be thread-safe for concurrent access
- The components should be testable in isolation


### Why VehicleSize instead of VehicleType (like Bike, Car, Truck)?

- Designing the system around vehicle size rather than specific vehicle types makes it easier to maintain, scale, and reason about.

- When you use VehicleType, you tie your logic to specific labels like Bike, Car, or Truck. This becomes a problem when a new vehicle type is introduced.

- For example, adding a new type like “Mini Truck” would require updating the allocation logic, billing logic, and compatibility checks.

- On the other hand, using VehicleSize keeps the focus on the space the vehicle occupies, which is the primary concern in a parking lot. Whether a vehicle is a motorcycle, scooter, or bike is less important than the amount of physical room it needs.


#### Vehicle
The Vehicle class is abstract and immutable. Both fields are final


### 1. The "Where Do I Park?" Game Plans (SpotAllocationStrategy)

Imagine a giant toy parking garage with different floors and different sized parking spaces (small, medium, and large). You have two different rules for how cars should find a spot:

#### Plan A: The "Perfect Match" Plan (BestFitStrategy)This plan is very picky. It wants to save big spots for big trucks.How it works: If you have a small toy car, this plan searches the entire garage looking only for small spots first. If it finds one, it parks there. It will only give you a medium spot if all the small ones are totally full.

#### Plan B: The "Closest Spot" Plan (NearestFirstStrategy)This plan is lazy. It just wants to park as fast as possible.How it works: It starts on Floor 1. It looks at the very first spot it sees. If your car fits, it parks right there! It doesn't care if a small car takes a giant truck spot; it just wants to stop driving.


### 2. The "How Much Do I Pay?" Game Plans (FeeStrategy)When it's time to leave the parking garage, you have to pay with toy coins. You wrote three different rules for how much the ticket costs:

#### Plan 1: The "One Price" Rule (FlatRateFeeStrategy)How it works: It doesn't matter if you stayed for one minute or a whole day. It doesn't matter if you drive a tiny motorcycle or a giant semi-truck. Everyone pays exactly 5 coins (or whatever flat rate you choose).

#### Plan 2: The "Clock" Rule (HourlyFeeStrategy)How it works: The longer you stay, the more you pay. If the rule is 2 coins per hour, and you stay for 3 hours, you pay:$$2 \text{ coins} \times 3 \text{ hours} = 6 \text{ coins}$$

#### Plan 3: The "Big Car, Big Money" Rule (VehicleBasedFeeStrategy)How it works: This rule looks at the clock and how big your car is. Tiny cars pay a little bit of money per hour, but giant trucks have to pay a lot of money per hour because they take up so much space!