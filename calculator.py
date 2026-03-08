print("Welcome to Calculator project")

while True:
    try:
        num1 = float(input("Enter your first number: "))
        operator = input("Enter operator(+, -, *, /, %, //, **): ").strip()
        num2 = float(input("Enter your second number: "))

        if operator == "+":
            print(f"Result: {num1 + num2}")

        elif operator == "-":
            print(f"Result: {num1 - num2}")

        elif operator == "*":
            print(f"Result: {num1 * num2}")

        elif operator == "/":
                try:
                    print(f"Result: {num1 / num2}")
                except ZeroDivisionError:
                    print("Error: cannot divide by zero!") 

        elif operator == "%":
            print(f"Result: {num1 % num2}")

        elif operator == "//":
            print(f"Result: {num1 // num2}")

        elif operator == "**":
            print(f"Result: {num1 ** num2}")

        else:
            print("Invalid operator")


        choice = input("Do you continue Yes/no: ").lower()

        if choice == "yes":
            continue
        else:
            break

    except ValueError:
        print("Invalid input, Please enter a valid number") 

        
