from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Fish:
    id: str
    name: str
    level_required: int
    xp: float
    item_id: str
    weight: float = 1.0
    
