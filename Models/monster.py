from dataclasses import dataclass
from typing import List

from .drop import Drop


@dataclass(slots=True, frozen=True)
class Monster:
    """
    Static definition of a combat enemy.

    Loaded from monsters.json.

    This describes what a monster IS,
    not the combat happening against it.
    """

    id: str

    name: str

    hitpoints: int

    attack_level: int

    strength_level: int

    defence_level: int

    attack_speed: float

    drops: List[Drop]

    description: str = ""

    image: str = ""