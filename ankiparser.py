import json

with open('/home/sbl/project1/wordlist.txt', 'r') as file:
    wordlist = file.read()

lines = wordlist.strip().split('\n')

index = []

parsedwordlist = []

for line in lines:
    wordlist = line.split("\t")
    
    # Delete index 1 and 3
    wordlist = [wordlist[0], wordlist[2]]
    
    parsedwordlist.append(wordlist)
    
# Export the list to a JSON file
with open('/home/sbl/project1/word_data.json', 'w') as json_file:
    json.dump(parsedwordlist, json_file, ensure_ascii=False, indent=4)
