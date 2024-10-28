import json

# Load the JSON data from the file
with open('data/data.json', 'r') as json_file:
    data = json.load(json_file)

# Assign the loaded data to original variable names
verbs = data["verbs"]
adjectives = data["adjectives"]
adverbs = data["adverbs"]
nouns = data["nouns"]

# 
verbs_keylist = list(verbs.keys())
adjectives_keylist = list(adjectives.keys())
adverbs_keylist = list(adverbs.keys())
nouns_keylist = list(nouns.keys())
