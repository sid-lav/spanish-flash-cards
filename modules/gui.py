from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from modules.flashcard import get_next_due_card, process_card_review

class FlashcardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.current_card = None
        self.load_next_card()

    def setup_ui(self):
        self.setWindowTitle("Flashcard App")
        self.setGeometry(100, 100, 400, 300)

        self.flashcard_label = QLabel(self)
        self.flashcard_label.setAlignment(Qt.AlignCenter)

        self.show_answer_button = QPushButton("Show Answer", self)
        self.show_answer_button.clicked.connect(self.show_answer)

        self.easy_button = QPushButton("Easy", self)
        self.good_button = QPushButton("Good", self)
        self.hard_button = QPushButton("Hard", self)
        self.again_button = QPushButton("Again", self)

        self.easy_button.clicked.connect(lambda: self.next_card("Easy"))
        self.good_button.clicked.connect(lambda: self.next_card("Good"))
        self.hard_button.clicked.connect(lambda: self.next_card("Hard"))
        self.again_button.clicked.connect(lambda: self.next_card("Again"))

        layout = QVBoxLayout()
        layout.addWidget(self.flashcard_label)
        layout.addWidget(self.show_answer_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.easy_button)
        button_layout.addWidget(self.good_button)
        button_layout.addWidget(self.hard_button)
        button_layout.addWidget(self.again_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_next_card(self):
        self.current_card = get_next_due_card()
        if self.current_card:
            self.flashcard_label.setText(self.current_card[1])  # Spanish word
            self.show_answer_button.setEnabled(True)
        else:
            self.flashcard_label.setText("No cards due!")
            self.show_answer_button.setEnabled(False)

    def show_answer(self):
        if self.current_card:
            self.flashcard_label.setText(self.current_card[2])  # English translation
            self.show_answer_button.setEnabled(False)

    def next_card(self, difficulty):
        if self.current_card:
            # Pass individual tuple elements to process_card_review
            process_card_review(self.current_card[0], self.current_card[3], 
                                self.current_card[4], self.current_card[8], 
                                self.current_card[9], difficulty)
        self.load_next_card()
