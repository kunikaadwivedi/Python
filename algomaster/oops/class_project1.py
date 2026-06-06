class Restaurant:
    restaurant_name = "Pookies Diner"
    customer_capacity = 50
    
    def __init__(self, menu):
        self.total_bill = 0.0
        self.menu = menu
        self.available_seats = self.customer_capacity
    
    def seat_guests(self, number_of_people):
        """Checks if there is enough room and updates available seats."""
        if number_of_people <= self.available_seats:
            self.available_seats -= number_of_people
            print(f"Seated {number_of_people} people. Seats left: {self.available_seats}")
        else:
            print(f"Sorry, not enough room! Only {self.available_seats} seats left.")
    
    def scan_menu(self):
        print(f"Welcome to {self.restaurant_name}!")
        print("Today's menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")
    
    def place_order(self, item, quantity):
        item_lower = item.lower()
        if item_lower in self.menu:
            item_price = self.menu[item_lower]
            total_item_price = item_price * quantity
            self.total_bill += total_item_price  
            print(f"-> Added {quantity}x {item.title()} to the order. Current bill: ${self.total_bill:.2f}")
        else:
            print(f"-> Sorry, we don't serve '{item}' here.")
        
    def get_remaining_seats(self):
        """Quickly returns the number of empty seats."""
        return self.available_seats
    
# 1. Define a menu (using a Python dictionary)
my_menu = {
    "burger": 10.99,
    "pizza": 14.50,
    "fries": 3.99,
    "soda": 2.50
}

kikus_diner = Restaurant(my_menu)

# --- Interactive User Input Loop ---
kikus_diner.scan_menu()

print("\n--- Let's manage the restaurant table ---")

# 1. Input for Seating Guests
# We wrap input() in int() because we need a number for calculations
guests = int(input("How many guests arrived? "))
kikus_diner.seat_guests(guests)

# 2. Input for Placing an Order
print("\n--- Time to order food ---")
food_choice = input("What would you like to order? ")
food_qty = int(input(f"How many units of '{food_choice}'? "))

# Pass the user's inputs directly into the class method!
kikus_diner.place_order(food_choice, food_qty)
        
    
print("\n--- Taking Orders ---")

# We create a flag variable to control the loop
ordering = True

while ordering:
    # 1. Ask what they want to order
    food_choice = input("\nWhat would you like to order? ")
    food_qty = int(input(f"How many units of '{food_choice}'? "))
    
    # 2. Process the order through our class
    kikus_diner.place_order(food_choice, food_qty)
    
    # 3. Ask the crucial question: "Anything else?"
    anything_else = input("\nWould you like to order anything else? (yes/no): ").lower().strip()
    
    # 4. If they say no, stop the loop
    if anything_else == "no":
        ordering = False
        print("\nThank you for ordering!")
        print(f"Your final grand total is: ${diner.total_bill:.2f}")
        print("Have a wonderful day!")