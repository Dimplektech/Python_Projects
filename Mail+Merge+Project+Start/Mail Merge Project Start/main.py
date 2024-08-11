# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
f = open("Mail Merge Project Start/Input/Names/invited_names.txt", "r")
names = f.readlines()
print(names)
f.close

f_para = open("Mail Merge Project Start/Input/Letters/starting_letter.txt","r")
para = f_para.read()

# Include each name in the text and create new txt file 
for name in names:
    name = name.strip()
  
    new_letter = para.replace(PLACEHOLDER, name)
    with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.docx", "w") as completed_letter:
        completed_letter.write(new_letter)
    