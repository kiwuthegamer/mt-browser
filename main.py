import sys
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtWebEngineWidgets as QtWebEngineWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

def create_browser_window():
    window = QtWidgets.QMainWindow()

    window.setWindowTitle("browser")
    window.setWindowIcon(QtGui.QIcon("logos/icon.png"))
    window.setGeometry(100, 100, 800, 600)
    window.showMaximized()

    central_widget = QtWidgets.QWidget()
    central_layout = QtWidgets.QVBoxLayout()

    hello_label = QtWidgets.QLabel("Hello World")
    hello_label.setAlignment(QtCore.Qt.AlignCenter)
    hello_label.setStyleSheet("font-size: 20px; padding: 10px; background-color: lightgray;")

    web_view = QtWebEngineWidgets.QWebEngineView()
    web_view.setUrl(QtCore.QUrl("https://www.google.com"))

    central_layout.addWidget(hello_label)
    central_layout.addWidget(web_view)

    central_widget.setLayout(central_layout)
    window.setCentralWidget(central_widget)

    return window


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and display the browser window
    window = create_browser_window()
    window.show()

    sys.exit(app.exec_())

