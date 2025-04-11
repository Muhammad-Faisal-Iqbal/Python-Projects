import random

MAX_ATTEMPTS = 5
SCORE_DECREMENT = 100

# Function to get valid range
def get_valid_range():
    while True:
        try:
            min_n, max_n =  input("Enter a range of number Separated by comma like (1,100): ").strip().split(",")
            min_n, max_n = int(min_n), int(max_n)
            # check that min alwaye less than max
            if min_n > max_n:
                print("Minimum number alwaye be less than Maximum number not like this (min:100,max:1)")
                continue
            return min_n, max_n
        except ValueError:
            print("Invalid Input! Pelase enter 2 number separated by comma like (1, 100)")

# Function to get number that user guess
def get_guess(min_n, max_n):
    while True:
        try:
            return int(input(f"Enter a number to guess b/w {min_n} to {max_n}: "))
        
        except ValueError:
            print("Invalid input! Please enter a valid integer number.")

# Main function that hundle all functionality
def main():

    min_n, max_n = get_valid_range()
    number_to_guess = random.randint(min_n, max_n)
    attempts = 1
    score = 100
    while True:

        if attempts > MAX_ATTEMPTS:
            print(f"You lost! The correct number was {number_to_guess}.")
            break
        guess = get_guess(min_n, max_n)

        if guess > number_to_guess:
            print(f"Too high! You have {MAX_ATTEMPTS - attempts} attempts left.")
            score -= SCORE_DECREMENT
            attempts += 1
        elif guess < number_to_guess:
            print(f"Too low! You have {MAX_ATTEMPTS - attempts} attempts left.")
            score -= SCORE_DECREMENT
            attempts += 1
        else:
            print(f"Congratulation! You guessed the number in {attempts} attempts.")
            print("You are score is:",score)
            break

if __name__ == "__main__":
    main()