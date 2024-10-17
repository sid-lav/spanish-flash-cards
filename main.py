import sys
from PyQt5.QtWidgets import QApplication
from modules.gui import FlashcardApp  # Import the GUI

# Main application class that interacts with the GUI and database
class FlashcardController(FlashcardApp):
    def __init__(self):
        super().__init__()
        self.load_next_card()

    def load_next_card(self):
        self.current_card = get_next_due_card()
        if self.current_card:
            self.flashcard_label.setText(self.current_card[1])  # Display the Spanish verb
        else:
            self.flashcard_label.setText("No cards due!")

    def show_answer(self):
        if self.current_card:
            self.flashcard_label.setText(self.current_card[2])  # Show the translation
        self.show_answer_button.setEnabled(False)

    def next_card(self, difficulty):
        if self.current_card:
            process_card_review(self.current_card, difficulty)
        self.load_next_card()




# Main application entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the controller that manages GUI and database interaction
    controller = FlashcardController()

    # Show the GUI
    controller.show()

    # Start the event loop
    sys.exit(app.exec_())
