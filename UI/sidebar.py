from UI.skill_selector import SkillSelector

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame
from PySide6.QtCore import Signal



class Sidebar(QWidget):

    paged_changed = Signal(str)

    def __init__(self, game):

        super().__init__()

        self.game = game

        self.main_layout = QVBoxLayout()

        self.setLayout(
            self.main_layout
        )

        player_button = QPushButton(
            "Player"
        )

        player_button.clicked.connect(  
            lambda: self.paged_changed.emit("player")
        )

        skills_button = QPushButton(
            "Skills"
        )

        skills_button.clicked.connect(
            lambda: self.paged_changed.emit("skills")
        )

        inventory_button = QPushButton(
            "Inventory"
        )

        inventory_button.clicked.connect(
            lambda: self.paged_changed.emit("inventory")
        )

        self.main_layout.addWidget(
            player_button
        )
        self.main_layout.addWidget(
            skills_button
        )
        self.main_layout.addWidget(
            inventory_button
        )


        seperator = QFrame()
        seperator.setFrameShape(QFrame.Shape.HLine)

        self.main_layout.addWidget(
            seperator
        )

        self.skill_selector = SkillSelector(
            game
        )


        self.main_layout.addWidget(
            self.skill_selector
        )
    