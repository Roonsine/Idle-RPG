from dataclasses import dataclass


@dataclass
class Rock:
    """
    A mineable resource.
    """

    id: str

    name: str

    level_required: int

    xp: float

    interval: float

    ore_item_id: str