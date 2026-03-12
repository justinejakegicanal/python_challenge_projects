try:    
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    difference = first_number - second_number

    print(f"The difference is: {difference}")    

except ValueError:
    print("Invalid input. Please enter numeric values.")    
