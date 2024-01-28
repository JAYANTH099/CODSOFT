import random
import string

def generate_password(length, symbols, numbers):
    # Define character sets
    letters = string.ascii_letters
    numbers_set = string.digits
    symbols_set = '!#$%&()*+'

    # Initialize password list
    password_list = []

    # Add random letters
    password_list += [random.choice(letters) for _ in range(length)]

    # Add random symbols
    password_list += [random.choice(symbols_set) for _ in range(symbols)]

    # Add random numbers
    password_list += [random.choice(numbers_set) for _ in range(numbers)]

    # Shuffle the password list
    random.shuffle(password_list)

    # Convert password list to string
    password = ''.join(password_list)

    return password

def get_user_input():
    try:
        # Get user input for password criteria
        length = int(input("How many letters would you like to have in your password?\n"))
        symbols = int(input("How many symbols would you like to have?\n"))
        numbers = int(input("How many numbers would you like to have?\n"))

        return length, symbols, numbers
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return get_user_input()

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password criteria
    length, symbols, numbers = get_user_input()

    # Generate and print the password
    password = generate_password(length, symbols, numbers)
    print(f"Your password is: {password}")

# Run the program
if __name__ == "__main__":
    main()
