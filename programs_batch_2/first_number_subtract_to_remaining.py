first_number = float(input("First number: "))

for i in range(9):
    remaining_numbers = float(input("Enter a number: "))
    first_number = first_number - remaining_numbers
    
print(f"The result is: {first_number}")
