import json
import difflib
from difflib import get_close_matches, SequenceMatcher

data = json.load(open('data.json'))
word = input('What word would you like defined? ')

def getDefinition(str):
    lowerStr = str.lower()
    for key in data:
        if SequenceMatcher(None, lowerStr, key).ratio() == 1.00:
            return {key: data[key]}
    
    matches = get_close_matches(lowerStr, data.keys(),5,0.78)
    if len(matches) == 0:
        return 'Can\'t find a matching word!'
    else: 
        newInput = input(f'Which word closest matches your yours? {matches} ? ')
        return getDefinition(newInput)

print(json.dumps(getDefinition(word), indent=2))
