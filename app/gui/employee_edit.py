import csv
import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QComboBox,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from app.gui.utilities.imgbuttonBtext import imgbuttonBtext

import os

os.environ['QT_QPA_PLATFORM'] = 'eglfs'

class NewUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("app/gui/assets/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Back button
        self.backbtn = imgbuttonBtext(self, "app/gui/assets/icons/BackIcon.png", 30, 30, (5, 44), self.openUserMenu, "", "#D9D9D9")

        def get_employee_info(employee_id):
            with open('app/gui/utilities/EmpMaster-Epitage.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] == employee_id:
                        if len(row) > 2:
                            return row[1], row[2]  # Return EmployeeName and Date of Birth
                        else:
                            break  # Handle the case where the row doesn't have enough elements
                return None  # Return None if employee info is not found

        # Parse column from CSV file
        column_list = []
        dob_dict = {}  # Dictionary to store EmployeeName and Date of Birth mapping
        with open('app/gui/utilities/EmpMaster-Epitage.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first row if it contains headers
            for row in reader:
                if len(row) > 0:  # Check if the row has at least one element
                    column_list.append(row[0])  # Append EmpID to column_list
                    dob_dict[row[0]] = row[2]  # Store empID and Date of Birth mapping

        # ID selection combo box
        combo = QComboBox(self)
        combo.addItems(column_list)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.completer().setCompletionMode(QComboBox.PopupCompletion)
        combo.setStyleSheet("QComboBox { height: 35px; }")
        combo.move(108, 96)
        combo.setFixedWidth(255)
        combo.setFixedHeight(30)

        # Connect combo box signal
        combo.currentTextChanged.connect(self.combo_text_changed)

        # Labels and text fields
        self.create_label_and_text("ID:", 18, 102, combo)
        self.create_label_and_text("Name:", 18, 139, self.text_id, readonly=False)
        self.create_label_and_text("Birth Date:", 18, 213, self.text_dob, readonly=False)

        # Photo display
        self.create_label_and_image("images/placeholderimg.png", 369, 96, 94, 142)

        # RFID, Finger, Face labels and buttons
        self.create_label_and_text("RFID:", 128, 246, self.label_rfid)
        self.create_imgbuttonBtext("app/gui/assets/icons/Card.png", 100, 100, (17, 246), self.recordRFID)

        self.create_label_and_text("Finger:", 128, 372, self.label_fing)
        self.create_imgbuttonBtext("app/gui/assets/icons/FingerVeri_Icon.png", 100, 100, (17, 372), self.recordFinger)

        self.create_label_and_text("Face:", 128, 498, self.label_face)
        self.create_imgbuttonBtext("app/gui/assets/icons/facebtn.png", 100, 100, (17, 498), self.recordFace)

        # Cancel and OK buttons
        self.create_imgbuttonBtext("images/icons/facebtn.png", 100, 100, (17, 498), self.openUserMenu)

        # Save button
        save_button = QPushButton('Save', self)
        save_button.move(246, 729)
        save_button.setFixedSize(85, 35)
        save_button.clicked.connect(self.save_employee_info)

        self.show()

    def combo_text_changed(self):
        selected_employee_id = self.combo.currentText()
        if selected_employee_id:
            employee_info = self.get_employee_info(selected_employee_id)
            if employee_info is not None:
                employee_name, dob = employee_info
                self.text_id.setText(str(employee_name))  # Display EmployeeName
                self.text_dob.setText(dob)
                # Update employee picture based on the selected ID
                image_path = f'data/emp-photos/{selected_employee_id}.jpg'  # Replace with your image path
                self.picture_label.setPixmap(QPixmap(image_path))
                return
        self.text_id.clear()
        self.text_dob.clear()
        self.picture_label.setPixmap(QPixmap("images/placeholderimg.png"))  # Show placeholder image if no ID selected

    def save_employee_info(self):
        employee_id = self.combo.currentText()
        employee_name = self.text_id.text()
        dob = self.text_dob.text()
        rfid = self.label_rfid.text()
        finger = self.label_fing.text()

        # Check if any of the fields are empty
        if not employee_id or not employee_name or not dob or not rfid or not finger:
            return

        # Open the CSV file in append mode and write the new user data
        with open('app/gui/utilities/EmpMaster-Epitage.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([employee_id, employee_name, dob, rfid, finger])

        # Clear the input fields and reset the combo box
        self.combo.setCurrentIndex(-1)
        self.text_id.clear()
        self.text_dob.clear()
        self.label_rfid.clear()
        self.label_fing.clear()
        self.picture_label.setPixmap(QPixmap("images/placeholderimg.png"))

        # Optional: Update the combo box and dob_dict with the new user data
        self.column_list.append(employee_id)
        self.dob_dict[employee_id] = dob
        self.combo.addItem(employee_id)

    def create_label_and_text(self, text, x, y, linked_widget, readonly=True):
        label = QLabel(text, self)
        label.move(x, y)

        text_field = QLineEdit(self)
        text_field.setReadOnly(readonly)
        text_field.move(x + 90, y - 5)
        text_field.resize(255, 30)

        if readonly:
            setattr(self, "label_" + text.lower(), text_field)
