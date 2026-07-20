from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Equipment:
    """
    Static definition of equipment stats.

    References an Item through item_id.
    """

    id: str

    item_id: str

    slot: str

    attack_bonus: int = 0

    strength_bonus: int = 0

    defence_bonus: int = 0

    magic_bonus: int = 0

    ranged_bonus: int = 0

    description: str = ""