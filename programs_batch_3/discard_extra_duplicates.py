unique_numbers = []

for i in range(10):
    number = int(input("Enter a number: "))
    
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"The first entries are: {unique_numbers}")