full_word = input("Enter a word: ")
slice_to_remove = input("Enter the prefix to remove: ")

slice_size = len(slice_to_remove)

front_letters = full_word[:slice_size]

if front_letters == slice_to_remove:
    final_word = full_word[slice_size:]
else: 
    final_word = full_word

print(f"The final word will be: {final_word}")
