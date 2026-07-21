from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QProgressBar
)


class ActionPanel(QWidget):
    """
    Displays the currently running action.
    """

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Current Action")

        layout.addWidget(title)

        self.action_name = QLabel("None")

        layout.addWidget(self.action_name)

        self.progress = QProgressBar()

        self.progress.setRange(0, 100)
        self.progress.setFormat("%p%")

        layout.addWidget(self.progress)

        self.remaining = QLabel(
            "Time Remaining: --"
        )

        layout.addWidget(self.remaining)

        self.reward = QLabel(
            "Last Reward: None"
        )

        layout.addWidget(self.reward)

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

    def set_reward(self, result):

        if result is None:
            return

        self.reward.setText(
            f"+{result['amount']} {result['item']}\n"
            f"+{result['xp']} XP"
        )