from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Drop:
    """
    Defines a possible item reward.

    Used by:
    - Monsters
    - Trees
    - Mining nodes
    - Fishing spots
    - Other reward systems

    This is only the definition of a drop,
    not the actual item received.
    """

    item_id: str

    chance: float

    min_quantity: int = 1

    max_quantity: int = 1