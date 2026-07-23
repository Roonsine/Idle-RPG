from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class FishingSpotEntry:
    fish_id: str
    weight: float