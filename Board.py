class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = self.create_empty_board()

    ## Creating empty boards
    def create_empty_board(self):
        return [["~" for _ in range(self.size)] for _ in range(self.size)]
    
    def display_board(self):
        print(self.grid)

    def display_ship(self,x1,y1,x2,y2):
        ## making x1>x2 and y1>y1
        if(x2 > x1):
            t = x1
            x1 = x2
            x2 = t
        
        elif(y2>y1):
            t = y1
            y1 = y2
            y2 = t

        ## placing ship
        if(y1 == y2):
            for i in range(x1,x2+1):
                self.grid[i][y1] = "@"
        
        else:
            for i in range(y1,y2+1):
                self.grid[x1][i] = "@"

        print(self.grid)

        #----------X---------------X------------X--------X

    ## target coords
    def is_valid_position(x,y):
        if(x>0 and x<=10 and y>0 and y<=10):
            return True
        else:
            return False

    def check_target(self,x,y):
        if(self.grid[x][y] == "@"): return True
        else: return False

    def display_hit_miss(self,x,y):
        r1 = Board.is_valid_position(x,y)
        if(r1 == True):
            r2 = Board.check_target(x,y)
            if(r2 == True):
                self.grid[x][y] = "!"
                print(self.grid)
            else:        ########## r2 is false
                self.grid[x][y] = "M"
                print(self.grid)
        else:           ####### r1 is false
            r = "Not a valid position."
            return r





        




# SYMBOLS
# ~ => water
# @ => ship
# ! => hit
# M => miss