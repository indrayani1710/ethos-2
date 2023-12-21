#!/usr/bin/python

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Slot
import os

# Set the environment variable for the Qt platform to 'eglfs'
os.environ['QT_QPA_PLATFORM'] = 'eglfs'

# Define the slot function
@Slot()
def say_hello():
    print("Button clicked, Hello!")

# Create the Qt Application
app = QApplication(sys.argv)

# Create a widget to hold the button
widget = QWidget()

# Create a layout for the widget
layout = QVBoxLayout(widget)

# Create a button
button = QToolButton("Click me")

# Connect the button's click signal to the say_hello slot
button.clicked.connect(say_hello)

# Set the width and height of the button to match the text dimensions
button.setFixedSize(button.sizeHint())

# Add the button to the layout
layout.addWidget(button)

# Show the widget
widget.show()

# Run the main Qt event loop
app.exec()
