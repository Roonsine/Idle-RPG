from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Recipe:
    """
    Static definition of a production recipe.

    Loaded from recipes.json.

    Describes what materials are required
    and what is produced.
    """

    id: str

    name: str

    skill_id: str

    inputs: dict[str, int]

    outputs: dict[str, int]

    amount: int

    level_required: int

    xp: float

    interval: float

    description: str = ""