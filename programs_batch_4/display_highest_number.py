collected_numbers = []

while True: 
    try: 
        number = input("Enter a number: ")
        current_number = int(number)
        collected_numbers.append(current_number)
    
    except ValueError:
        print("Stopping the input.")
        break

if collected_numbers:
    highest_number = max(collected_numbers)
    print(f"The highest number entered is: {highest_number}")