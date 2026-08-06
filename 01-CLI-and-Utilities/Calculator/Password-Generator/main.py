import random
import string


def generate_password(length=12, use_digits=True, use_symbols=True):
    # Base character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    # Combine all allowed characters
    all_characters = letters + digits + symbols

    if not all_characters:
        return "❌ Error: At least one character set must be selected!"

    # Ensure password contains at least one character from each selected set
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))

    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill the remaining length with random choices
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    # Shuffle to ensure randomness
    random.shuffle(password)

    return "".join(password)


def main():
    print("=" * 45)
    print("🔐 Welcome to the Random Password Generator! 🔐")
    print("=" * 45)

    try:
        length = int(
            input("Enter desired password length (minimum 6 characters): ")
        )
        if length < 6:
            print(
                "⚠️ Password length should be at least 6. Setting length to 6."
            )
            length = 6

        include_digits = (
            input("Include numbers? (y/n): ").strip().lower() == "y"
        )
        include_symbols = (
            input("Include special characters? (y/n): ").strip().lower() == "y"
        )

        password = generate_password(length, include_digits, include_symbols)

        print("\n" + "✨" * 20)
        print(f"🔑 Your Generated Password:  {password}")
        print("✨" * 20)

    except ValueError:
        print("❌ Invalid input! Please enter a valid number for length.")


if __name__ == "__main__":
    main()