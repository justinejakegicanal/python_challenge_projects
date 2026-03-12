try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    remainder = first_number % second_number
    print(f"The remainder is: {remainder}")

except ValueError:
    print("Invalid input. Please enter numeric values.")

except ZeroDivisionError:
    print("Error: Second number cannot be zero.")