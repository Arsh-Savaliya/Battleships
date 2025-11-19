from newboard import Board
from ships import ship,fleet
# from gameManager import gameManager

class player:  #player class that keeps player data
    def __init__(self,name): # creats player object
        self.name = name
        self.Board = Board()
        self.ships = fleet()      

    def get_ship_coords(self,size): 
        # takes coords of ships and validates them
        while True:
            try:
               start = tuple(map(int,input("Enter starting coords as 1 2 for (1,2): ").split()))  #starting coords
               print(f"Keep in mind that ship size is {size}")
               ending = tuple(map(int,input("Enter ending coords as 1 5 for (1,5): ").split()))   #ending coords
            except:
                 print("Enter 2 inegers spaced by one blank")
                 continue
            
            if not ((start[0] == ending[0] or start[1] == ending[1]) and (start != ending)):   #checks if ships is either vertical or horizontal and covers more than 1 block
                 print("Keep in mind that ship can be either vertical or horizontal")
                 continue
                 
            if (len(start) != 2) or (len(ending) != 2):  #checks if user has given only 2 nums for coords
                print("Please enter only two numbers")
                continue
            
            if start[0] == ending[0]:   #checks if the given coords alligns with ship size
                 if (abs(start[1]-ending[1])+1 != size):
                      print(f"Keep in mind that ship is of size {size}")
                 coords = [(start[0],y) for y in range(min(start[1],ending[1]),max(start[1],ending[1]) +1)]
            elif (start[1]== ending[1]):
                 coords = [(x,start[1]) for x in range(start[0],ending[0]+1)]
            if not self.Board.validShipPlace(coords):
                 continue
            return coords    

    def place_ships(self): #handle manual placement of ship
            print(f"its now {self.name}'s turn to place ship")
            self.Board.display_board()

            for s in self.ships:
                 flag = False
                 while not flag:
                    self.Board.display_board()
                    print(f"place ship {s.name} of size {s.size}")

                    coords = self.get_ship_coords(s.size)
                    s.place(coords)
                    self.Board.display_ship(coords)
                    flag = True
                 print()
            print("your final board is: ")
            self.Board.display_board()

    def attack(self): #takes attack coords and attacks
         while True:
               try:
                    attack_r,attack_c = map(int,input("Enter only 2 coords separated by space to attack (row,col)").split())
               except:
                    print("please give only 2 numbers for coords separated by space.")
                    print("Example : you wanna attack (1,2) type 1 2")
                    continue
                   
     #          attack_r,attack_c = map(int,input("Enter only 2 coords separated by space to attack (row,col)").split())

     #      #     if not (isinstance(attack_c,int) or isinstance(attack_r,int)):
     #      #          continue
     #          if not self.Board.is_valid_position(attack_r,attack_c):
     #               print("Coords must be betwwn 0 and 9")
     #               continue
               return attack_r,attack_c