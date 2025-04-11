import sys
import random

MIN_DICE = 1
MAX_DICE = 5
DICE_SIDE = 6

def get_user_choice():
    while True:
        choice = input("Roll the dice? (y/n): ")
        if choice in ['y', 'n']:
            return choice
        print("Invalid choice! Please enter 'y' or 'n'.")

def rolling_dice():
    while True:
        try:
            dices_count = int(input(f"How many dice you want to roll? ({MIN_DICE}-{MAX_DICE}): "))
            if 0 <= dices_count  <= 5:
                break
            else:
                print(f"Enter a number b/w {MIN_DICE} and {MAX_DICE}")
        except ValueError:
            print("Invalid input please enter a valid number.")
    
    dices_nums = [random.randint(1, DICE_SIDE) for _ in range(dices_count)]
    
    return dices_nums

def main():

    counter = 0

    while True:
        # Ask the user that he want to roll the dice are not 
        choice = get_user_choice()

        if choice == "y":
            counter += 1 
            dices_nums = rolling_dice()
            print(tuple(dices_nums))
            print("Times you rolled the dice:", counter)
            
        elif choice == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()