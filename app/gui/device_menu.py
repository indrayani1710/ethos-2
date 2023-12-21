import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QLineEdit,
    QApplication
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt, QObject, QEvent, QTimer
from .utilities.imgbuttonBtext import imgbuttonBtext
from .utilities.imgbutton import img_button
from .utilities.virtualkeyboardtest import open_keyboard
import os

os.environ['QT_QPA_PLATFORM'] = 'eglfs'

class DeviceMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        current_directory = os.getcwd()
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap(os.path.join(current_directory, "gui/assets/background.png")))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(5, 4, 190, 20)
        font_small = QFont("inika", 15, QFont.Bold)
        self.date_time_label.setFont(font_small)

        # Initial date and time display
        self.update_date_time()

        # Back button
        self.backbtn = imgbutton(self, "gui/assets/icons/BackIcon.png", 30, 30, "#D9D9D9", 5, 44, self.openSplashScreen)

        # Password label and field
        label = QLabel("Password", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 106)

        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("Please enter password here")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.textChanged.connect(self.verify_password)
        self.password_field.setFixedSize(355, 30)
        self.password_field.move(108, 100)
        self.password_field.installEventFilter(self)

        self.password_field.mouseDoubleClickEvent(open_keyboard(self.password_field, width=480, height=200))

        # User Menu button
        self.UserMenu = imgbuttonBtext(self, "gui/assets/icons/UserIcon.png", 55, 100, "User", "#D9D9D9", 18, 142, self.openEmployeeMenu)
        self.UserMenu.setEnabled(False)

        # Canteen button
        self.canteen = imgbuttonBtext(self, "gui/assets/icons/CanteenIcon.png", 55, 100, "Canteen", "#D9D9D9", 133, 142, self.openCanteenMenu)
        self.canteen.setEnabled(False)

    def eventFilter(self, obj, event):
        if obj == self.password_field and event.type() == QEvent.MouseButtonPress:
            self.virtual_keyboard.text_edit.setPlainText(self.password_field.text())
            if self.virtual_keyboard.exec_() == QtWidgets.QDialog.Accepted:
                self.password_field.setText(self.virtual_keyboard.text_edit.toPlainText())
        return super().eventFilter(obj, event)

    def update_date_time(self):
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%d{} %B %Y").format(
            "th" if 10 <= current_datetime.day <= 19 else {1: "st", 2: "nd", 3: "rd"}.get(current_datetime.day % 10, "th")
        )
        current_day = current_datetime.strftime("%A")
        formatted_time = current_datetime.strftime("%H:%M:%S")

        current_datetime_str = f"{formatted_date} - {formatted_time}"
        self.date_time_label.setText(current_datetime_str)

    def verify_password(self):
        password = self.password_field.text()
        expected_password = "ADMIN"
        is_password_matched = (password == expected_password)
        print("Password Matched:", is_password_matched)

        self.UserMenu.setEnabled(is_password_matched)
        self.canteen.setEnabled(is_password_matched)

    def openEmployeeMenu(self):
        from gui.employee_menu import EmployeeMenu
        self.openEmployeeMenu = EmployeeMenu()
        self.openEmployeeMenu.show()
        self.close()

    def openSplashScreen(self):
        from gui.device_splashscreen import SplashWindow
        self.openSplashScreen = SplashWindow()
        self.openSplashScreen.show()
        self.close()

    def openCanteenMenu(self):
        from canteen_main import canteenMain
        self.openCanteenMenu = canteenMain()
        self.openCanteenMenu.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeviceMenuWindow()
    window.show()
    sys.exit(app.exec_())
