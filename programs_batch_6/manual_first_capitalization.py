import string

word = input("Enter a word: ")
upper = string.ascii_uppercase
lower = string.ascii_lowercase

first = word[0]
last = word[1:]

if first in lower:
    final_first = upper[lower.find(first)]
else: 
    final_first = first

final_last = ""
for character in last:
    if character in upper:
        final_last += lower[upper.find(character)]
    else:
        final_last += character 

result = final_first + final_last
print(result) 