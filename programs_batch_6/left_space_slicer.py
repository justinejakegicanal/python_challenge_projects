unedited_text = input("Enter a text: ")
position = 0

while unedited_text[position] == " ":
    position = position + 1 

edited_text = unedited_text[position:]

print(edited_text)