listed_numbers = []

while True:
    try:
        present_number = float(input("Enter a number: "))
        listed_numbers.append(present_number)
    
    except ValueError:
        print("Stopping the input.")
        break

if listed_numbers:
    average_of_numbers = sum(listed_numbers) / len(listed_numbers)
    print(f"The average of the listed_numbers are: {average_of_numbers}")
