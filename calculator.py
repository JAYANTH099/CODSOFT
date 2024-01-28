def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b

def calculate(operand, fn, ln):
    if operand == '+':
        solution = add(fn, ln)
    elif operand == '-':
        solution = sub(fn, ln)
    elif operand == '*':
        solution = mul(fn, ln)
    elif operand == '/':
        solution = div(fn, ln)
        if solution is None:
            return None
    else:
        print("Error: Invalid operand")
        return None

    print(f"{fn} {operand} {ln} = {solution}")
    return solution

def main():
    try:
        first_digit = float(input("Enter the first digit: "))
        oper = input("Select one operation (+, -, *, /): ")
        last_digit = float(input("Enter the second number: "))

        result = calculate(oper, first_digit, last_digit)

        if result is not None:
            while input("Type 'yes' to continue or 'no' to exit: ").lower() == 'yes':
                new_oper = input("Pick an operator: ")
                new_digit = float(input("Enter the next digit: "))
                result = calculate(new_oper, result, new_digit)
                if result is None:
                    break

        print("Thank you")
    except ValueError:
        print("Error: Invalid input. Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
