full_word = input("Enter a word: ")
slice_to_remove = input("Enter the suffix to remove: ")

slice_size = len(slice_to_remove)
suffix = full_word[-slice_size:]

if suffix == slice_to_remove: 
    final_word = full_word[:-slice_size]
else: 
    final_word = full_word

print(final_word) 