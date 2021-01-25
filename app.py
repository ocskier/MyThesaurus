import json
import difflib
from difflib import SequenceMatcher

data = json.load(open('data.json'))
word = input('What word would you like defined? ')

def getDefinition(str):
    lowerStr = str.lower()
    matches = []
    for key in data:
        if SequenceMatcher(None, lowerStr, key).ratio() > 0.78:
            matches.append({key : data[key]})
    
    if len(matches) == 0:
        return 'Word does not exist!'
    else: 
        return matches

for i in getDefinition(word):
    print(json.dumps(i, indent=2))
