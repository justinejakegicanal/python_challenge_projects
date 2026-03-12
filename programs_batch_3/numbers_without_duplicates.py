collected_numbers = []

for i in range(10):
    number = int(input("Enter a number: "))
    collected_numbers.append(number)

for current_number in collected_numbers:
    if collected_numbers.count(current_number) == 1:
        print(current_number)