from dataclasses import dataclass


@dataclass
class Tree:

    id: str

    name: str

    level_required: int

    xp: float

    interval: float

    amount: int

    log_item_id: str