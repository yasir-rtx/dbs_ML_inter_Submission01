# Import library
from os import path
import json

# Stopwords Path
STOPWORDS_PATH = './resources/stopwords/'
stop_path = path.join(STOPWORDS_PATH, 'stopwords.txt')

#  Read Stopwords file
print("Read Stopwordsd.txt")
with open(stop_path, 'r') as file:
    stopwords = file.readlines()
    
# Create Stopwords Dictionary
print("\nCreating Dictionary...")
stopwords_dictonary = {}
for word in stopwords:
    word = word.replace('\n', '')               # Remove newline
    stopwords_dictonary[word] = None
print("Dictionary is Created!")
    
# Save Stopwords Dictionary
print("\nSave dictionary as json file...")
with open(path.join(STOPWORDS_PATH, 'stopwords_dict.json'), mode='w') as file:
    json.dump(stopwords_dictonary, file, indent=4)
print("Dictionary is Saved!")