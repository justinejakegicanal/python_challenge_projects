import string

sentence = input("Enter a sentence: ")
upper = string.ascii_uppercase
lower = string.ascii_lowercase

result = ""

for i in range(len(sentence)):
    character = sentence[i]

    if i == 0 or sentence[i-1] == " ":
        if character in lower: 
            result += upper[lower.find(character)]
        else:
            result += character
    else:
        if character in upper: 
            result += lower[upper.find(character)]
        else: 
            result += character 

print(result) 
