from dataclasses import dataclass, field

from Player.inventory import Inventory
from Models.player_skill import PlayerSkill


@dataclass
class Player:
    """
    Represents the current player state.

    This stores progress only.
    Game actions happen elsewhere.
    """

    name: str

    inventory: Inventory = field(
        default_factory=Inventory
    )

    skills: dict[str, PlayerSkill] = field(
        default_factory=dict
    )

    equipment: dict[str, str] = field(
        default_factory=dict
    )

    gold: int = 0