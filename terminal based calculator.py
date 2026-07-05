def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b


def show_menu():
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"

        if result is not None:
            print(f"\nResult: {num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    main()