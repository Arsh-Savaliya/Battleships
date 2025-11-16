import random

from Board import Board
from ships import ship,fleet
from player import player

class gameManager:
    def __init__(self,p1,p2):  # makes two player objects (handles extra spaces)
        self.player1 = player(input("Enter name of PLayer 1: ").strip())
        self.player2 = player(input("Enter name of player 2: ").strip())

    def get_ship_coords(self,name,size):
        while True:
            start = tuple(map(int,input("Enter starting coords as 1 2 for (1,2): ").split()))
            print(f"Keep in mind that ship size is {self.size}")
            ending = tuple(map(int,input("Enter ending coords as 1 5 for (1.5): ").split()))
            if (start[0]!=ending[0]) ^ (start[1]!=ending[1]):
                 print("Keep in mind that ship can be either vertical or horizontal")
                 continue
                 
            if (len(start) != 2) or (len(ending) != 2):
                print("Please enter only two numbers")
                continue
            
            if (start[0] == ending[0]):
                 if (abs(start[1]-ending[0]) != size):
                      print(f"Keep in mind that ship is of size {size}")
                 coords = [(start[0],y) for y in range(start[1],ending[1]+1)]
            elif (start[1]== ending[1]):
                 coords = [(x,start[1]) for x in range(start[0],ending[0]+1)]
            if not Board.validShipPlace(self.name,coords):
                 continue
        return coords
    
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