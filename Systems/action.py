from dataclasses import dataclass


@dataclass
class Action:
    """
    Base class for all timed player actions.

    Examples:
    - Woodcutting
    - Mining
    - Cooking
    - Combat
    """

    id: str

    name: str

    interval: float


    def can_execute(self, player, game_data):
        """
        Checks if the player can perform this action.

        Child actions override this.
        """

        return True


    def execute(self, player, game_data):
        """
        Performs the action.

        Child actions must override this.
        """

        raise NotImplementedError(
            "Action must implement execute()"
        )