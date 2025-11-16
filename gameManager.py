import random

from Board import Board
from ships import ship,fleet
from player import player

class gameManager:
    def __init__(self,p1,p2):  # makes two player objects (handles extra spaces)
        self.player1 = player(input("Enter name of PLayer 1: ").strip())
        self.player2 = player(input("Enter name of player 2: ").strip())
    
    def place_ships_randomly(self):
        print(f"\nPlacing ships randomly for {self.name}...")

        for s in self.ships:
            size = s.size

            placed = False
            while not placed:
                # choose orientation
                orientation = random.choice(["H", "V"])

                if orientation == "H":
                    x = random.randint(0, self.Board.size - 1)
                    y = random.randint(0, self.Board.size - size)
                    coords = [(x, y + i) for i in range(size)]
                else:
                    x = random.randint(0, self.Board.size - size)
                    y = random.randint(0, self.Board.size - 1)
                    coords = [(x + i, y) for i in range(size)]

                # check board validity
                if not self.Board.validShipPlace(coords):
                    continue

                # place on board
                for (a, b) in coords:
                    self.Board.grid[a][b] = "@"

                s.coord = coords
                placed = True

        print(f"Ships placed for {self.name}.")
        self.Board.display_board()