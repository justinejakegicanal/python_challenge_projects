try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    quotient = first_number // second_number
    print(f"The quotient is: {quotient}")

except ValueError:
    print("Invalid input. Please enter numeric values.")

except ZeroDivisionError:
    print("Error: Second number cannot be zero.") 