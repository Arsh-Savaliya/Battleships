from Board import Board
from ships import ship,fleet

class player:  #player class that keeps player data
    def __init__(self,name): # creats player object
        self.name = name
        self.Board = Board()
        self.ships = fleet()

    def place_ships(self):
        pass

    