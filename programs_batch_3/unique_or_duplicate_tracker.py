numbers_list = []

while True:
    try:
        number = input("Enter a number:")
        current_number = float(number)

        if current_number in numbers_list:
            print("Duplicate")

        else:
            print("Unique")
            numbers_list.append(current_number)

    except ValueError:
        print("Input is not a valid number. Stopping input.")
        break
        
