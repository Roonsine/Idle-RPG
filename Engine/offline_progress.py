from datetime import datetime


class OfflineProgress:
    """
    Handles calculating progress made while the game
    was closed.
    """


    def calculate_seconds_away(self, last_saved):
        """
        Calculates how long the player was offline.

        Args:
            last_saved:
                ISO formatted datetime string

        Returns:
            seconds offline
        """

        if last_saved is None:
            return 0


        saved_time = datetime.fromisoformat(
            last_saved
        )

        now = datetime.now()

        seconds = (
            now - saved_time
        ).total_seconds()


        return max(
            int(seconds),
            0
        )


    def calculate_completions(
        self,
        seconds_away,
        action
    ):
        """
        Calculates how many actions completed.

        Example:

        Tree takes 5 seconds

        Player away 60 seconds

        Result:
        12 logs
        """

        if action is None:
            return 0


        if action.interval <= 0:
            return 0


        return int(
            seconds_away /
            action.interval
        )