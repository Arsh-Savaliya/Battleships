from Board import Board
from ships import ship,fleet
# from gameManager import gameManager

class player:  #player class that keeps player data
    def __init__(self,name): # creats player object
        self.name = name
        self.Board = Board()
        self.ships = fleet()      

    def get_ship_coords(self,name,size): 
        # takes coords of ships and validates them
        while True:
            start = tuple(map(int,input("Enter starting coords as 1 2 for (1,2): ").split()))  #starting coords
            print(f"Keep in mind that ship size is {self.size}")
            ending = tuple(map(int,input("Enter ending coords as 1 5 for (1.5): ").split()))   #ending coords
            if (start[0]!=ending[0]) ^ (start[1]!=ending[1]):   #checks if ships is either vertical or horizontal and covers more than 1 block
                 print("Keep in mind that ship can be either vertical or horizontal")
                 continue
                 
            if (len(start) != 2) or (len(ending) != 2):  #checks if user has given only 2 nums for coords
                print("Please enter only two numbers")
                continue
            
            if (start[0] == ending[0]):   #checks if the given coords alligns with ship size
                 if (abs(start[1]-ending[0]) != size):
                      print(f"Keep in mind that ship is of size {size}")
                 coords = [(start[0],y) for y in range(start[1],ending[1]+1)]
            elif (start[1]== ending[1]):
                 coords = [(x,start[1]) for x in range(start[0],ending[0]+1)]
            if not Board.validShipPlace(self.name,coords):
                 continue
        return coords    

    def place_ships(self):
            print(f"its now {self.name}'s turn to place ship")
            self.Board.display_board()

            for s in self.ships:
                 placed = False
                 while not placed:
                    print(f"first place ship {s.name} of size {s.size}")
                    self.Board.display_board()

                    coords = self.get_ship_coords(s.size)
                    s.place(coords)
                    self.Board.display_ship(coords)
                    placed = True
                 print()
            print("your final board is: ")
            self.Board.display_board

    def attack(self): #takes attack coords and attacks
         while True:
              attack_r,attack_c = input("Enter only 2 coords separated by space to attack (row,col)").split()

              if not (isinstance(attack_c,int) or isinstance(attack_r,int)):
                   continue
              if not self.Board.is_valid_position(attack_r,attack_c):
                   print("Coords must be betwwn 0 and 9")
                   continue
              return attack_r,attack_c