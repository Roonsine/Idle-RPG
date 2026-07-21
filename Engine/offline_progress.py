from datetime import datetime


class OfflineProgressCalculator:

    def calculate(self, game, save_data):
        """
        Calculate rewards earned while offline.
        """
        if save_data.current_action == None:
            return None
        last_saved = datetime.fromisoformat(
        save_data.last_saved
        )

        now = datetime.now()

        elapsed_seconds = (
                now - last_saved
            ).total_seconds()
        return elapsed_seconds