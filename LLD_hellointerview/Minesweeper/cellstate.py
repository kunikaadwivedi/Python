from enum import Enum

class CellState(Enum):
    HIDDEN = "hidden"
    REVEALED = "revealed"
    FLAGGED = "flagged"
    
    