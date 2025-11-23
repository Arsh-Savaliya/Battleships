import os
import time
from gameManager import gameManager
from colorama import Fore,init,Back,Style

def main():

    WelcomHeading = """░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░       ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓████████▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓██████▓▒░         ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░                    ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░                    ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓████████▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  
                                                                                                                                                
                                                                                                                                                """

    Thanks = """░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░    ░▒▓██████▓▒░ ░▒▓██████▓▒░  
                                                                                                                 
                                                                                                                 """
   
   
   
    print(Fore.RED + WelcomHeading +Style.RESET_ALL)

    print(Fore.RED + "------------------------------------------------------------------------------------------------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.MAGENTA)
    print("1. New Game")
    print("2. Load Game")
    print("3. Rules")
    print("4. Exit")
    print(Style.RESET_ALL)
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    
    
    while True: 
        n = input("Enter 1,2,3,4 according to what you wanna do: ")

        if n=="1":
            os.system('cls' if os.name == 'nt' else 'clear')
            gm = gameManager()
            gm.clear_scrn()
            winner = gm.play_game()
            gm.clear_scrn()
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
            print()
            print(Fore.RED +  Thanks + Style.RESET_ALL) 

            break

        elif n == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            gm = gameManager(loading=True)

            from fileManager import load_game

            if load_game(gm):
                gm.play_game()
            else:
                print("Starting a NEW game instead.")
                gm = gameManager()
                gm.play_game()

            break

        elif n == "3":
            rules()

        elif n=="4":
            break
       
        
        else:
            print(Fore.RED + "INVALID INPUT " + Style.RESET_ALL + "please give a valid input")
            continue


def rules():
    print(Fore.CYAN + "\n GAME RULES — BATTLESHIPS\n" + Style.RESET_ALL)

    print("Goal:")
    print(" • Destroy all enemy ships before they destroy yours.")
    
    print("\nBoard:")
    print(" • 10 × 10 grid (rows & columns numbered 0–9)")
    print(" • Ships are hidden from the opponent’s view")

    print("\nShip Fleet:")
    print(" • Aircraft Carrier  → size 5")
    print(" • Battleship        → size 4")
    print(" • Submarine         → size 3")
    print(" • Cruiser           → size 3")
    print(" • Destroyer         → size 2")

    print("\nTurns & Attacks:")
    print(" • Players take turns firing at enemy coordinates")
    print(" • You input a row & column: example → 2 6")
    print(" • HIT → you get another turn")
    print(" • MISS → opponent’s turn")
    print(" • Re-hitting the same tile = hit again")

    print("\nWinning Condition:")
    print(" • You win when ALL enemy ships are sunk!")

    print(Fore.CYAN + "\n Board Symbols and Their Meaning\n" + Style.RESET_ALL)
    print(" ~  → Unknown water (not attacked yet)")
    print(Fore.GREEN + " M " + Style.RESET_ALL + "→ Missed shot")
    print(Fore.RED + " ! " + Style.RESET_ALL + "→ Direct hit on ship")
    print(Fore.YELLOW + " S " + Style.RESET_ALL + "→ Ship segment completely sunk")
    print(Fore.BLUE + " @ " + Style.RESET_ALL + "→ Your ship location")

    print("\nTips:")
    print(" • Shoot logically — track patterns")
    print(" • Think where longer ships might fit")
    print(" • Use confirmed hits to hunt the remaining parts of that ship")
    print("\nGood luck, Commander! ⚓🔥")

    input("\nPress Enter to return to menu... ")
    os.system('cls' if os.name == 'nt' else 'clear')
    


if __name__ == "__main__":
    main()