from gameManager import gameManager

def main():
    print("=== Welcome to Battleships ===")
    # create the manager — it already asks for player names
    gm = gameManager()

    # start the battle
    gm.play_game()

if __name__ == "__main__":
    main() 