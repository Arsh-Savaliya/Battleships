class ship:
    def __init__(self,name,size):  # all info of a specific ship
        self.name = name
        self.size = size  #(4/3/3/2)
        self.coord = []
        self.hits = 0

    def place(self,coords):  #takes starting coords and ending coords
        # Calculate expected length based on input coordinates
        if len(coords) != self.size:
            print(f"Error: Ship {self.name} must be size {self.size}, but got {len(coords)} cells.")
            return 
        self.coord = coords
 
    def is_hit(self,row,col): #checks if the coords given are of ship or not
        if (row,col) in self.coord:
            return True
        return False
    
    def Hit(self): #keeps check of how many blocks of ships are hit
        self.hits+=1

    def sunkShip(self): # keeps check of a ship is sunk or not
        return self.hits>=self.size

def fleet():  # creats the fleet of 4 ships of different size for a player
    ship1 = ship("Aircraft Carrier",5)
    ship2 = ship("battleship",4)
    ship3 = ship("Submarine",3)
    ship4 = ship("Cruiser",3)
    ship5 = ship("Destroyer",2)
    armada = [ship1,ship2,ship3,ship4,ship5]
    return armada 