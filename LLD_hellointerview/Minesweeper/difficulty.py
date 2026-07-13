class Difficulty:
    EASY = (9,9,10)
    MEDIUM = (16,16,40)
    HARD = (30,16,99)
    
    def __init__(self, rows, cols, mines_count):
        self.rows = rows
        self.cols = cols
        self.mines_count = mines_count
        
    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def mine_count(self) -> int:
        return self._mine_count