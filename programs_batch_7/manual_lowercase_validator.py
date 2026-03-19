import string

word = input("Enter a word: ")
upper = string.ascii_uppercase
lower = string.ascii_lowercase

is_all_lower = True

for characters in word:
    if characters in upper:
        is_all_lower = False 

print(f"The word is all lower? {is_all_lower}")
