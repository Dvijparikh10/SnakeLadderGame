import random

# Define snakes and ladders as dictionaries
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to check for snakes or ladders
def check_snake_or_ladder(position):
    if position in snakes:
        print(f"Oops! You got bitten by a snake. You move from {position} to {snakes[position]}.")
        return snakes[position]
    elif position in ladders:
        print(f"Yay! You climbed a ladder. You move from {position} to {ladders[position]}.")
        return ladders[position]
    else:
        return position

# Function to play the game
def play_game():
    player1_position = 0
    player2_position = 0
    current_player = 1

    while True:
        input(f"Player {current_player}, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"Player {current_player} rolled a {dice_value}.")

        if current_player == 1:
            player1_position += dice_value
            player1_position = check_snake_or_ladder(player1_position)
            print(f"Player 1 is now at position {player1_position}.")
            if player1_position >= 100:
                print("Player 1 wins!")
                break
        else:
            player2_position += dice_value
            player2_position = check_snake_or_ladder(player2_position)
            print(f"Player 2 is now at position {player2_position}.")
            if player2_position >= 100:
                print("Player 2 wins!")
                break

        # Switch players
        current_player = 2 if current_player == 1 else 1

# Start the game
print("Welcome to Snake and Ladder!")
play_game()