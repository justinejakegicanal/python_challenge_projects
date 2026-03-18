import string

text = input("Enter a text: ")
upper = string.ascii_uppercase  
lower = string.ascii_lowercase
result = ""

for character in text:
    if character in upper:
        result += lower[upper.find(character)]
    else:
        result += character
    
print(result) 