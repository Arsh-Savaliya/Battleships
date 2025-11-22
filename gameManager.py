import random
import os
import time
from colorama import Fore,init,Back,Style

from newboard import Board
from ships import ship,fleet
from player import player

class gameManager:
    def __init__(self):  # makes two player objects (handles extra spaces)
        self.player1 = player(input("Enter name of PLayer 1: ").strip())
        self.player2 = player(input("Enter name of player 2: ").strip())
        self.currPlayer = self.player1
        self.oppPlayer = self.player2

        print("Now lets us begin game between you two")

    # def get_ship_coords(self,size): 
    #     # takes coords of ships and validates them
    #     while True:
    #         start = tuple(map(int,input("Enter starting coords as 1 2 for (1,2): ").split()))  #starting coords
    #         print(f"Keep in mind that ship size is {self.size}")
    #         ending = tuple(map(int,input("Enter ending coords as 1 5 for (1.5): ").split()))   #ending coords
    #         if (start[0]!=ending[0]) ^ (start[1]!=ending[1]):   #checks if ships is either vertical or horizontal and covers more than 1 block
    #              print("Keep in mind that ship can be either vertical or horizontal")
    #              continue
                 
    #         if (len(start) != 2) or (len(ending) != 2):  #checks if user has given only 2 nums for coords
    #             print("Please enter only two numbers")
    #             continue
            
    #         if (start[0] == ending[0]):   #checks if the given coords alligns with ship size
    #              if (abs(start[1]-ending[0]) != size):
    #                   print(f"Keep in mind that ship is of size {size}")
    #              coords = [(start[0],y) for y in range(start[1],ending[1]+1)]
    #         elif (start[1]== ending[1]):
    #              coords = [(x,start[1]) for x in range(start[0],ending[0]+1)]
    #         if not Board.validShipPlace(self.name,coords):
    #              continue
    #     return coords
    
    def place_ships_randomly(self,player):  #random ship placement mechanism
        print(f"\nPlacing ships randomly for {self.currPlayer.name}...")

        for s in self.currPlayer.ships:
            size = s.size

            placed = False
            while not placed:
                # choose orientation
                orientation = random.choice(["H", "V"])

                if orientation == "H":
                    x = random.randint(0, self.currPlayer.Board.size - 1)
                    y = random.randint(0, self.currPlayer.Board.size - size)
                    coords = [(x, y + i) for i in range(size)]
                else:
                    x = random.randint(0, self.currPlayer.Board.size - size)
                    y = random.randint(0, self.currPlayer.Board.size - 1)
                    coords = [(x + i, y) for i in range(size)]

                # check board validity
                if not self.currPlayer.Board.validShipPlace(coords):
                    continue

                # place on board
                for (a, b) in coords:
                    self.currPlayer.Board.grid[a][b] = Fore.BLUE + "@ " + Style.RESET_ALL

                s.coord = coords
                placed = True

        print(f"Ships placed for {self.currPlayer.name}.")  
        self.currPlayer.Board.display_board()

    def swap(self):
        self.currPlayer,self.oppPlayer = self.oppPlayer,self.currPlayer
    
    def turns(self):
        r,c = self.currPlayer.get_ship_coords()

    def check_attack(self,r,c):
        current = self.oppPlayer.Board.grid[r][c]

    # If spot already attacked, don't count it
        if current in (
            Fore.RED + "! " + Style.RESET_ALL,   # already hit
            Fore.GREEN + "M " + Style.RESET_ALL, # already miss
            Fore.YELLOW + "S " + Style.RESET_ALL # already sunk
        ):
            print(Fore.YELLOW + "You already attacked here!" + Style.RESET_ALL)
            n = input("Press Enter to hit again")
            return True
        HitShip = False #flag of hitting a ship
        for i in self.oppPlayer.ships:
            if i.is_hit(r,c):
                if current in (Fore.RED + "! " + Style.RESET_ALL, Fore.YELLOW + "S " + Style.RESET_ALL):
                     # Already hit before — do nothing further
                    return None
                i.Hit()
                print(Fore.RED + "YAY!! that was a hit" + Style.RESET_ALL)
                # n = input("Press Enter to Hit again")

                if i.sunkShip():
                    print(Fore.YELLOW + "CRAZY you sunk a ship!")
                    self.oppPlayer.Board.sunkShip(i.coord)
                    # n = input("Press Enter to Hit again")
                HitShip = True
                break
        if not HitShip:
            print("OOH!! that was a miss")
            # n = input("Press Enter to giv turn to opponent")
        
        return HitShip
    
    def Victory_logic(self):
        all_sunk = all(s.sunkShip() for s in self.oppPlayer.ships)
        return all_sunk
    
    def play_game(self):
        choice = input("Choose M to manualy place ships and R to randomly: ").upper()
        if choice == "M":
             print("\nManual placement chosen for BOTH players.\n")
             time.sleep(1)
             self.player1.place_ships()
             self.player2.place_ships()

        if choice == "R":
            print("Random placement chosen for both players")
            self.place_ships_randomly(self.currPlayer)
            go_ahead = input("Press Enter to continue")
            self.clear_scrn()
            self.swap()
            self.place_ships_randomly(self.currPlayer)
            go_ahead = input("Press Enter to continue")

        while True:
            self.clear_scrn()
            
            print(f"its {self.currPlayer.name}'s turn to attack")
            print()
            self.currPlayer.Board.attack_board()
            print("Current State of your board is this \u2191")
            print()

            self.oppPlayer.Board.attack_board()
            print(f"{self.oppPlayer.name}'s board \u2191." + " (~ Water, M miss, ! partialy sunked ship, X completly sunken ship)")
            print()
            
            attack_r, attack_c = self.currPlayer.attack()
            hit = self.check_attack(attack_r,attack_c)
            self.oppPlayer.Board.display_hit_miss(attack_r,attack_c)

            if self.Victory_logic():
                print(f"Congratulations, {self.currPlayer.name} wins ")
            if not hit:
                 self.swap()

    def clear_scrn(self):
        os.system('cls' if os.name == 'nt' else 'clear')