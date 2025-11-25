from colorama import Fore, Style

SAVE_FILE = "savegame.txt"

def clean_cell(cell): #converts coloured symbols back normal
    if "@ " in cell:
        return "@"
    if "!" in cell:
        return "!"
    if "M" in cell:
        return "M"
    if "S" in cell:
        return "S"
    return "~"

def save_game(gm):  #this function helps save game
    try: 
        with open(SAVE_FILE, "w") as f:
            # Save whose turn
            f.write(gm.currPlayer.name + "\n")

            # Save Player1 board
            for row in gm.player1.Board.grid:
                line = "".join(clean_cell(c) for c in row)
                f.write(line + "\n")

            f.write("===\n")  # separator

            # Save Player2 board
            for row in gm.player2.Board.grid:
                line = "".join(clean_cell(c) for c in row)
                f.write(line + "\n")

        print("Game saved successfully ✔")

    except:
        print("Error saving game:")


def load_game(gm): #loads the previously loaded game
    try:
        with open(SAVE_FILE, "r") as f:
            lines = f.read().splitlines()

        current_name = lines[0]
        sep = lines.index("===")

        p1 = lines[1:sep]
        p2 = lines[sep + 1:]

        def restore_board(lines, board):
            for r in range(len(lines)):
                for c, ch in enumerate(lines[r]):
                    if ch == "@":
                        board.grid[r][c] = Fore.BLUE + "@ " + Style.RESET_ALL
                    elif ch == "!":
                        board.grid[r][c] = Fore.RED + "! " + Style.RESET_ALL
                    elif ch == "M":
                        board.grid[r][c] = Fore.GREEN + "M " + Style.RESET_ALL
                    elif ch == "S":
                        board.grid[r][c] = Fore.YELLOW + "S " + Style.RESET_ALL
        
        gm.player1.Board.grid = gm.player1.Board.create_empty_board()
        gm.player2.Board.grid = gm.player2.Board.create_empty_board()


        restore_board(p1, gm.player1.Board)
        restore_board(p2, gm.player2.Board)

        # Restore correct turn
        gm.currPlayer = gm.player1 if gm.player1.name == current_name else gm.player2
        gm.oppPlayer = gm.player2 if gm.currPlayer == gm.player1 else gm.player1

        print("Game loaded successfully ✔")
        return True

    except:
        print("No save file found")
        return False
