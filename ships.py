class ship:
    def __init__(self,name,size):  # all info of a specific ship
        self.name = name
        self.size = size  #(4/3/3/2)
        self.coord = []
        self.hits = 0

    def place(self,x1,y1,x2,y2):  #takes starting coords and ending coords
        # Calculate expected length based on input coordinates
        self.coord = []
        length = 0
        if x1 == x2:
            length = abs(y2 - y1) + 1
        elif y1 == y2:
            length = abs(x2 - x1) + 1
            
        if length != self.size:
            print(f"Error: Ship {self.name} (size {self.size}) must span exactly {self.size} squares.")
            return # Exit if invalid size
        
        if x1==x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                self.coord.append((x1,i))
        if y1==y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                self.coord.append((i,y1))
 
    def is_hit(self,row,col): #checks if the coords given are of ship or not
        if (row,col) in self.coord:
            return True
        return False
    
    # def is_miss(self,row,col):
        # if (row,col) not in self.coord:
        #     return True
    
    def Hit(self): #keeps check of how many blocks of ships are hit
        self.hits+=1

    def sunkShip(self): # keeps check of a ship is sunk or not
        return self.hits>=self.size

def fleet():  # creats the fleet of 4 ships of different size for a player
    ship1 = ship("A",4)
    ship2 = ship("B",3)
    ship3 = ship("C",3)
    ship4 = ship("D",2)
    armada = [ship1,ship2,ship3,ship4]
    return armada