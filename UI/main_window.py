from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PySide6.QtCore import QTimer


from UI.skill_selector import SkillSelector
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

        self.sidebar = Sidebar(
            self.game
        )

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

        self.action_panel = ActionPanel(self.game)

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

        self.refreshables = [
            self.player_panel,
            self.skill_panel,
            self.inventory_panel,
            self.action_panel
        ]
        
        for panel in self.refreshables:
            panel.refresh()

    def connect_signals(self):

        self.sidebar.paged_changed.connect(
            self.pages.show_page
        )

        self.sidebar.skill_selector.skill_selected.connect(
            self.activity_panel.set_skill
        )

        self.activity_panel.action_selected.connect(
            self.game.start_action
        )

        self.action_panel.stop_requested.connect(
            self.game.stop_action
        )


        self.game.action_changed.connect(
            self.action_panel.refresh
        )

        self.game.action_completed.connect(
            self.action_panel.show_reward
        )

        self.game.skills_changed.connect(
            self.skill_panel.refresh
        )

        self.game.inventory_changed.connect(
            self.inventory_panel.refresh
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

        self.game.update()

        self.action_panel.refresh()

    def refresh(self):

        for panel in self.refreshables:
            panel.refresh()

    def closeEvent(self, event):

        print(
            "Saving game..."
        )


        self.game.save()


        print(
            "Save complete."
        )


        event.accept()