from collections import deque
from typing import List, Dict
from players import Players
from dice import Dice
from game_status import GameStatus

class SnakeAndLadders:
    def __init__(self, board_size: int = 100):
        self.board_size = board_size
        self.dice = Dice(min_value=1, max_value=6)
        self.status = GameStatus.NOT_STARTED
        
        # Players are stored in a queue to naturally handle round-robin turns
        self.players: deque[Players] = deque()
        
        # Key: Start/Head -> Value: End/Tail
        self.snakes: Dict[int, int] = {
            99: 54, 70: 55, 52: 42, 25: 2
        }
        self.ladders: Dict[int, int] = {
            6: 25, 11: 40, 60: 85, 46: 90
        }
    
    def add_player(self, player: Players):  # Changed name to singular to match main.py call
        if self.status != GameStatus.NOT_STARTED:
            print("Game already started! Can't add players now.")
            return
        self.players.append(player)         # Fixed: Append directly to self.players queue
    
    def start_game(self):
        if len(self.players) < 2:
            print("❌ Need at least 2 players to start the game.")
            return
        
        self.status = GameStatus.RUNNING
        print("🏁 Game has just begun!\n")
        
        while self.status == GameStatus.RUNNING:
            current_player = self.players.popleft()
            roll_value = self.dice.roll()
            old_position = current_player.position
            new_position = old_position + roll_value
            
            print(f"🎲 {current_player.name} rolled a {roll_value}. Moving {old_position} -> {new_position}")
            
            if new_position > self.board_size:
                print(f"⚠️ Invalid move!! You need to roll exactly {self.board_size - old_position} to win. Skip turn.")
                self.players.append(current_player)
                continue
            
            if new_position in self.snakes:
                final_position = self.snakes[new_position]
                print(f"🐍 Oops!! {current_player.name} was bitten by a snake at {new_position}! Sliding down to {final_position}")
            elif new_position in self.ladders:
                final_position = self.ladders[new_position]
                print(f"🪜 Hurrah!! {current_player.name} encountered a ladder at {new_position}! Climbing up to {final_position}")
            else:
                final_position = new_position
                
            current_player.position = final_position
            print(f"📍 {current_player.name} is now at position {current_player.position}\n")
            
            if current_player.position == self.board_size:
                self.status = GameStatus.FINISHED
                print(f"🎉🎉 Congratulations!! {current_player.name} won the game! 🎉🎉")
                break
            
            self.players.append(current_player)