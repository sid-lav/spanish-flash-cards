import json
import os

# Define paths
data_folder = os.path.join(os.path.dirname(__file__), 'data')
input_file = os.path.join(data_folder, 'categorised_words.json')
output_file = os.path.join(data_folder, 'cleaned_word_data.json')

# Load the JSON data from the word_data.json file
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Initialize an empty dictionary to hold the sorted data
sorted_data = {
    "verbs": {},
    "adjectives": {},
    "nouns": {},
    "adverbs": {}
}

# Process the data
if isinstance(data, dict):
    # Loop over each category (e.g., 'adjectives', 'verbs')
    for category, word_list in data.items():
        # Ensure the category exists in our sorted_data (to avoid unexpected keys)
        if category in sorted_data:
            # For each pair of words in the category list, add to the corresponding sorted dictionary
            sorted_data[category] = {item[0]: item[1] for item in word_list}
        else:
            print(f"Category '{category}' is not recognized and will be ignored.")
elif isinstance(data, list):
    print("Unexpected list structure. Sorting into specific categories is not possible without category labels.")
    sorted_data = {}  # Reset in case of error

# Write the sorted dictionary to a new JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=4)

print(f"Sorted and cleaned JSON has been saved to {output_file}")
