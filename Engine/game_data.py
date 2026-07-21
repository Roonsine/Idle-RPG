from dataclasses import dataclass

from Engine.registry import Registry


@dataclass
class GameData:
    """
    Container for all loaded game content.

    Every system in the game will access
    content through this object.
    """

    items: Registry

    skills: Registry

    trees: Registry

    monsters: Registry

    recipes: Registry

    equipment: Registry

    rocks: Registry