unedited_text = input("Enter a text: ")

position = len(unedited_text) - 1

while position >= 0 and unedited_text[position] == " ":
    position = position - 1 

edited_text = unedited_text[:position + 1]

print(f"Final: '{edited_text}'") 
