import json
from datetime import datetime, timezone
from fsrs import FSRS, Card, Rating

# Initialize the FSRS scheduler
f = FSRS()

# Load the JSON data from the file with UTF-8 encoding
with open('data/data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Assign the loaded data to original variable names
verbs = data["verbs"]
verbs_keylist = list(verbs.keys())

# Dictionary to store the FSRS cards
cards = {}

# Load cards from a file if it exists
try:
    with open('fsrs_cards.json', 'r', encoding='utf-8') as file:
        card_data = json.load(file)
        for spanish, data in verbs.items():
            card = Card.from_dict(data['card'])
            translation = data['translation']
            cards[spanish] = (card, translation)
    print("Loaded saved cards from file.")
except FileNotFoundError:
    print("No saved cards found. Initializing new cards.")
    # Create a new card for each verb if no saved file exists
    for spanish, english in verbs.items():
        card = Card()
        cards[spanish] = (card, english)

# Helper function to get a rating from the user
def get_rating_from_user():
    while True:
        return Rating.Again

# Review each card, update FSRS, and save to file
def review_cards(cards_dict):
    for spanish, (card, translation) in cards_dict.items():
        #print(f"Reviewing '{spanish}' (means '{translation}')")
        rating = get_rating_from_user()

        # Update the card based on the user's rating
        card, review_log = f.review_card(card, rating)

        # Update the card in the dictionary
        cards_dict[spanish] = (card, translation)

        # Save the updated cards to a file
        save_cards(cards_dict)

# Save the cards to a file with UTF-8 encoding
def save_cards(cards_dict):
    with open('fsrs_cards.json', 'w', encoding='utf-8') as file:
        data_to_save = {spanish: {'card': card.to_dict(), 'translation': translation} 
                        for spanish, (card, translation) in cards_dict.items()}
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)  # ensure_ascii=False ensures special characters are saved correctly
    #print("Saved cards to fsrs_cards.json.")

# Run the review process
if __name__ == "__main__":
    review_cards(cards)
    print("All cards have been reviewed!")
