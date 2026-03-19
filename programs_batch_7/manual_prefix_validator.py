word = input("Enter a word: ")
slice_to_search = input("Enter the prefix to check: ")

slice_size = len(slice_to_search)

head = word[:slice_size]

if head == slice_to_search:
    is_starting = True
else:
    is_starting = False

print(f"Is the prefix same with with the starting word? {is_starting}") 