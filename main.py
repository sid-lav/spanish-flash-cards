import sys
from PyQt5.QtWidgets import QApplication
from modules.gui import FlashcardApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    flashcard_app = FlashcardApp()
    flashcard_app.show()
    sys.exit(app.exec_())
