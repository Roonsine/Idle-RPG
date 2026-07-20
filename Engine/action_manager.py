import time


class ActionManager:
    """
    Handles repeating idle actions.
    """

    def __init__(self):

        self.current_action = None

        self.start_time = None

        self.completed_actions = 0


    def start(self, action):

        self.current_action = action

        self.start_time = time.time()

        self.completed_actions = 0


    def stop(self):

        self.current_action = None

        self.start_time = None


    def is_active(self):

        return self.current_action is not None


    def progress(self):

        if not self.is_active():
            return 0

        elapsed = time.time() - self.start_time

        return min(
            elapsed / self.current_action.interval,
            1
        )


    def finished(self):

        return (
            self.is_active()
            and self.progress() >= 1
        )


    def tick(self, player, game_data):
        """
        Checks whether the action completed.

        If yes:
        - reward player
        - restart timer
        """

        if not self.finished():

            return None


        result = self.current_action.execute(
            player,
            game_data
        )


        self.completed_actions += 1


        # restart timer

        self.start_time = time.time()


        return result