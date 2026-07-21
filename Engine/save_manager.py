import json
from pathlib import Path
from dataclasses import asdict

from Engine.serializer import Serializer


class SaveManager:
    """
    Handles saving and loading game state.
    """

    def __init__(self, save_directory):

        self.save_directory = Path(save_directory)

        self.save_directory.mkdir(
            parents=True,
            exist_ok=True
        )


    @property
    def save_file(self):

        return self.save_directory / "player.json"


    def exists(self):
        """
        Checks if a save file exists.
        """

        return self.save_file.exists()


    def save(self, game):
        """
        Saves the current game state.
        """

        save = Serializer.create_save(
            game.player,
            game.action_state
        )

        with open(
            self.save_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                asdict(save),
                file,
                indent=4
            )


    def load(self):
        """
        Loads save data from disk.

        Returns:
            dict | None
        """

        if not self.exists():
            return None


        with open(
            self.save_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)