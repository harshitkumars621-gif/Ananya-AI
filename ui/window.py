import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class AnanyaWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ananya AI")
        self.resize(420, 220)

        layout = QVBoxLayout()

        title = QLabel("🌸 Ananya AI")
        title.setAlignment(Qt.AlignCenter)

        text = QLabel("Hello Harshit ❤️\nMain Ananya hoon.")
        text.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(text)

        self.setLayout(layout)


def run():
    app = QApplication(sys.argv)

    window = AnanyaWindow()
    window.show()

    sys.exit(app.exec())