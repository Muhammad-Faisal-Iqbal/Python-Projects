ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'


emojis = {ROCK: '✊', PAPER: '📄', SCISSOR: '✂'}
choices = tuple(emojis.keys())

user1_name = input("Player1: What's your name? ")
user2_name = input("Player2: What's your name? ") 


def get_game_settings():
    while True:
        try:
            best_of_rounds = int(input("Enter 'Best of' rounds (e.g. 3, 5, 7): "))
            if best_of_rounds % 2 == 1 and best_of_rounds > 0:
                required_wins = (best_of_rounds // 2) + 1
                print(f"First to {required_wins} wins take the match!")
                return required_wins       
            print("Error: Must be a positive odd number.")

        except ValueError:
            print("Invalid input! Please enter valid positive odd number.")

# Function to get choice as input ✊, 📄, ✂

def get_user_choice(player_name):    
    while True:
        user_choice = input(f"{player_name}: Rock, paper, or Scissors? (r/p/s): ").strip().lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choice(user1_choice, user2_choice):      
    print(f"{user1_name} chose: {emojis[user1_choice]}")
    print(f"{user2_name} chose: {emojis[user2_choice]}")

# Function to dicide who win 
def determine_winner(user1_choice, user2_choice, scores):

    if user1_choice == user2_choice:
        scores["ties"] += 1
        print("⚖ It's a tie!")
    elif (
        (user1_choice == ROCK and user2_choice == PAPER) or
        (user1_choice == PAPER and user2_choice == SCISSOR) or
        (user1_choice == SCISSOR and user2_choice == ROCK)
        ):        
        scores["user2"] += 1
        print(f"✅ {user2_name} win this round!")
    else:
        scores["user1"] += 1
        print(f"✅ {user1_name} win this round!")

def display_scores(scores):
    print("\nCurrent Score:")
    print(f"{user1_name}: {scores["user1"]} | {user2_name}: {scores["user2"]} | Ties: {scores["ties"]}\n")

def display_final_score(scores):
        print(f"\n🏁 Final Game Summary")
        print(f"{user1_name}: {scores["user1"]}")
        print(f"{user2_name}: {scores["user2"]}")
        print(f"Ties with {user2_name}: {scores["ties"]}")
        if scores["user1"] > scores["user2"]:
            print(f"🎉 {user1_name} is the overall winner!")
        elif scores["user2"] > scores["user1"]:
            print(f"🎉 {user2_name} is the overall winner!")
        else:
            print("It's a tie overall!")

def ask_to_continue():
    while True:
        shall_continue = input("Continue? (y/n): ")
        if shall_continue == "y":
            return True
        elif shall_continue == "n":
            return False
        print("Invalid input! Please enter 'y' for continue or 'n' for quit.")

def play_round(scores):
    user1_choice = get_user_choice(user1_name)
    user2_choice = get_user_choice(user2_name)

    display_choice(user1_choice, user2_choice)
    determine_winner(user1_choice, user2_choice, scores)
    display_scores(scores)


# Main function
def play_game():
    while True:
        scores = {"user1": 0, "user2": 0, "ties": 0}
        required_wins = get_game_settings()

        while True:
            if scores["user1"] == required_wins or scores["user2"] == required_wins or scores["ties"] == required_wins:
                break
            play_round(scores)
        
        display_final_score(scores)
        if not ask_to_continue():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()