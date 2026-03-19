word = input("Enter a word: ")
find_letter = input("Enter the letter to find: ")

counter = 0 

for character in word:
    if character == find_letter:
        counter += 1 

print(f"The letter repeated for '{counter}' times.")