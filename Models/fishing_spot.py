from dataclasses import dataclass
from Models.fishing_spot_entry import FishingSpotEntry

@dataclass(slots=True, frozen=True)
class FishingSpot:
    id: str
    name: str
    interval: float
    level_required: int
    fish: list[FishingSpotEntry]