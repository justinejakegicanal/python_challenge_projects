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
    most_duplicate = max(collected_numbers, key=collected_numbers.count)

    if collected_numbers.count(most_duplicate) > 1:
        print(f"The number with most duplicates is: {most_duplicate}")
    
    else:
        print("All the numbers are unique.")
