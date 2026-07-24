from dataclasses import dataclass, field


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

    tools: dict[str, int] = field(
        default_factory=dict
    )

    level_required: int = 1

    xp: float = 0

    interval: float = 1

    description: str = ""