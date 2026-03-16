package_of_numbers = []

while True:
    try:
        number_input = input("Enter a number: ")
        current_number = float(number_input)
        package_of_numbers.append(current_number)

    except ValueError:
        print("Input is not a valid number. Stopping input.")
        break

if package_of_numbers: 
    package_of_numbers.sort()
    print(f"The numbers from lowest to highest are: {package_of_numbers}") 
    

    for current_number in package_of_numbers:
        print(current_number)

else: 
    print("No numbers were entered.")