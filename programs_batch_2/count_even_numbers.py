even_numbers = 0

for number in range(10):
    input_number = int(input("Enter a number: "))   
    
    if input_number % 2 == 0:
        even_numbers += 1 

print(f"There are {even_numbers} even numbers")  
