odd_count = 0

for i in range(10):
    number = int(input("Enter a number: "))

    if number % 2 == 1:
        odd_count += 1 

print(f"You entered {odd_count} odd numbers.")