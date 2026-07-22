from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class PlayerPanel(QWidget):
    """
    Displays player information.
    """


    def __init__(self, game):

        super().__init__()

        self.game = game

        self.main_layout = QVBoxLayout()

        self.setLayout(
            self.main_layout
        )


        self.label = QLabel()

        self.main_layout.addWidget(
            self.label
        )


        self.refresh()



    def refresh(self):

        player = self.game.player


        if player is None:
            return


        self.label.setText(
            f"""
Player:
{player.name}

Gold:
{player.gold}
"""
        )