collected_numbers = []

for i in range(10):
    number = input("Enter a number: ")
    current_number = int(number)
    collected_numbers.append(current_number)

duplicate_numbers = []

print("Number with duplicates: ")
for current_number in collected_numbers:
    if collected_numbers.count(current_number) > 1:
        if current_number not in duplicate_numbers:
            duplicate_numbers.append(current_number)
            print(current_number)











