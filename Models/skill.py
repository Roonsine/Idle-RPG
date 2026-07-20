from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SkillDefinition:
    """
    Static definition of a skill.

    Loaded from skills.json.

    This describes the skill itself,
    not a player's progress.
    """

    id: str

    name: str

    description: str

    max_level: int = 99

    icon: str = ""