from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar,
    QPushButton
)

from PySide6.QtCore import Signal

class ActionPanel(QWidget):
    """
    Displays the currently running action.
    """

    stop_requested = Signal()

    def __init__(self, game):

        super().__init__()

        self.game = game
        self.main_layout = QVBoxLayout(self)

        self.title = QLabel("Current Action")
        self.main_layout.addWidget(self.title)

        self.action_name = QLabel("None")

        self.main_layout.addWidget(self.action_name)

        self.progress = QProgressBar()

        self.progress.setRange(0, 100)
        self.progress.setFormat("%p%")

        self.main_layout.addWidget(self.progress)

        self.remaining = QLabel(
            "Time Remaining: --"
            
        )

        stop = QPushButton(
            "Stop Action"
        )

        stop.clicked.connect(
            self.stop_requested.emit
        )


        self.main_layout.addWidget(
            stop
        )
        self.main_layout.addWidget(self.remaining)

        self.reward_label = QLabel(
            "Last Reward: None"
        )

        self.main_layout.addWidget(self.reward_label)

    def refresh(self):

        state = self.game.action_state

        if state is None:

            self.action_name.setText("None")

            self.progress.setValue(0)

            self.remaining.setText(
                "Time Remaining: --"
            )

            return


        self.action_name.setText(
            state.action_name
        )


        self.progress.setValue(
            int(state.progress() * 100)
        )


        self.remaining.setText(
            f"Time Remaining: "
            f"{state.remaining_time():.1f}s"
        )
    def show_reward(self, reward):

        if not reward:
            return


        # Handle failed actions

        if reward.get("success") is False:

            self.reward_label.setText(
                reward.get(
                    "message",
                    "Action stopped."
                )
            )

            return


        # Normal reward

        self.reward_label.setText(
            f"+{reward['amount']} {reward['item']}\n"
            f"+{reward.get('xp', 0)} XP"
        )