import random 

def winner(user, comp):
    # We need the global keyword to modify these variables inside a function
    global scorecomp, scoreuser
    
    # 0: Snake, 1: Water, 2: Gun
    if user == comp:
        print("It's a tie for this round!")
        return

    if comp == 0:  # Comp chooses Snake
        if user == 1: # Water
            print("Point goes to comp (Snake drinks Water)")
            scorecomp += 1
        elif user == 2: # Gun
            print("Point goes to you (Gun kills Snake)")
            scoreuser += 1
            
    elif comp == 1:  # Comp chooses Water
        if user == 2: # Gun
            print("Point goes to comp (Water destroys Gun)")
            scorecomp += 1
        elif user == 0: # Snake
            print("Point goes to you (Snake drinks Water)")
            scoreuser += 1
            
    elif comp == 2:  # Comp chooses Gun
        if user == 0: # Snake
            print("Point goes to comp (Gun kills Snake)")
            scorecomp += 1
        elif user == 1: # Water
            print("Point goes to you (Water destroys Gun)")
            scoreuser += 1
            
        
def scorecard(scorecomp, scoreuser):
    print("\n--- FINAL SCORECARD ---")
    print(f"You: {scoreuser}, Comp: {scorecomp}")
    if scorecomp > scoreuser:
        print("Comp won the game!! 🤖")
    elif scorecomp < scoreuser:
        print("You won the game!! 🎉")
    else:
        print("The game is a tie! 👔")
        

# Initialize scores
scorecomp = 0
scoreuser = 0

print("Welcome to my game: Snake🐍, Water💧, Gun🔫")
print("Rules are simple:")
print("1. Snake drinks Water (0 beats 1)")
print("2. Water destroys Gun (1 beats 2)")
print("3. Gun kills Snake (2 beats 0)\n")

while True:
    comp = random.randint(0, 2)
    
    # Simple check to make sure user enters a valid number
    try:
        user = int(input("Enter the choice -> 0:snake, 1:water, 2:gun: "))
        if user not in [0, 1, 2]:
            print("Invalid choice! Please enter 0, 1, or 2.")
            continue
    except ValueError:
        print("Please enter a valid integer.")
        continue
        
    winner(user, comp)
    i = input("Do you want to play again? (y/n): ").lower().strip()
    if i == 'y':
        print("-" * 20)
        continue
    else:
        break

scorecard(scorecomp, scoreuser)