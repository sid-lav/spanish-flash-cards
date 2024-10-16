import json

def load_categorised_words(json_file):
    # Open and load the JSON file
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Extract the individual dictionaries from the JSON file
    adjectives = data.get('adjectives', [])
    verbs = data.get('verbs', [])
    adverbs = data.get('adverbs', [])
    nouns = data.get('nouns', [])
    
    # Optionally: also load the word type frequencies if needed
    word_type_frequencies = data.get('word_type_frequencies', {})
    
    # Return the dictionaries
    return adjectives, verbs, adverbs, nouns
    
adjectives, verbs, adverbs, nouns = load_categorised_words("data/categorised_words.json")
