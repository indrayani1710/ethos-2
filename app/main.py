import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from gui.device_splashscreen import Config

def main():
    print("Ethos firmware started")
    
    # Set environment variable for display
    os.environ['QT_QPA_PLATFORM'] = 'eglfs'
    
    # Set display size for Waveshare 5-inch
    os.environ['QT_EGLFS_PHYSICAL_WIDTH'] = '86'  # Adjust based on the actual display width
    os.environ['QT_EGLFS_PHYSICAL_HEIGHT'] = '64'  # Adjust based on the actual display height
    
    app = QApplication(sys.argv)
    config = Config()  # Assuming Config is a class that extends QMainWindow or QWidget
    window = config.get_main_window()  # Replace getMainWindow with the appropriate method to get your QMainWindow instance
    print("SplashWindow created")
    window.showFullScreen()  # This should set the window to full screen
    sys.exit(app.exec_())
    
    


if __name__ == "__main__":
    main()
