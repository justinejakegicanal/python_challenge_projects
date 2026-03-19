unedited_text = input("Enter a word: ")
length_of_characters = int(input("Number of the length of characters: "))

result = unedited_text

while len(result) < length_of_characters:
    result = "0" + result

print(f"Result: '{result}'")
