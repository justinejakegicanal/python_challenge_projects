full_word = input("Enter a word: ")
suffix = input("Enter the suffix to remove: ")

slice_to_remove = len(suffix)

tail = full_word[-slice_to_remove:]

if suffix == tail:
    final_answer = True
else:
    final_answer = False

print(f"Is suffix the same as the tail: {final_answer}")

