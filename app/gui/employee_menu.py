import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtCore import Qt

from .utilities.imgbuttonBtext import imgbuttonBtext
from .utilities.imgbutton import imgbutton
from gui.employee_new import NewUserWindow
from gui.device_menu import DeviceMenuWindow
from gui.employee_copy import EmployeeCopy
from gui.employee_delete import EmployeeDelete

class EmployeeMenu(QMainWindow):

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
        self.backbtn = imgbutton(self, "gui/assets/icons/BackIcon.png", 30, 30, "#D9D9D9", 5, 44, self.openMenuScreen)

        # New User button
        self.new_user_btn = imgbuttonBtext(self, "gui/assets/icons/NewUserIcon.png", 55, 100, "New", "#D9D9D9", 18, 142, self.openNewUserScreen)
        self.new_user_btn.setEnabled(True)

        # Edit User button
        self.edit_user_btn = imgbuttonBtext(self, "gui/assets/icons/EditUserIcon.png", 55, 100, "Edit", "#D9D9D9", 133, 142, self.openNewUserScreen)
        self.edit_user_btn.setEnabled(True)

        # Copy User button
        self.copy_user_btn = imgbuttonBtext(self, "gui/assets/icons/CopyUserIcon.png", 55, 100, "Copy", "#D9D9D9", 248, 142, self.openEmployeeCopy)
        self.copy_user_btn.setEnabled(True)

        # Delete User button
        self.delete_user_btn = imgbuttonBtext(self, "gui/assets/icons/DeleteUserIcon.png", 55, 100, "Delete", "#D9D9D9", 363, 142, self.openEmployeeDelete)
        self.delete_user_btn.setEnabled(True)

    def openNewUserScreen(self):
        self.openNewUserScreen = NewUserWindow()
        self.openNewUserScreen.show()
        self.close()

    def openMenuScreen(self):
        self.openMenuScreen = DeviceMenuWindow()
        self.openMenuScreen.show()
        self.close()

    def openEmployeeCopy(self):
        self.openEmployeeCopy = EmployeeCopy()
        self.openEmployeeCopy.show()
        self.close()

    def openEmployeeDelete(self):
        self.openEmployeeDelete = EmployeeDelete()
        self.openEmployeeDelete.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeMenu()
    window.show()
    sys.exit(app.exec_())
