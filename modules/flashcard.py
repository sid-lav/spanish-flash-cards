import sqlite3
from datetime import datetime, timezone, timedelta

# Connect to SQLite database (or create it)
def connect_db(db_name='data/flashcards.db'):
    return sqlite3.connect(db_name)


def get_next_due_card():
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
    SELECT id, spanish, english, due, stability, difficulty, elapsed_days, scheduled_days, reps, lapses
    FROM cards
    WHERE due <= ?
    ORDER BY due ASC
    LIMIT 1
    '''
    now = datetime.now(timezone.utc).isoformat()
    cursor.execute(query, (now,))
    card = cursor.fetchone()

    conn.close()
    return card


# Update a card after the user has reviewed it
def update_card(card_id, new_due, stability, difficulty, reps, lapses, state, last_review):
    conn = connect_db()
    cursor = conn.cursor()

    query = '''
    UPDATE cards
    SET due = ?, stability = ?, difficulty = ?, reps = ?, lapses = ?, state = ?, last_review = ?
    WHERE id = ?
    '''
    cursor.execute(query, (new_due, stability, difficulty, reps, lapses, state, last_review, card_id))

    conn.commit()
    conn.close()

def process_card_review(card, difficulty):
    conn = connect_db()
    cursor = conn.cursor()

    card_id = card["id"]
    stability = float(card["stability"])
    reps = int(card["reps"])
    lapses = int(card["lapses"])

    if difficulty == "Easy":
        stability += 1.5
        reps += 1
    elif difficulty == "Good":
        stability += 1
        reps += 1
    elif difficulty == "Hard":
        stability += 0.5
        reps += 1
    elif difficulty == "Again":
        stability = max(0, stability - 1)
        lapses += 1

    new_due = datetime.now(timezone.utc) + timedelta(days=int(stability))

    cursor.execute('''
    UPDATE cards 
    SET due = ?, stability = ?, difficulty = ?, reps = ?, lapses = ?
    WHERE id = ?
    ''', (new_due.isoformat(), stability, difficulty, reps, lapses, card_id))

    conn.commit()
    conn.close()

