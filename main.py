import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from gui.device_splashscreen import SplashWindow

def main():
    print("Ethos firmware started")
    
    # Set environment variable for display
    os.environ['QT_QPA_PLATFORM'] = 'eglfs'
    
    # Set display size for Waveshare 5-inch
    os.environ['QT_EGLFS_PHYSICAL_WIDTH'] = '86'  # Adjust based on the actual display width
    os.environ['QT_EGLFS_PHYSICAL_HEIGHT'] = '64'  # Adjust based on the actual display height
    
    # Create the application object with appropriate flags
    app = QApplication(sys.argv + ['--platform', 'eglfs'])
    
    # Set the window to be fullscreen on the specified display
    window = SplashWindow()
    window.setWindowState(Qt.WindowFullScreen)
    
    print("SplashWindow created")
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
