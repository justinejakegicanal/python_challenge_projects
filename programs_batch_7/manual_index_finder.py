word = input("Enter a word: ")
search_character = input("Enter a character: ")

found_index = -1 

for i in range(len(word)):
    if word[i] == search_character:
        found_index = i 
        break

print(f"The first occurrence of '{search_character}' is at index: {found_index}")