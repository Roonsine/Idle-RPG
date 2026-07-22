from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton
)

from PySide6.QtCore import Signal


class SkillSelector(QWidget):
    """
    Displays available skills.
    """

    skill_selected = Signal(str)


    def __init__(self, game):

        super().__init__()

        self.game = game

        self.main_layout = QVBoxLayout()

        self.setLayout(
            self.main_layout
        )

        self.buttons = {}

        self.build()

    def build(self):

        if self.game.player is None:
            return


        for skill_id in self.game.player.skills:

            button = QPushButton(
                skill_id.title()
            )


            button.clicked.connect(
                lambda checked=False,
                s=skill_id:
                self.skill_selected.emit(s)
            )


            self.buttons[skill_id] = button


            self.main_layout.addWidget(
                button
            )