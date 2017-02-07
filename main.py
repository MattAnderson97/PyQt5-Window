from PyQt5.QtWidgets import *
from Layouts.MainLayout import MainLayout

import sys


class MainWindow(QMainWindow):
    """Main window class for the application"""

    def __init__(self):
        super().__init__()

        self.status_bar = QStatusBar()
        self.outer_layout = MainLayout()

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.outer_layout)

        self.setWindowTitle("Main Window")
        self.setCentralWidget(self.central_widget)
        self.setStatusBar(self.status_bar)

        self.outer_layout.button.clicked.connect(self.show_message)

    def show_message(self):
        first_name = self.outer_layout.input_layout.first_name_input.text()
        surname = self.outer_layout.input_layout.surname_input.text()
        self.status_bar.showMessage("Hello, {first_name} {surname}".format(first_name=first_name, surname=surname))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()