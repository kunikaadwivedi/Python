from players import Players
from game import SnakeAndLadders

def main():
    game_engine = SnakeAndLadders(board_size = 100)
    print("🎲 WELCOME TO SNAKE & LADDER LLD SIMULATOR 🎲\n")
    
    while True:
        try: 
            num_players = int(input("Enter the no. of players(2-6)"))
            if num_players <2:
                print("⚠️ You need at least 2 players to play!")
                continue
            break
        except ValueError:
            print("⚠️ Please enter a valid number.")
            
    print("\n✍️ Enter player names:")
    
    # 2. Manually collect names in a loop
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ").strip()
        
        # Fallback if they just press Enter without typing anything
        if not name:
            name = f"Player_{i}"
            
        # Create unique ID (e.g., P1, P2, P3) and create the Player object
        player_id = f"P{i}"
        player = Players(player_id=player_id, name=name)
        
        # Add player to the game engine
        game_engine.add_player(player)
    
    print("\n--- All players registered! Let's begin ---")
    game_engine.start_game()
    
if __name__ == '__main__':
    main()
    