from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Tree:
    """
    Static definition of a woodcutting resource.

    Loaded from trees.json.

    This describes the tree itself,
    not the player's interaction with it.
    """

    id: str

    name: str

    level_required: int

    xp: float

    interval: float

    log_item_id: str

    depletion_chance: float = 0.0

    respawn_time: float = 0.0