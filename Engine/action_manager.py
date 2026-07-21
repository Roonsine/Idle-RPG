from datetime import datetime, timedelta

from Engine.action_state import ActionState
from Systems.action import Action


class ActionManager:
    """
    Handles repeating idle actions.
    """


    def __init__(self):

        self.current_action: Action | None = None

        self.state: ActionState | None = None


    def start(self, action, action_type, target_id):

        self.current_action = action

        now = datetime.now()

        self.state = ActionState(

            action_type= action_type,

            target_id=target_id,

            action_id=action.id,

            action_name=action.name,

            started_at=now,

            completes_at=(
                now +
                timedelta(
                    seconds=action.interval
                )
            )
        )


    def stop(self):

        self.current_action = None

        self.state = None


    def is_active(self):

        return self.current_action is not None


    def progress(self):

        if self.state is None:
            return 0

        return self.state.progress()


    def finished(self):

        if self.state is None:
            return False

        return self.state.progress() >= 1


    def tick(self, player, game_data):

        if self.current_action is None:
            return None


        if not self.finished():
            return None


        result = self.current_action.execute(
            player,
            game_data
        )


        if self.state is not None:
            self.state.complete()


        # restart timer

        now = datetime.now()

        if self.state is not None:

            self.state.started_at = now

            self.state.completes_at = (
                now +
                timedelta(
                    seconds=self.current_action.interval
                )
            )

        return result