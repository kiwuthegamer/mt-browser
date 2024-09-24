import sys
import ctypes
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QWidget, QPushButton, QLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl, QSize


# Get the screen size
SCREEN_SIZE = pyautogui.size()

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_SIZE

# Define a function to create an icon button
def create_icon_button(icon_name, icon_size=32):
    button = QPushButton()
    button.setIcon(QIcon(f'icons/{icon_name}.svg'))  # Assuming feather icons are saved as .svg
    button.setIconSize(QSize(icon_size, icon_size))
    button.setFixedSize(50, 50)  # Fixed button size for consistency
    button.setStyleSheet("""
        background-color: #333;
        border-radius: 12px;
    """)
    return button

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowIcon(QIcon('logos/icon.png'))
        self.setWindowTitle("browser")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #000;")  # Dark background

        # Create a central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create the top bar layout (HLayout for the top bar)
        top_bar_height_size = 0.1
        top_bar_layout = QHBoxLayout()
        # set height to 0.1 * screen height
        top_bar_layout.setSpacing(0)
        top_bar_layout.setContentsMargins(0, 0, 0, 0)
        top_bar_layout.setSizeConstraint(QLayout.SetFixedSize)
        top_bar_layout.setFixedHeight(int(SCREEN_HEIGHT * top_bar_height_size))
        
        
        # Logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("logos/logo.png")  # Assuming the logo image is saved as "logo.png"
        # Scale the logo to the height of the bar
        logo_label.setPixmap(logo_pixmap.scaled(top_bar_layout.sizeHint().height(), top_bar_layout.sizeHint().height(), Qt.KeepAspectRatio))
        top_bar_layout.addWidget(logo_label)

        # Back button
        back_button = create_icon_button('arrow-left')  # Feather icon for "back"
        top_bar_layout.addWidget(back_button)

        # Reload button
        reload_button = create_icon_button('rotate-cw')  # Feather icon for "reload"
        top_bar_layout.addWidget(reload_button)

        # Forward button
        forward_button = create_icon_button('arrow-right')  # Feather icon for "forward"
        top_bar_layout.addWidget(forward_button)

        # Search bar (Expanding)
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search or enter URL...")
        search_bar.setStyleSheet("""
            background-color: #333;
            padding: 10px;
            border-radius: 12px;
            font-size: 16px;
        """)
        top_bar_layout.addWidget(search_bar)
        search_bar.setSizePolicy(1, 1)  # Expanding the search bar to fill remaining space

        # Search button
        search_button = create_icon_button('search')  # Feather icon for "search"
        top_bar_layout.addWidget(search_button)

        # Settings button
        settings_button = create_icon_button('settings')  # Feather icon for "settings"
        top_bar_layout.addWidget(settings_button)

        # Add the top bar to the main layout

        # Create a web engine view for displaying the web page
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.example.com"))  # You can change the URL to any website

        # Add to the layout
        layout.addLayout(top_bar_layout)
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
