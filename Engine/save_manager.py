import json
from pathlib import Path
from dataclasses import asdict

from Engine.serializer import Serializer


class SaveManager:

    def __init__(self, save_directory):

        self.save_directory = Path(save_directory)

        self.save_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    @property
    def save_file(self):

        return self.save_directory / "player.json"

    def save(self, game):

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