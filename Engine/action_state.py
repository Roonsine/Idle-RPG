from dataclasses import dataclass
from datetime import datetime


@dataclass
class ActionState:
    """
    Stores information about the currently running action.
    """

    action_type: str

    target_id: str

    action_id: str

    action_name: str

    started_at: datetime

    completes_at: datetime

    completed_count: int = 0


    def progress(self):

        now = datetime.now()

        total = (
            self.completes_at -
            self.started_at
        ).total_seconds()

        elapsed = (
            now -
            self.started_at
        ).total_seconds()


        if total <= 0:
            return 1.0


        return min(
            elapsed / total,
            1.0
        )


    def remaining_time(self):

        remaining = (
            self.completes_at -
            datetime.now()
        ).total_seconds()

        return max(
            remaining,
            0
        )


    def complete(self):

        self.completed_count += 1