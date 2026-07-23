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
    Equipment,
    Rock,
    Fish,
    FishingSpot,
    FishingSpotEntry
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

    def load_registry(self, filename, model_cls):

        registry = Registry()

        for entry in self.load_json(filename):
            registry.register(model_cls(**entry))

        return registry

    def load_items(self):
        return self.load_registry("items.json", Item)


    def load_skills(self):
        return self.load_registry("skills.json", SkillDefinition)


    def load_trees(self):
        return self.load_registry("trees.json", Tree)

    
    def load_rocks(self):
        return self.load_registry("rocks.json", Rock)

    def load_fish(self):
        registry = Registry()

        for entry in self.load_json("fish.json"):

            fish = Fish(**entry)

            registry.register(fish)

        return registry
    
    def load_fishing_spots(self):

        registry = Registry()

        for entry in self.load_json("fishing_spots.json"):

            fish_entries = []

            for fish_data in entry["fish"]:

                fish_entries.append(
                    FishingSpotEntry(**fish_data)
                )

            entry["fish"] = fish_entries

            spot = FishingSpot(**entry)

            registry.register(spot)

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
        return self.load_registry("recipes.json", Recipe)


    def load_equipment(self):
        return self.load_registry("equipment.json", Equipment)

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

            equipment=self.load_equipment(),

            rocks= self.load_rocks(),

            fishing_spots=self.load_fishing_spots(),
            
            fish=self.load_fish()
        )