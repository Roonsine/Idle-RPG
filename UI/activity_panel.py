from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea
)


class ActivityPanel(QWidget):

    action_selected = Signal(
        str,
        str
    )

    stop_requested = Signal()


    def __init__(self, game):

        super().__init__()


        self.game = game


        self.buttons = []


        self.layout = QVBoxLayout() # type: ignore

        self.setLayout(
            self.layout # type: ignore
        )


        self.build()



    def build(self):

        title = QLabel(
            "Activities"
        )

        self.layout.addWidget( # type: ignore
            title
        )


        self.create_actions()



        stop = QPushButton(
            "Stop Action"
        )

        stop.clicked.connect(
            self.stop_requested.emit
        )


        self.layout.addWidget( # type: ignore
            stop
        )



    def create_actions(self):

        if self.game.data is None:
            return


        # --------------------
        # Woodcutting
        # --------------------

        for tree_id in self.game.data.trees:

            tree = self.game.data.trees.get(
                tree_id
            )


            button = QPushButton()


            button.setText(
                f"🌳 {tree.name}"
            )


            required = tree.level_required


            current = (
                self.game.player.skills["woodcutting"].level
            )


            if current >= required:

                button.clicked.connect(

                    lambda checked=False,
                    t=tree_id:
                    self.action_selected.emit(
                        "woodcutting",
                        t
                    )

                )

            else:

                button.setText(
                    f"🔒 {tree.name}\n"
                    f"Requires Level {required}"
                )

                button.setEnabled(
                    False
                )


            self.layout.addWidget( # type: ignore
                button
            )


        # --------------------
        # Mining
        # --------------------

        for rock_id in self.game.data.rocks:

            rock = self.game.data.rocks.get(
                rock_id
            )


            button = QPushButton()


            button.setText(
                f"⛏ {rock.name}"
            )


            required = rock.level_required


            current = (
                self.game.player.skills["mining"].level
            )


            if current >= required:

                button.clicked.connect(

                    lambda checked=False,
                    r=rock_id:
                    self.action_selected.emit(
                        "mining",
                        r
                    )

                )


            else:

                button.setText(
                    f"🔒 {rock.name}\n"
                    f"Requires Level {required}"
                )

                button.setEnabled(
                    False
                )


            self.layout.addWidget( # type: ignore
                button
            )

    def refresh(self):

        for button in self.findChildren(QPushButton):

            button.deleteLater()


        self.create_actions()