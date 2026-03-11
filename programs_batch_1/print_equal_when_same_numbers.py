first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

if first_number > second_number: 
    print(f"The bigger number is: {first_number}")
elif first_number < second_number:
    print(f"The bigger number is: {second_number}")
else:
    print("The numbers are equal")
