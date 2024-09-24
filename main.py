import sys
import ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle("browser")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #121212;")  # Dark background

        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create a label that says hi
        label = QLabel("Hi!")
        label.setStyleSheet("color: #FFFFFF;")  # White text

        # Create a web engine view for displaying the web page
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # You can change the URL to any website

        # Add the label and the browser view to the layout
        layout.addWidget(label)
        layout.addWidget(self.browser)

        # Set the central widget's layout
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showEvent(self, event):
        super().showEvent(event)
        # Get the window handle (HWND) using winId() and pass it to the ctypes function
        hwnd = self.winId().__int__()
        value = ctypes.c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, 20, ctypes.byref(value), ctypes.sizeof(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the browser window
    window = BrowserWindow()
    window.show()

    sys.exit(app.exec_())
