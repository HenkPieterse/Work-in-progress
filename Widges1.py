import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("My App")

            widget = QLabel("Hello")
            font = widget.font()
            font.setPointSize(30)
            widget.setFont(font)
            widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = QMainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()