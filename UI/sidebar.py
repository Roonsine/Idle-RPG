from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout
)


class Sidebar(QWidget):

    page_changed = Signal(str)

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        buttons = [

            ("👤 Player","player"),

            ("⚒ Skills","skills"),

            ("🎒 Inventory","inventory"),

            ("⚔ Equipment","equipment"),

            ("⚙ Settings","settings")

            ]

        for text, page in buttons:

            button = QPushButton(text)

            button.clicked.connect(

                lambda _, p=page:
                self.page_changed.emit(p)
            )

            layout.addWidget(button)

        layout.addStretch()