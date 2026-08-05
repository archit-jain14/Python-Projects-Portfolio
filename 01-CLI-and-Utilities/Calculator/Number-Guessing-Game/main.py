import random

def guessing_game():
    print("=" * 40)
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("=" * 40)
    print("I am thinking of a number between 1 and 100...")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("\nEnter your guess (1-100): "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("❌ Please enter a number strictly between 1 and 100!")
                continue

            if user_guess < secret_number:
                print("📉 Too Low! Try a higher number.")
            elif user_guess > secret_number:
                print("📈 Too High! Try a lower number.")
            else:
                print("\n" + "🎉" * 15)
                print(f" Congratulations! You guessed the number {secret_number} correctly!")
                print(f"🏆 Total Attempts: {attempts}")
                print("🎉" * 15)
                break

        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()