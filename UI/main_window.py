from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)

from PySide6.QtCore import QTimer


from UI.player_panel import PlayerPanel
from UI.skill_panel import SkillPanel
from UI.inventory_panel import InventoryPanel



class MainWindow(QMainWindow):
    """
    Main game window.

    Handles:
    - UI layout
    - game timer
    - user input
    - refreshing panels
    """


    def __init__(self, game):

        super().__init__()

        self.game = game


        self.setWindowTitle(
            "Idle RPG"
        )


        self.resize(
            900,
            600
        )


        self.setup_ui()


        self.start_timer()



    def setup_ui(self):
        """
        Builds the window layout.
        """


        central = QWidget()

        self.setCentralWidget(
            central
        )


        main_layout = QVBoxLayout()


        central.setLayout(
            main_layout
        )


        # -------------------------
        # Top section
        # -------------------------

        top_layout = QHBoxLayout()


        self.player_panel = PlayerPanel(
            self.game
        )


        self.skill_panel = SkillPanel(
            self.game
        )


        self.inventory_panel = InventoryPanel(
            self.game
        )


        top_layout.addWidget(
            self.player_panel
        )


        top_layout.addWidget(
            self.skill_panel
        )


        top_layout.addWidget(
            self.inventory_panel
        )


        main_layout.addLayout(
            top_layout
        )



        # -------------------------
        # Action display
        # -------------------------

        self.action_label = QLabel()

        main_layout.addWidget(
            self.action_label
        )



        # -------------------------
        # Buttons
        # -------------------------

        button_layout = QHBoxLayout()


        self.tree_button = QPushButton(
            "Chop Normal Tree"
        )


        self.tree_button.clicked.connect(
            self.start_tree
        )


        button_layout.addWidget(
            self.tree_button
        )



        self.mine_button = QPushButton(
            "Mine Copper Rock"
        )


        self.mine_button.clicked.connect(
            self.start_mining
        )


        button_layout.addWidget(
            self.mine_button
        )



        self.stop_button = QPushButton(
            "Stop Action"
        )


        self.stop_button.clicked.connect(
            self.stop_action
        )


        button_layout.addWidget(
            self.stop_button
        )


        main_layout.addLayout(
            button_layout
        )



    def start_timer(self):
        """
        Creates the game update loop.
        """


        self.timer = QTimer()


        self.timer.timeout.connect(
            self.update_game
        )


        # update every second

        self.timer.start(
            1000
        )



    def update_game(self):
        """
        Updates engine then refreshes UI.
        """


        self.game.update()


        self.refresh()



    def refresh(self):
        """
        Refreshes all UI components.
        """


        self.player_panel.refresh()

        self.skill_panel.refresh()

        self.inventory_panel.refresh()


        self.refresh_action()



    def refresh_action(self):

        state = self.game.action_state


        if state is None:

            self.action_label.setText(
                "Action: None"
            )

            return



        self.action_label.setText(
            f"""
Action:
{state.action_name}

Progress:
{state.progress() * 100:.1f}%

Time Remaining:
{state.remaining_time():.1f}s
"""
        )



    def start_tree(self):

        self.game.start_action(
            "woodcutting",
            "normal_tree"
        )



    def start_mining(self):

        self.game.start_action(
            "mining",
            "copper_rock"
        )



    def stop_action(self):

        self.game.stop_action()



    def closeEvent(self, event):
        """
        Saves when the window closes.
        """


        print(
            "Saving game..."
        )


        self.game.save()


        print(
            "Save complete."
        )


        event.accept()