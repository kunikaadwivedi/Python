class Restaurant:
    restaurant_name = "Pookies Diner"
    customer_capacity = 50
    
    def __init__(self, menu):
        self.menu = menu
        self.available_seats = self.customer_capacity
        self.customers_log = []  # Tracks all groups that enter today
        
        # These reset per order session
        self.total_bill = 0.0
        self.orders_list = []  
    
    def seat_guests(self, number_of_people):
        """Checks if there is enough room and reduces available seats."""
        if number_of_people <= self.available_seats:
            self.available_seats -= number_of_people  # Seats decrease here!
            
            group_number = len(self.customers_log) + 1
            self.customers_log.append(f"Party #{group_number}: {number_of_people} people")
            
            print(f"-> Success! Seated {number_of_people} people. Seats remaining: {self.available_seats}")
            return True 
        else:
            print(f"-> Sorry, not enough room! Only {self.available_seats} seats left.")
            return False 
    
    def scan_menu(self):
        print(f"\nWelcome to {self.restaurant_name}!")
        print("Today's menu:")
        for item, price in self.menu.items():
            print(f"  {item.title()}: ${price:.2f}")
    
    def place_order(self, item, quantity):
        item_lower = item.lower()
        if item_lower in self.menu:
            item_price = self.menu[item_lower]
            total_item_price = item_price * quantity
            self.total_bill += total_item_price  
            
            self.orders_list.append(f"{quantity}x {item.title()}")
            print(f"-> Added {quantity}x {item.title()} to the order. Current bill: ${self.total_bill:.2f}")
        else:
            print(f"-> Sorry, we don't serve '{item}' here.")
            
    def clear_order_session(self):
        """Resets the bill and order list for the next customer group."""
        self.total_bill = 0.0
        self.orders_list = []


# --- Setup Data ---
my_menu = {
    "burger": 10.99,
    "pizza": 14.50,
    "fries": 3.99,
    "soda": 2.50
}

kikus_diner = Restaurant(my_menu)
kikus_diner.scan_menu()

# --- THE GRAND MASTER LOOP ---
shift_active = True

while shift_active:
    print("\n==========================================")
    print(f"  CURRENT AVAILABLE SEATS IN DINER: {kikus_diner.available_seats}  ")
    print("==========================================")
    
    # 1. Input for Seating
    guests_input = input("How many guests arrived? (or type 'close'): ").lower().strip()
    
    if guests_input == 'close':
        shift_active = False
        print("\nClosing up Pookies Diner for the day!")
        print("\n--- Final Seating Audit Log for Today ---")
        for entry in kikus_diner.customers_log:
            print(f"- {entry}")
        break
        
    guests = int(guests_input)
    seating_success = kikus_diner.seat_guests(guests)
    
    # If there wasn't enough room, go back to the top and wait for a smaller party
    if not seating_success:
        continue

    # 2. Input for Ordering
    print("\n--- Taking Orders for This Party ---")
    ordering = True
    
    while ordering:
        food_choice = input("What would you like to order? ")
        food_qty = int(input(f"How many units of '{food_choice}'? "))
        
        kikus_diner.place_order(food_choice, food_qty)
        
        anything_else = input("\nWould you like to order anything else? (yes/no): ").lower().strip()
        
        if anything_else == "no":
            ordering = False
            
            # Print receipt
            print("\n--- Current Table Receipt ---")
            for ordered_item in kikus_diner.orders_list:
                print(f"- {ordered_item}")
            print(f"Total for this order: ${kikus_diner.total_bill:.2f}")
            print("Enjoy your meal!")
            
            # Reset order tracking data, but DO NOT touch the seats
            kikus_diner.clear_order_session()