from ships import ship, fleet   
from colorama import init,Fore,Style,Back 

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = self.create_empty_board()
        # self.attackGrid = self.create_empty_board()

    ## Creating empty boards
    def create_empty_board(self):
        return [["~" for _ in range(self.size)] for _ in range(self.size)]
    
    #displays the current state of
    def display_board(self):
        # header 
        header = "   " + " ".join(f"{c:2}" for c in range(self.size))
        print(header)
        for r in range(self.size):
            row_str = " ".join(f"{self.grid[r][c]:2}" for c in range(self.size))
            print(f"{r:2} {row_str}")
        print()
    
    def attack_board(self):
        header = "   " + " ".join(f"{c:2}" for c in range(self.size))
        print(header)
        for r in range(self.size):
            rowDis = []
            for c in range(self.size):
                block = self.grid[r][c]

                # If it's a ship symbol, hide it as water
                if block in ("@", Fore.BLUE + "@ " + Style.RESET_ALL):
                    rowDis.append("~ ")
                else:
                    # Ensure 2-char alignment
                    rowDis.append(f"{block:2}")

            print(f"{r:2} " + " ".join(rowDis))
        print()

    #         row_str = " ".join(f"{self.attackGrid[r][c]:2}" for c in range(self.size))
    #         print(f"{r:2} {row_str}")
    #     print()


    def display_ship(self,coords):
        # # changing coordinates so x1<=x2 and y1<=y2
        # if x2 < x1:
        #     x1, x2 = x2, x1
        # if y2 < y1:
        #     y1, y2 = y2, y1

        # # checking (horizontal or vertical)
        # if y1 == y2:
        #     for i in range(x1, x2+1):
        #         self.grid[i][y1] = "@"
        # else:
        #     for i in range(y1, y2+1):
        #         self.grid[x1][i] = "@"

        for x,y in coords:
            self.grid[x][y]= Fore.BLUE+"@ "+Style.RESET_ALL

        self.display_board()

    def is_valid_position(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def check_target(self, x, y):
        if not self.is_valid_position(x, y):
            return False
        return self.grid[x][y] in ("@", Fore.BLUE+"@ "+Style.RESET_ALL)

    def display_hit_miss(self, x, y):
        if not self.is_valid_position(x, y):
            print(Fore.RED + "! Not a valid position. !" + Style.RESET_ALL)
            return False  # invalid move

        current = self.grid[x][y]

        # Cells that have already been attacked or sunk
        already_marks = (
            Fore.RED + "! " + Style.RESET_ALL,    # hit
            Fore.GREEN + "M " + Style.RESET_ALL,  # miss
            Fore.YELLOW + "S " + Style.RESET_ALL  # sunk ship
        )

        # If this spot was already processed before, don't change it
        if current in already_marks:
            print(Fore.YELLOW + "You already attacked this spot!" + Style.RESET_ALL)
            self.display_board()
            return None  # special: no change

        # Fresh hit on a ship
        if current in ("@", Fore.BLUE + "@ " + Style.RESET_ALL):
            self.grid[x][y] = Fore.RED + "! " + Style.RESET_ALL
            self.display_board()
            return True   # hit

        # Otherwise, it's water -> miss
        self.grid[x][y] = Fore.GREEN + "M " + Style.RESET_ALL
        self.display_board()
        return False      # miss



    def sunkShip(self,coords):
        for x, y in coords:
            self.grid[x][y] = Fore.YELLOW + "S " + Style.RESET_ALL

    def validShipPlace(self, coords):  # checks if the ship placement is valid or not
        for x, y in coords:
            if not self.is_valid_position(x, y):  # checks inside board
                print("given coords are out of board")
                return False
            
            if self.grid[x][y] in ("@", Fore.BLUE + "@ " + Style.RESET_ALL):
                print("invalid positioning. ship clashes with other ship")
                return False
        return True
