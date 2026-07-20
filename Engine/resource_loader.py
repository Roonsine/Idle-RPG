"""
Loads JSON data and converts it into game models.
"""

from pathlib import Path
import json

from Models import (
    Item,
    Tree,
    SkillDefinition,
    Monster,
    Drop,
    Recipe,
    Equipment
)

from Engine.registry import Registry
from Engine.game_data import GameData


class ResourceLoader:

    """
    Responsible for loading all static game content.
    """

    def __init__(self, data_directory: Path):

        self.data_directory = data_directory


    def load_json(self, filename: str):

        path = self.data_directory / filename

        if not path.exists():
            raise FileNotFoundError(
                f"Missing data file: {path}"
            )

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)


    def load_items(self):

        registry = Registry()

        for entry in self.load_json("items.json"):

            item = Item(**entry)

            registry.register(item)

        return registry


    def load_skills(self):

        registry = Registry()

        for entry in self.load_json("skills.json"):

            skill = SkillDefinition(**entry)

            registry.register(skill)

        return registry


    def load_trees(self):

        registry = Registry()

        for entry in self.load_json("trees.json"):

            tree = Tree(**entry)

            registry.register(tree)

        return registry


    def load_monsters(self):

        registry = Registry()

        for entry in self.load_json("monsters.json"):

            drops = []

            for drop_data in entry["drops"]:

                drops.append(
                    Drop(**drop_data)
                )

            entry["drops"] = drops

            monster = Monster(**entry)

            registry.register(monster)

        return registry


    def load_recipes(self):

        registry = Registry()

        for entry in self.load_json("recipes.json"):

            recipe = Recipe(**entry)

            registry.register(recipe)

        return registry


    def load_equipment(self):

        registry = Registry()

        for entry in self.load_json("equipment.json"):

            equipment = Equipment(**entry)

            registry.register(equipment)

        return registry


    def load_all(self):

        """
        Loads the entire game database.
        """

        return GameData(

            items=self.load_items(),

            skills=self.load_skills(),

            trees=self.load_trees(),

            monsters=self.load_monsters(),

            recipes=self.load_recipes(),

            equipment=self.load_equipment()
        )