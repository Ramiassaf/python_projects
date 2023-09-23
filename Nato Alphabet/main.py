import pandas as pd

# TODO 1. Create a dictionary in this format:
# Read the CSV file into a DataFrame
data = pd.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary where keys are letters and values are NATO phonetic codes
Nato_letters = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Get user input and convert it to uppercase
user_input = input("Enter a word: ").upper()
# Create a list of NATO phonetic code words corresponding to each letter in user input
result = [Nato_letters[Letter] for Letter in user_input]
# Print the list of phonetic code words
print(result)
