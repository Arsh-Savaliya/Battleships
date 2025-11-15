class ship:
    def __init__(self,name,size):  # all info of a specific ship
        self.name = name
        self.size = size  #(4/3/3/2)
        self.coord = []
        self.hits = 0

    def is_hit(self,row,col): #checks if the coords given are of ship or not
        if (row,col) in self.coord:
            return True
    def is_miss(self,row,col):
        if (row,col) not in self.coord:
            return True
    
    def Hit(self): #keeps check of how many blocks of ships are hit
        self.hits+=1

    def sunkShip(self): # keeps check of a ship is sunk or not
        return self.hits>=self.size

def fleet():  # creats the fleet of 4 ships of different size for a player
    ship1 = ship("a",4)
    ship2 = ship("b",3)
    ship3 = ship("c",3)
    ship4 = ship("d",2)