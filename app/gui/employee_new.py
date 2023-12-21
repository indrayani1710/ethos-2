import csv
import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QLineEdit,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .utilities.imgbuttonBtext import imgbuttonBtext
from .utilities.imgbutton import imgbutton

import os

os.environ['QT_QPA_PLATFORM'] = 'eglfs'

class NewUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("gui/assets/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Back button
        self.backbtn = imgbutton(self, "gui/assets/icons/BackIcon.png", 30, 30, "#D9D9D9", 5, 44, self.openUserMenu)

        # QLabel to display employee picture
        picture_label = QLabel(self)
        picture_label.setGeometry(369, 96, 94, 142)
        picture_label.setPixmap(QPixmap("gui/assets/placeholderimg.png"))
        picture_label.setScaledContents(True)

        # Employee ID
        label_id = QLabel('ID:', self)
        label_id.move(18, 102)
        newID = QLineEdit(self)
        newID.setReadOnly(False)
        newID.move(108, 96)
        newID.resize(255, 30)

        # Employee Name
        label_name = QLabel('Name:', self)
        label_name.move(18, 139)
        text_name = QLineEdit(self)
        text_name.setReadOnly(False)
        text_name.move(108, 134)
        text_name.resize(255, 30)

        # Birth Date
        label_dob = QLabel('Birth Date:', self)
        label_dob.move(18, 213)
        text_dob = QLineEdit(self)
        text_dob.setReadOnly(False)
        text_dob.move(108, 208)
        text_dob.resize(255, 30)

        # RFID
        label_rfid = QLineEdit(self)
        label_rfid.setReadOnly(False)
        label_rfid.move(128, 246)
        label_rfid.resize(350, 30)
        self.rfidcardbtn = imgbuttonBtext(self, "gui/assets/icons/Card.png", 100, 100, "", "#D9D9D9", 17, 246, self.close)

        # Finger Verification
        label_fing = QLineEdit(self)
        label_fing.setReadOnly(False)
        label_fing.move(128, 372)
        label_fing.resize(355, 30)
        self.fingerbtn = imgbuttonBtext(self, "gui/assets/icons/FingerVeri_Icon.png", 100, 100, "", "#D9D9D9", 17, 372, self.close)

        # Face Recognition
        label_face = QLineEdit(self)
        label_face.setReadOnly(False)
        label_face.move(128, 498)
        label_face.resize(355, 200)
        self.facebtn = imgbuttonBtext(self, "gui/assets/icons/facebtn.png", 100, 100, "", "#D9D9D9", 17, 498, self.close)

        # Cancel and OK buttons
        self.cancelbtn = imgbuttonBtext(self, "gui/assets/icons/facebtn.png", 100, 100, "", "#D9D9D9", 17, 498, self.openUserMenu)
        self.okbtn = imgbuttonBtext(self, "gui/assets/icons/facebtn.png", 100, 100, "", "#D9D9D9", 17, 498, self.openUserMenu)

        # Save button
        save_button = QPushButton('Save', self)
        save_button.move(246, 729)
        save_button.setFixedSize(85, 35)
        save_button.clicked.connect(self.save_employee_info)

        self.show()

    def openUserMenu(self):
        from gui.employee_menu import EmployeeMenu
        self.openUserMenu = EmployeeMenu()
        self.openUserMenu.show()
        self.close()

    def save_employee_info(self):
        employee_id = newID.text()
        employee_name = text_name.text()
        dob = text_dob.text()

        # Check if any of the fields are empty
        if not employee_id or not employee_name or not dob:
            return

        # Open the CSV file in append mode and write the new user data
        with open('app/gui/utilities/EmpMaster-Epitage.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([employee_id, employee_name, dob])

        # Clear the input fields and reset the combo box
        newID.clear()
        text_name.clear()
        text_dob.clear()
        label_rfid.clear()
        label_fing.clear()
        label_face.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewUserWindow()
    window.show()
    sys.exit(app.exec_())
