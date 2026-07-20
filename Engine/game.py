from pathlib import Path

from Engine.resource_loader import ResourceLoader
from Engine.game_data import GameData
from Engine.action_manager import ActionManager

from Player import Player
from Models.player_skill import PlayerSkill


class Game:
    """
    Main game controller.

    Holds:
    - loaded content
    - current player
    - game state
    """

    def __init__(self, data_directory: Path):

        self.loader = ResourceLoader(
            data_directory
        )

        self.data: GameData | None = None

        self.player: Player | None = None

        self.action_manager = ActionManager()

    def update(self):

        if self.player is None:
            return


        result = self.action_manager.tick(
            self.player,
            self.data
        )


        return result

    def load(self):
        """
        Load all static game content.
        """

        self.data = self.loader.load_all()


    def create_player(self, name: str):
        """
        Create a new player.

        Gives the player every available skill
        at level 1.
        """

        if self.data is None:
            raise RuntimeError(
                "Game data has not been loaded."
            )


        self.player = Player(
            name=name
        )


        for skill_id in self.data.skills:

            skill = PlayerSkill(
                skill_id=skill_id,
                level=1,
                xp=0
            )

            self.player.skills[skill_id] = skill


    def start(self):
        """
        Start the game.
        """

        if self.data is None:
            self.load()


        if self.player is None:
            self.create_player(
                "Player"
            )