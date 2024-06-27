import random

def get_computer_choice():
    """Randomly select between 'rock', 'paper', and 'scissors' for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    """Get the player's choice and validate it."""
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(player, computer):
    """Determine the winner based on the choices of the player and the computer."""
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
