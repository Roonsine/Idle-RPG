from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class InventoryPanel(QWidget):

    def __init__(self, game):

        super().__init__()

        self.game = game


        layout = QVBoxLayout()

        self.setLayout(
            layout
        )


        self.label = QLabel()

        layout.addWidget(
            self.label
        )


        self.refresh()



    def refresh(self):

        player = self.game.player


        if player is None:
            return


        text = "Inventory:\n\n"


        for item, amount in player.inventory.items.items():

            text += (
                f"{item}: {amount}\n"
            )


        self.label.setText(
            text
        )