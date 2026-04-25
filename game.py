import random

def play_game():
    while True:   # 🔥 LOOP START
        print("\n🎮 Stone Paper Scissors")

        choices = {1: "Stone", 2: "Paper", 3: "Scissors"}

        print("1. Stone")
        print("2. Paper")
        print("3. Scissors")

        user = int(input("Enter your choice: "))
        computer = random.randint(1, 3)

        print(f"You chose: {choices[user]}")
        print(f"Computer chose: {choices[computer]}")

        if user == computer:
            print("It's a draw")

        elif (
            (user == 1 and computer == 3) or
            (user == 2 and computer == 1) or
            (user == 3 and computer == 2)
        ):
            print("You win!")
        else:
            print("Computer wins!")

        # if user not want to see the option for again ask play or exit so we add a new option 
        '''again = input("Play again? (y/n): ").lower()

        if again != 'y':
            break''' 