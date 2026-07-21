from pathlib import Path

from Engine.serializer import Serializer
from Engine.save_manager import SaveManager
from Engine.resource_loader import ResourceLoader
from Engine.game_data import GameData
from Engine.action_manager import ActionManager
from Engine.action_factory import ActionFactory
from Engine.action_registry import ActionRegistry

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

        self.save_manager = SaveManager("save")

        self.action_manager = ActionManager()
        self.action_factory = ActionFactory()
        self.action_registry = ActionRegistry()


    def start(self):
        if self.player is None:

            if self.save_manager.exists():

                data = self.save_manager.load()

                self.player = Serializer.load_player(data)

            else:

                self.create_player("Player")

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
        self.setup_actions()

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

    def load_player(self):
        """
        Loads player data from save file.
        """

        save_data = self.save_manager.load()

        if save_data is None:
            return False

        # temporary until we implement serializer loading

        self.player = Player(
            name=save_data.player_name
        )

        return True

    def save(self):

        self.save_manager.save(self)

    @property
    def action_state(self):

        return self.action_manager.state
    
    def start_action(self, action_type, target_id):
        """
        Starts a player activity.
        """

        if self.data is None:
            raise RuntimeError(
                "Game data not loaded."
            )


        if self.player is None:
            raise RuntimeError(
                "Player does not exist."
            )


        action = self.action_registry.create(
        action_type,
        target_id,
        self.data
    )


        self.action_manager.start(
            action,
            action_type,
            target_id
        )


        return action
    
    def setup_actions(self):

        self.action_registry.register(
            "woodcutting",
            self.action_factory.create_tree_action
        )

        self.action_registry.register(
        "mining",
        self.action_factory.create_rock_action
    )

    def stop_action(self):
        """
        Stops the currently running action.
        """

        self.action_manager.stop()