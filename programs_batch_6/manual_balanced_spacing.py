word = input("Enter a word: ")
length_of_characters = int(input("Enter the length of characters required: "))
                           
result = word

while len(result) < length_of_characters: 
    result = " " + result 
    
    if len(result) < length_of_characters:
        result = result + " " 

print(f"Result: '{result}'") 

