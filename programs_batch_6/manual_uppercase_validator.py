import string

text = input("Enter a word: ")
lower = string.ascii_lowercase

is_all_upper = True

for character in text:
    if character in lower:
        is_all_upper = False
    
print(f"The text is all upper? {is_all_upper}") 
