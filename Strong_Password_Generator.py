# Strong Password Generator
# Adam Flick
# February 2025

import random
import string

def generate_strong_password(length=14):
    # Ensure at least one of each required type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest randomly from all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += [random.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle to prevent predictable patterns
    random.shuffle(password)

    return "".join(password)

#--------------
# Main Menu CLI
# -------------
def main_menu():
    print("\n--- Strong Password Generator ---")
    print("""
Welcome to the Strong Password Generator!

This program generates a strong password with:
- At least 14 characters
- A mix of uppercase, lowercase, numbers, and special characters""")
    user_choice = input("\nWould you like to generate a secure password? (yes/no): ").strip().lower()

    while user_choice == "yes":
        print("\nYour secure password is:", generate_strong_password())

        # Ask if they want another password
        user_choice = input("\nWould you like another password? (yes/no): ").strip().lower()

    print("\nThank you for using the Secure Password Generator!")

if __name__ == "__main__":
    main_menu()
