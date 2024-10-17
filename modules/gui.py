import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from modules.flashcard import get_next_due_card, process_card_review  # Import SQL functions

# Main window class
class FlashcardApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Flashcard App")
        self.setGeometry(100, 100, 400, 300)

        # Initialize the current card
        self.current_card = None

        # Create a label for the flashcard question/answer
        self.flashcard_label = QLabel(self)
        self.flashcard_label.setAlignment(Qt.AlignCenter)

        # Create a "Show Answer" button
        self.show_answer_button = QPushButton("Show Answer", self)
        self.show_answer_button.clicked.connect(self.show_answer)

        # Difficulty buttons
        self.easy_button = QPushButton("Easy", self)
        self.good_button = QPushButton("Good", self)
        self.hard_button = QPushButton("Hard", self)
        self.again_button = QPushButton("Again", self)

        # Connect the difficulty buttons to their respective functions
        self.easy_button.clicked.connect(lambda: self.next_card("Easy"))
        self.good_button.clicked.connect(lambda: self.next_card("Good"))
        self.hard_button.clicked.connect(lambda: self.next_card("Hard"))
        self.again_button.clicked.connect(lambda: self.next_card("Again"))

        # Layout setup
        layout = QVBoxLayout()

        # Add the flashcard label to the layout
        layout.addWidget(self.flashcard_label)

        # Add the "Show Answer" button
        layout.addWidget(self.show_answer_button)

        # Create a horizontal layout for the difficulty buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.easy_button)
        button_layout.addWidget(self.good_button)
        button_layout.addWidget(self.hard_button)
        button_layout.addWidget(self.again_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        # Set the main layout for the window
        self.setLayout(layout)

        # Display the first flashcard
        self.load_next_card()

    # Show the current flashcard's question
    def show_question(self):
        if self.current_card:
            self.flashcard_label.setText(self.current_card["spanish"])
            self.show_answer_button.setEnabled(True)
            self.show_answer_button.setText("Show Answer")

    # Show the answer when "Show Answer" is clicked
    def show_answer(self):
        if self.current_card:
            self.flashcard_label.setText(self.current_card["english"])
            self.show_answer_button.setEnabled(False)

    # Load the next card from the database
    def load_next_card(self):
        card = get_next_due_card()  # Fetch the next due card from the database
        if card:
            # Store the card details for future use
            self.current_card = {
                "id": card[0],
                "spanish": card[1],
                "english": card[2],
                "due": card[3],
                "stability": card[4],
                "difficulty": card[5],
                "elapsed_days": card[6],
                "scheduled_days": card[7],
                "reps": card[8],
                "lapses": card[9]
            }
            self.show_question()
        else:
            self.flashcard_label.setText("No more cards due for review.")

    # Move to the next flashcard after a difficulty is chosen
    def next_card(self, difficulty):
        if self.current_card:
            # Process and update the card based on the review
            process_card_review(self.current_card, difficulty)

            # Load the next card
            self.load_next_card()

# Main application
app = QApplication(sys.argv)
window = FlashcardApp()
window.show()
sys.exit(app.exec_())
