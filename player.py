from Board import Board
from ships import ship,fleet

class player:  #player class that keeps player data
    def __init__(self,name): # creats player object
        self.name = name
        self.Board = Board()
        self.ships = fleet()

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
            

    def place_ships(self):
            print(f"its now {self.name}'s turn to place ship")
            self.Board.display_board()

            for s in self.ships:
                 placed = False
                 while not placed: