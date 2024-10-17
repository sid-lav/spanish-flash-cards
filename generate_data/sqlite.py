import sqlite3
import json

# Load the JSON data from the file (no need to call json.loads again)
with open('cards.json', 'r') as json_file:
    cards = json.load(json_file)  # This already returns a Python dictionary

# Connect to SQLite database (or create it)
conn = sqlite3.connect('flashcards.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    spanish TEXT NOT NULL UNIQUE,
    english TEXT NOT NULL,
    due TEXT,
    stability REAL,
    difficulty REAL,
    elapsed_days INTEGER,
    scheduled_days INTEGER,
    reps INTEGER,
    lapses INTEGER,
    state INTEGER,
    last_review TEXT
)
''')

# Function to insert data into the database
def insert_card(spanish, translation, card_data):
    cursor.execute('''
        INSERT OR REPLACE INTO cards 
        (spanish, english, due, stability, difficulty, elapsed_days, scheduled_days, reps, lapses, state, last_review) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        spanish,  # spanish verb
        translation,  # english translation
        card_data['due'],  # due
        card_data['stability'],  # stability
        card_data['difficulty'],  # difficulty
        card_data['elapsed_days'],  # elapsed_days
        card_data['scheduled_days'],  # scheduled_days
        card_data['reps'],  # reps
        card_data['lapses'],  # lapses
        card_data['state'],  # state
        card_data['last_review']  # last_review
    ))

# Loop over each card and insert it into the database
for spanish, data in cards.items():
    translation = data['translation']
    card_data = data['card']
    insert_card(spanish, translation, card_data)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()

print("Data successfully imported into SQLite!")
