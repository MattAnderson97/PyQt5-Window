from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    """custom line edit object which implements the focusInEvent() and focusOutEvent() methods"""

    def __init__(self):
        super().__init__()

    def focusInEvent(self, e):
        self.setStyleSheet("border: 1px solid #43a047;")
        super(LineEdit, self).focusInEvent(e)

    def focusOutEvent(self, e):
        self.setStyleSheet("")
        super(LineEdit, self).focusOutEvent(e)