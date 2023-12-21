import sys
import os
from datetime import datetime
from PySide6.QtWidgets import (QLabel, QMainWindow, QPushButton, QApplication)
from PySide6.QtGui import QPixmap, QFont, QIcon
from PySide6.QtCore import Qt, QTimer
from .utilities.imgbuttonBtext import imgbuttonBtext
import subprocess
from gui.device_menu import DeviceMenuWindow

class Config:
    display_width = 480
    display_height = 800
    background_image_path = "gui/assets/background.png"
    logo_image_path = "gui/assets/EpitageLogo_final.png"
    additional_date_label_position = (50, 509, 380, 26)
    time_label_position = (205, 547, 300, 30)
    menu_button_position = (190, 623)
current_directory = os.path.dirname(os.path.abspath(__file__))
background_image_path = os.path.join(current_directory, Config.background_image_path)
logo_image_path = os.path.join(current_directory, Config.logo_image_path)
shutdown_button_path = os.path.join(current_directory, "gui/assets/icons/shutdown_button.png")
FONT_SMALL_SIZE = 15
FONT_BIG_SIZE = 20

# ...

font_small = QFont("inika", FONT_SMALL_SIZE, QFont.Bold)
font_big = QFont("inika", FONT_BIG_SIZE, QFont.Normal)
def update_date_time(self):
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%d{} %B %Y").format(
        "th" if 10 <= current_datetime.day <= 19 else {1: "st", 2: "nd", 3: "rd"}.get(current_datetime.day % 10, "th")
    )
    current_day = current_datetime.strftime("%A")
    formatted_time = current_datetime.strftime("%H:%M:%S")

    current_datetime_str = f"{formatted_date} - {formatted_time}"
    self.date_time_label.setText(current_datetime_str)
    self.additional_date_label.setText(f"{current_day}, {formatted_date}")
    self.time_label.setText(formatted_time)
