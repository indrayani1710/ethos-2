from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QDialog, QLabel
from PySide6.QtCore import Qt

import os
os.environ['QT_QPA_PLATFORM'] = 'eglfs'



class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Popup Dialog")

        layout = QVBoxLayout(self)
        label = QLabel("This is a popup!", self)
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.button = QPushButton('Show Popup', self)
        self.button.clicked.connect(self.show_popup)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_popup(self):
        popup = PopupDialog(self)
        popup.setGeometry(100, 100, 200, 100)
        popup.exec()

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
