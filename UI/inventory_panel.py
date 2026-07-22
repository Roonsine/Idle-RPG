from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class InventoryPanel(QWidget):

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


        text = "Inventory:\n\n"


        for item, amount in player.inventory.all_items().items():

            text += (
                f"{item}: {amount}\n"
            )


        self.label.setText(
            text
        )