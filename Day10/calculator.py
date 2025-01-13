# Add the logo from art.py
import art
print(art.logo)

# Create 4 functions - add, subtract, multiply and divide
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(art.logo)

    # Program asks the user to type the first number
    first_number = float(input("What's the first number?: "))
    continue_calculating = True

    while continue_calculating:
        # Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
        print("+")
        print("-")
        print("*")
        print("/")
        chosen_operation = input("Pick an operation: ")

        # Program asks the user to type the second number
        second_number = float(input("What's the next number?: "))

        # Program works out the result based on the chosen mathematical operator
        if chosen_operation in operations:
            result = operations[chosen_operation](first_number, second_number)
            print(f"{first_number} {chosen_operation} {second_number} = {result}")

            # Program asks if the user wants to continue working with the previous result.
            reuse_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            # If yes, program loops to use the previous result as the first number and then repeats the calculation process.
            if reuse_result == "y":
                first_number = result
            # If no, program asks the user for the first number and wipes all memory of previous calculations.
            else:
                continue_calculating = False
                print("\n" * 20)
                calculator()
calculator()
