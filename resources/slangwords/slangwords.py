# Import library
from os import path
import json

# Slangwords Path
SLANGWORDS_PATH = './resources/slangwords/'
slang_path = './resources/slangwords/slangwords.txt'

#  Read slangwords file
print("Read slangwords.txt")
with open(slang_path, mode='r') as file:
    slangwords = file.readlines()
    
# Create Slangwords Dictionary
print("\nCreating Dictionary...")
slangwords_dict = {}
for slang in slangwords:
    slang = slang.replace('\n', '')         # Remove newline
    slang = slang.split('\t')               # Split by '\t'
    # print(slang)
    
    # Append slangwords to dictionary
    slangwords_dict[slang[0]] = slang[1]
print("Dictionary is Created!")
    
# Save Slangwords Dictionary
print("\nSave dictionary as json file...")
with open(path.join(SLANGWORDS_PATH, './slangwords_dict.json'), mode="w") as file:
    json.dump(slangwords_dict, file, indent=4)
print("Dictionary is Saved!")