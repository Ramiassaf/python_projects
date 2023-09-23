# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open the starting letter file and read its contents
with open("/Users/user/Desktop/pycharmprojects/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

# Open the invited names file and read its contents into a list
with open("/Users/user/Desktop/pycharmprojects/Mail Merge Project Start/Input/Names/invited_names.txt") as guests:
    names = guests.readlines()

# Loop through each name in the list of invited names
for name in names:
    # Replace the "[name]" placeholder in the letter with the actual name
    personal = letter_content.replace("[name]", name.strip())

    # Construct the filename for the personalized letter using the recipient's name
    filename = f"/Users/user/Desktop/pycharmprojects/Mail Merge Project Start/Output/ReadyToSend/" \
               f"Letter_for_{name.strip()}.txt"

    # Create a new file with the specified filename in the "ReadyToSend" folder
    # and write the contents of the personalized letter to the file
    with open(filename, mode="w") as letter:
        letter.write(personal)
        