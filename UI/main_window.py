from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import QTimer


from UI.player_panel import PlayerPanel
from UI.skill_panel import SkillPanel
from UI.inventory_panel import InventoryPanel
from UI.page_stack import PageStack
from UI.action_panel import ActionPanel
from UI.activity_panel import ActivityPanel
from UI.sidebar import Sidebar



class MainWindow(QMainWindow):
    """
    Main application window.

    Responsible for:
    - arranging UI panels
    - connecting signals
    - updating the game loop
    - saving on exit
    """


    def __init__(self, game):

        super().__init__()

        self.game = game


        self.setWindowTitle(
            "Idle RPG"
        )


        self.resize(
            1000,
            650
        )


        self.setup_ui()

        self.connect_signals()

        self.start_timer()



    def setup_ui(self):

        central = QWidget()

        self.setCentralWidget(
            central
        )


        main_layout = QHBoxLayout()

        central.setLayout(
            main_layout
        )


        # -----------------------
        # Sidebar
        # -----------------------

        self.sidebar = Sidebar()

        main_layout.addWidget(
            self.sidebar
        )


        # -----------------------
        # Main content
        # -----------------------

        content_layout = QVBoxLayout()


        main_layout.addLayout(
            content_layout,
            3
        )


        # Activity buttons

        self.activity_panel = ActivityPanel(self.game)

        content_layout.addWidget(
            self.activity_panel
        )


        # Current action

        self.action_panel = ActionPanel()

        content_layout.addWidget(
            self.action_panel
        )



        # -----------------------
        # Right information panel
        # -----------------------


        self.player_panel = PlayerPanel(
            self.game
        )

        self.skill_panel = SkillPanel(
            self.game
        )

        self.inventory_panel = InventoryPanel(
            self.game
        )


        self.pages = PageStack()


        self.pages.add_page(
            "player",
            self.player_panel
        )


        self.pages.add_page(
            "skills",
            self.skill_panel
        )


        self.pages.add_page(
            "inventory",
            self.inventory_panel
        )


        info_layout = QVBoxLayout()


        info_layout.addWidget(
            self.pages
        )


        main_layout.addLayout(
            info_layout,
            2
        )


    def connect_signals(self):

        """
        Connects UI events to game actions.
        """


        self.activity_panel.action_selected.connect(
            self.game.start_action
        )


        self.activity_panel.stop_requested.connect(
            self.game.stop_action
        )

        self.sidebar.page_changed.connect(
            self.pages.show_page
        )



    def start_timer(self):

        self.timer = QTimer()


        self.timer.timeout.connect(
            self.update_game
        )


        self.timer.start(
            100
        )



    def update_game(self):

        result = self.game.update()


        if result:

            self.reward_label.setText(
                f"+{result['amount']} {result['item']}\n"
                f"+{result['xp']} XP"
            )


        if self.game.skill_level_changed():

            self.activity_panel.refresh()


        self.refresh()



    def refresh(self):

        self.player_panel.refresh()

        self.skill_panel.refresh()

        self.inventory_panel.refresh()

        self.action_panel.update_action(
            self.game.action_state
        )



    def closeEvent(self, event):

        print(
            "Saving game..."
        )


        self.game.save()


        print(
            "Save complete."
        )


        event.accept()