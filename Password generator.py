import random
import string


def generate_password(length, use_upper, use_digits, use_symbols):
    # start with lowercase letters always included
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=== Simple Password Generator ===")

    length = int(input("Enter password length: "))

    upper_choice = input("Include uppercase letters? (y/n): ").lower()
    digit_choice = input("Include numbers? (y/n): ").lower()
    symbol_choice = input("Include symbols? (y/n): ").lower()

    use_upper = upper_choice == "y"
    use_digits = digit_choice == "y"
    use_symbols = symbol_choice == "y"

    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\nYour generated password is:")
    print(password)


# how many passwords do you want to generate?
if __name__ == "__main__":
    while True:
        main()
        again = input("\nGenerate another password? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break