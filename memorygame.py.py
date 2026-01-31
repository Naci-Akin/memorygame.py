import random

def play_game():
    """
    Main function to run the number guessing game.
    Computer selects a random number between 0-100,
    and the player has 5 attempts to guess it.
    """
    
    # Computer randomly selects a number between 0 and 100
    secret_number = random.randint(0, 100)
    attempts = 5
    guessed = False
    
    # Display welcome message
    print("=" * 50)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")
    print("=" * 50)
    print(f"\nI'm thinking of a number between 0 and 100.")
    print(f"You have {attempts} attempts to guess it.")
    print("Good luck!\n")
    
    # Main game loop - continue until user wins or runs out of attempts
    while attempts > 0 and not guessed:
        try:
            # Get user's guess
            guess = int(input(f"Attempt {6 - attempts}/5 - Enter your guess: "))
            
            # Validate input is within range
            if guess < 0 or guess > 100:
                print("❌ Please enter a number between 0 and 100.\n")
                continue
            
            # Check if guess is correct
            if guess == secret_number:
                guessed = True
                print("\n" + "=" * 50)
                print("🎉 CONGRATULATIONS! YOU WIN! 🎉")
                print("=" * 50)
                print(f"You guessed the correct number: {secret_number}")
                print(f"You won in {6 - attempts} attempt(s)!\n")
            
            # Provide hint if guess is incorrect
            else:
                attempts -= 1
                if guess < secret_number:
                    print(f"❌ Too low! The number is higher than {guess}.")
                else:
                    print(f"❌ Too high! The number is lower than {guess}.")
                
                # Display remaining attempts
                if attempts > 0:
                    print(f"💡 You have {attempts} attempt(s) left.\n")
        
        except ValueError:
            # Handle invalid input (non-integer)
            print("❌ Invalid input! Please enter a valid integer.\n")
            continue
    
    # Handle game loss
    if not guessed:
        print("\n" + "=" * 50)
        print("😔 GAME OVER - YOU LOST! 😔")
        print("=" * 50)
        print(f"The secret number was: {secret_number}")
        print("Better luck next time!\n")


def main():
    """
    Main entry point that allows the player to play multiple rounds.
    """
    play_again = True
    
    while play_again:
        play_game()
        
        # Ask if user wants to play again
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        play_again = response in ['yes', 'y']
        print()
    
    print("=" * 50)
    print("Thanks for playing! Goodbye! 👋")
    print("=" * 50)


if __name__ == "__main__":
    main()