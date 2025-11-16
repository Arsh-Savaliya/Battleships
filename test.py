from player import player

p = player("Tst")
p.Board.display_board()   # should print a 10x10 grid with indices

# place a ship manually on board grid (0-based coords)
p.Board.display_ship(0,0,0,3)   # a horizontal ship length 4 at row 0, cols 0..3

# test hit/miss
p.Board.display_hit_miss(0,0)   # should mark "!" and reprint
p.Board.display_hit_miss(5,5)   # should mark "M" and reprint
