word = input("Enter a word: ")
length_of_characters = int(input("Number of the length of characters:"))

result = word
while len(result) < length_of_characters:
    result = " " + result

print(f"Result: '{result}'")