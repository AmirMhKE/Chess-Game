class House:
    def __init__(self, x: int, y: int, piece):
        self.x = x
        self.y = y
        self.piece = piece
        self.top = self.down = self.right = self.left = None
        self.top_right = self.top_left = self.down_right = self.down_left = None 
