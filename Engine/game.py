from pathlib import Path

from Engine.offline_progress import OfflineProgress
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

        # Tracks skill levels for UI updates
        self.last_skill_levels = {}

        self.save_manager = SaveManager("save")

        self.offline_progress = OfflineProgress()

        self.action_manager = ActionManager()
        self.action_factory = ActionFactory()
        self.action_registry = ActionRegistry()


    def start(self):
        """
        Starts the game.

        Loads content first,
        then loads or creates player.
        """

        if self.data is None:
            self.load()


        if self.player is not None:
            return
        if self.save_manager.exists():

            data = self.save_manager.load()

            self.player = Serializer.load_player(data)

            self.initialize_skill_tracking()
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
            
        self.initialize_skill_tracking()

    def skill_level_changed(self):

        if self.player is None:
            return False


        for skill_id, skill in self.player.skills.items():

            old = self.last_skill_levels.get(
                skill_id,
                skill.level
            )


            if skill.level != old:

                self.last_skill_levels[skill_id] = skill.level

                return True


        return False
            
    def save(self):

        self.save_manager.save(self)

    def calculate_offline_progress(self, save_data):
        """
        Applies offline progress.
        """

        if self.player is None:
            return


        action_data = save_data.get(
            "current_action"
        )


        if action_data is None:
            return


        seconds = self.offline_progress.calculate_seconds_away(
            save_data.get("last_saved")
        )


        action = self.restore_action(
            action_data
        )


        if action is None:
            return


        completed = self.offline_progress.calculate_completions(
            seconds,
            action
        )


        if completed <= 0:
            return


        print(
            f"Offline completed actions: {completed}"
        )


        action.execute_many(
            self.player,
            self.data,
            completed
        )

    def restore_action(self, action_data):
        """
        Restores the action the player was doing
        when the game closed.
        """

        if action_data is None:
            return


        action = self.action_registry.create(
            action_data["action_type"],
            action_data["target_id"],
            self.data
        )


        self.action_manager.start(
            action,
            action_data["action_type"],
            action_data["target_id"]
        )


        return action

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
        print(
        "CREATED ACTION:",
        type(action)
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

    def initialize_skill_tracking(self):

        if self.player is None:
            return


        self.last_skill_levels = {
            skill_id: skill.level
            for skill_id, skill in self.player.skills.items()
        }