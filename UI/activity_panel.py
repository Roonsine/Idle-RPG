from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea
)


class ActivityPanel(QWidget):

    action_selected = Signal(str,str)

    stop_requested = Signal()


    def __init__(self, game):

        super().__init__()

        self.game = game

        self.current_skill = "woodcutting"

        self.build()

    def build(self):

        self.main_layout = QVBoxLayout(self)

        title = QLabel("Activities")
        self.main_layout.addWidget(title)

        # Sroll area to support dozens of activities later.
        self.activity_scroll = QScrollArea()
        self.activity_scroll.setWidgetResizable(True)
        self.main_layout.addWidget(self.activity_scroll)

        self.button_container = QWidget()
        self.button_layout = QVBoxLayout(self.button_container)
        self.activity_scroll.setWidget(self.button_container)

        self.refresh()

    def set_skill(self, skill_id):

        if skill_id == self.current_skill:
            return

        self.current_skill = skill_id

        self.refresh()

    def create_actions(self):

        if self.current_skill == "woodcutting":

            self.create_tree_actions()


        elif self.current_skill == "mining":

            self.create_mining_actions()

    def create_tree_actions(self):

        for tree_id in self.game.data.trees:

            tree = self.game.data.trees.get(
                tree_id
            )


            button = QPushButton(
                f"🌳 {tree.name}"
            )


            button.clicked.connect(
                lambda checked=False,
                t=tree_id:
                self.action_selected.emit(
                    "woodcutting",
                    t
                )
            )


            self.button_layout.addWidget(
                button
            )
   
    def create_mining_actions(self):

        for rock_id in self.game.data.rocks:

            rock = self.game.data.rocks.get(
                rock_id
            )


            button = QPushButton(
                f"⛏ {rock.name}"
            )


            button.clicked.connect(
                lambda checked=False,
                r=rock_id:
                self.action_selected.emit(
                    "mining",
                    r
                )
            )


            self.button_layout.addWidget(
                button
            )
    
    def refresh(self):

        while self.button_layout.count():

            item = self.button_layout.takeAt(0)

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        self.create_actions()