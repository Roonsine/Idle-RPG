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

    def __init__(self):

        super().__init__()

        self.main_layout = QVBoxLayout(self)

        title = QLabel("Current Action")

        self.main_layout.addWidget(title)

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

    def update_action(self, state):

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

        if reward is None:
            return

        self.reward_label.setText(
            f"+{reward['amount']} {reward['item']}\n"
            f"+{reward['xp']} XP"
        )