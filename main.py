from game import play_game

def main(): # main controller function
    while True: # infinity loop to create menu again and again, when case 2 come this loop stop 
        print("\nGame Menu")
        print("1. Play Game")
        print("2. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            play_game() # if user choose this this function is call to game.py part
        elif choice == 2:
            print("Thank you!")
            break
        else:
            print("Invalid choice")

main()