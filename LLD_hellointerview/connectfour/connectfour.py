import enum

class BoardPosition(enum.Enum):
    Empty = 0
    Red = 1
    Yellow = 2
    
class Board:
    def __init__(self, rows, columns):
        