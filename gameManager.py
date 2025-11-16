import random

from Board import Board
from ships import ship,fleet
from player import player

class gameManager:
    def __init__(self):  # makes two player objects (handles extra spaces)
        self.player1 = player(input("Enter name of PLayer 1: ").strip())
        self.player2 = player(input("Enter name of player 2: ").strip())
        self.currPlayer = self.player1
        self.oppPlayer = self.player2

        print("Now lets us begin game betwee you two")

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
    
    def place_ships_randomly(self):  #random ship placement mechanism
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

    def swap(self):
        self.currPlayer,self.oppPlayer = self.oppPlayer,self.currPlayer
    
    def turns(self):
        r,c = self.currPlayer.get_ship_coords()

    def check_attack(self,r,c):
        HitShip = False #flag of hitting a ship
        for i in self.oppPlayer.ships:
            if i.is_hit():
                i.Hit()
                flag = True
                print(f"YAY!! that was a hit")

                if i.sunkShip():
                    print("CRAZY you sunk a ship")
                break
        if not HitShip:
            print("OOH!! that was a miss")
        
        return HitShip
    
    def Victory_logic(self):
        all_sunk = all(s.sunkShip() for s in self.oppPlayer.ships)
        return all_sunk
    
    def play_game(self):
        while True:
            print(f"its {self.currPlayer}'s turn to attack")
            print()
            print(f"{self.oppPlayer}'s board. (~ Water, M miss, ! partialy sunked ship, X completly sunken ship)")
            self.oppPlayer.Board.display_board
            attack_r, attack_c = self.currPlayer.attack()
            self.check_attack(attack_r,attack_c)

            if self.Victory_logic():
                print(f"{self.currPlayer} wins")
                break
            self.swap()