from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt

import sys
import os


def button_pressed():
    print("Button pressed")


def main():
    app = QApplication(sys.argv)

    # Create a main window
    window = QMainWindow()

    # Create a QPushButton
    button = QPushButton()
    button.setText("Press Me")
    button.setGeometry(100, 100, 200, 50)

    # Connect the button's pressed signal to the button_pressed function
    button.pressed.connect(button_pressed)

    # Set the button as the central widget
    window.setCentralWidget(button)

    # Set up the main window properties
    window.setWindowTitle("Raspberry Pi Touch Screen Demo")
    window.setGeometry(0, 0, 480, 800)

    print("Central Widget Size:", window.centralWidget().size())
    print("Button Size:", button.size())

    # Show the main window
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
