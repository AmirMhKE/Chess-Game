from functools import wraps
from house import House
from errors import MoveError, AttackError

def check_move(func):
    @wraps(func)
    def wrapper(house: House):
        if not house.piece:
            func(house)
        raise MoveError("Your piece can't move!")
    
    return wrapper

def check_attack(color):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(house: House):
            if house.piece and house.piece.color != color:
                func(house)
            raise AttackError("You can't attack to your aim!")
        
        return inner_wrapper    
    return wrapper
