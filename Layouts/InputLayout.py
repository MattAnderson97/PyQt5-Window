from PyQt5.QtWidgets import QGridLayout, QLabel
from CustomWidgets.LineEdit import LineEdit


class InputLayout(QGridLayout):
    """Layout for the input labels and text boxes"""

    def __init__(self):
        super().__init__()

        self.first_name_label = QLabel("Please enter your first name")
        self.first_name_input = LineEdit()
        self.first_name_input.setPlaceholderText("John")

        self.surname_label = QLabel("Please enter your surname  ")
        self.surname_input = LineEdit()
        self.surname_input.setPlaceholderText("Doe")

        self.addWidget(self.first_name_label, 0, 0)
        self.addWidget(self.first_name_input, 0, 1)
        self.addWidget(self.surname_label, 1, 0)
        self.addWidget(self.surname_input, 1, 1)