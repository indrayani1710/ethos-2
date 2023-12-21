import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit, QCheckBox
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt

from .utilities.imgbuttonBtext import imgbuttonBtext

class EmployeeDelete(QMainWindow):
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

        # Delete user button
        self.deleteUser = imgbuttonBtext(self, "gui/assets/icons/copyUserIcon50x50.png", 50, 50, "Delete", "#D9D9D9", 215, 34, self.close)
        self.deleteUser.setEnabled(False)

        # Back button
        self.backbtnv2 = imgbuttonBtext(self, "gui/assets/icons/BackIcon.png", 30, 30, "", "#D9D9D9", 5, 44, self.openUserMenu)

        # Cancel button
        cancel_btn = imgbuttonBtext(self, "gui/assets/icons/Cancel_btn.png", 100, 100, "Cancel", "#D9D9D9", 147, 729, self.close)
        cancel_btn.resize(85, 35)

        # Delete button
        delete_btn = imgbuttonBtext(self, "gui/assets/icons/copyBtn.png", 100, 100, "Delete", "#D9D9D9", 248, 729, self.close)  # TODO: Function to be added to delete.
        delete_btn.resize(85, 35)

        # Labels & textfields
        self.create_label_and_text("ID", 18, 101, self.ID_field)

        # Checkboxes
        checkboxes_info = [("Card", 108, 135, self.cardCheckbox),
                           ("Thumb", 223, 135, self.thumbCheckbox),
                           ("Face", 321, 135, self.faceCheckbox),
                           ("Photo", 433, 135, self.photoCheckbox)]

        for info in checkboxes_info:
            self.create_checkbox(*info)

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

    def openUserMenu(self):
        from gui.employee_menu import EmployeeMenu
        self.openUserMenu = EmployeeMenu()
        self.openUserMenu.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeDelete()
    window.show()
    sys.exit(app.exec_())
