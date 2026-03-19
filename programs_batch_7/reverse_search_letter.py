word = input("Enter a word: ")
find_letter = input("Enter a letter to find: ")

reverse_search = -1 

for i in range(len(word) - 1, -1, -1):
    if word[i] == find_letter:
        reverse_search = i
        break

if reverse_search != -1:
    print(f"Found at {reverse_search}")
else: 
    print("Not found.")