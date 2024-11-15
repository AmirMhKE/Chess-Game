from abc import ABC, abstractmethod
from house import House
from decorators import check_move, check_attack

class Piece(ABC):
    color: str = ""

    def __init__(self, color, house):
        self.color: str = color
        self.house: House | None = house

    @check_move
    @abstractmethod
    def move(self, house: House):
        self.house.piece = None
        house.piece = self

    @check_attack(color)
    @abstractmethod
    def attack(self, house: House):
        self.house.piece = self

class Soldier(Piece):
    def __init__(self, color, house):
        self.has_move = False
        super().__init__(color, house)

    def move(self, house: House):
        possible_moves = {self.house.top}
        if not self.has_move:
            possible_moves.add(self.house.top.top)
        
        if house in possible_moves:
            super().move(house)

    def attack(self, house: House):
        possible_attacks = {self.house.top_left, self.house.top_right}
        if house in possible_attacks:
            super().attack(house)

class Horse(Piece):
    def __init__(self, color, house):
        super().__init__(color, house)

class Elephant(Piece):
    def __init__(self, color, house):
        super().__init__(color, house)

class Castle(Piece):
    def __init__(self, color, house):
        super().__init__(color, house)

class Minister(Elephant, Castle):
    def __init__(self, color, house):
        super().__init__(color, house)

class King(Piece):
    def __init__(self, color, house):
        self.is_kish = False
        super().__init__(color, house)
