from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):

    def __init__(self):
        super().__init__()

    def focusInEvent(self, e):
        self.setStyleSheet("border: 1px solid #43a047;")
        super(LineEdit, self).focusInEvent(e)

    def focusOutEvent(self, e):
        self.setStyleSheet("")
        super(LineEdit, self).focusOutEvent(e)