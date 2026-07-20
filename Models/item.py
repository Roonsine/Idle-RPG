from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True, frozen=True)
class Item:
    """
    Static definition of an item.

    Loaded from items.json.

    This represents what an item IS,
    not how many a player owns.
    """

    id: str

    name: str

    description: str

    value: int

    category: str

    rarity: str

    stackable: bool = True

    icon: str = ""

    equip_slot: Optional[str] = None