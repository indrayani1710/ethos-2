from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout ,QHBoxLayout
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

import os

def img_button(parent, image_path, png_size, button_size, position, on_click, text, bg_color):
    # Create a container widget
    container = QWidget(parent)
    container.setGeometry(*position, button_size, button_size)

    # Set the background color of the container
    container.setStyleSheet(f"background-color: {bg_color};")

    # Create a vertical layout for the container
    layout = QVBoxLayout(container)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)


    current_directory=os.getcwd()
    # Create a QLabel for the PNG image
    current_directory=os.getcwd()
    pixmap = QPixmap(os.path.join(current_directory,image_path))
    scaled_pixmap = pixmap.scaled(png_size, png_size, Qt.AspectRatioMode.KeepAspectRatio)
    label = QLabel(container)
    label.setPixmap(scaled_pixmap)
    label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

    # Create a QLabel for the text
    text_label = QLabel(container)
    text_label.setAlignment(Qt.AlignCenter)
    text_label.setFont(QFont("inika", 15))
    text_label.setText(text)
    text_label.setContentsMargins(0, -15, 0, 0)

    # Add the labels to the layout
    layout.addWidget(label)
    layout.addWidget(text_label)

    # Set the layout for the container
    container.setLayout(layout)

    # Set up custom event handling for mouse clicks
    def mousePressEvent(event):
        if callable(on_click):
            on_click()
        event.accept()

    container.mousePressEvent = mousePressEvent

    return container
