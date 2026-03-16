package_of_numbers = []

while True: 
    try: 
       input_number = input("Enter a number: ")
       current_number = float(input_number)

       package_of_numbers.append(current_number)

    except ValueError:
        print("Input is not a valid number. Stopping input.:")
        break

if package_of_numbers:
    current_number = min(package_of_numbers)
    print(f"The smallest number is: {current_number}")

else:
    print("No numbers were entered.")
