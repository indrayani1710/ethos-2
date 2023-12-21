import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QCheckBox
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from .utilities.imgbuttonBtext import imgbuttonBtext
from .utilities.combobox import custom_combobox

class EmployeeCopy(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        self.resize(self.width, self.height)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("gui/assets/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Copy user button
        self.copyUser = imgbuttonBtext(self, "gui/assets/icons/copyUserIcon50x50.png", 50, 50, "Copy", "#D9D9D9", 215, 34, self.close)
        self.copyUser.setEnabled(False)

        # Back button
        self.backbtnv2 = imgbuttonBtext(self, "gui/assets/icons/BackIcon.png", 30, 30, "", "#D9D9D9", 5, 44, self.close)

        # Cancel button
        cancel_btn = imgbuttonBtext(self, "gui/assets/icons/Cancel_btn.png", 100, 100, "Cancel", "#D9D9D9", 147, 729, self.close)
        cancel_btn.resize(85, 35)

        # Copy button
        copy_btn = imgbuttonBtext(self, "gui/assets/icons/copyBtn.png", 100, 100, "Copy", "#D9D9D9", 248, 729, self.close)
        copy_btn.resize(85, 35)

        # Labels & text fields
        self.create_label_and_combobox("Fr ID", 18, 96, self.FrID_field)
        self.create_label_and_text("To ID", 18, 134, self.ToID_field)
        
        # Checkboxes
        self.create_checkbox("Card", 108, 175, self.cardCheckbox)
        self.create_checkbox("Thumb", 223, 175, self.thumbCheckbox)
        self.create_checkbox("Face", 321, 175, self.faceCheckbox)
        self.create_checkbox("Photo", 433, 175, self.photoCheckbox)
        self.create_checkbox("Del Fr ID", 108, 210, self.delFrIdCheckbox)

        # Create label for date and time
        self.create_date_time_label()

        # Update date and time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        # Initial date and time display
        self.update_date_time()

    def create_label_and_combobox(self, text, x, y, combobox):
        label = QLabel(text, self)
        label.setStyleSheet("color: #808080")
        label.move(x, y)

        combobox.setFixedSize(355, 30)
        combobox.move(x + 90, y - 5)

    def create_label_and_text(self, text, x, y, text_field):
        label = QLabel(text, self)
        label.setStyleSheet("color: #808080")
        label.move(x, y)

        text_field.setFixedSize(355, 30)
        text_field.move(x + 90, y - 5)

    def create_checkbox(self, text, x, y, checkbox):
        label = QLabel(text, self)
        label.setStyleSheet("color: #808080")
        label.move(x, y)

        checkbox.setGeometry(x, y - 5, 100, 40)
        checkbox.setStyleSheet("QCheckBox::indicator { width : 20px; height : 20px; }"
                                "QCheckBox::indicator:pressed { background-color : orange; }")

    def create_date_time_label(self):
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(5, 4, 190, 20)
        font_small = QFont("inika", 10, QFont.Normal)
        self.date_time_label.setFont(font_small)

        self.time_label = QLabel(self)
        self.time_label.setGeometry(195, 547, 300, 30)
        self.time_label.setFont(font_small)

    def update_date_time(self):
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%d{} %B %Y").format(
            "th" if 10 <= current_datetime.day <= 19 else
            {1: "st", 2: "nd", 3: "rd"}.get(current_datetime.day % 10, "th")
        )
        current_day = current_datetime.strftime("%A")
        formatted_time = current_datetime.strftime("%H:%M:%S")

        current_datetime_str = f"{formatted_date} - {formatted_time}"
        self.date_time_label.setText(current_datetime_str)
