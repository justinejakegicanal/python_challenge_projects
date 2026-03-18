order_of_numbers = []

while True:
    try:
        digit = input("Enter a number: ")
        unordered_digit = int(digit)
        order_of_numbers.append(unordered_digit)

    except ValueError:
        print("Stopping the input.")
        break

if order_of_numbers:
    order_of_numbers.sort(reverse=True)
    print(f"The sorted order from highest to lowest is: {order_of_numbers}")

