from dataclasses import dataclass

@dataclass
class Action:

    id: str

    name: str

    category: str

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
    

    def execute_many(
        self,
        player,
        game_data,
        amount
    ):
        """
        Executes an action multiple times.

        Used for offline progression.
        """

        results = []

        for _ in range(amount):

            result = self.execute(
                player,
                game_data
            )

            results.append(result)

        return results