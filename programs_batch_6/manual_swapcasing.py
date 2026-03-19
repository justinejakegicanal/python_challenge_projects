import string

word = input("Enter a word: ")
upper = string.ascii_uppercase
lower = string.ascii_lowercase

result = ""

for character in word: 
    if character in upper: 
        result += lower[upper.find(character)]

    elif character in lower:
        result += upper[lower.find(character)]

    else:
        result += character 


print(result) 