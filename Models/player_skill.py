from dataclasses import dataclass


@dataclass
class PlayerSkill:
    """
    Represents a player's progress in a skill.

    This is saved with the player.

    It references a SkillDefinition
    through skill_id.
    """

    skill_id: str

    level: int = 1

    xp: float = 0.0

    mastery_level: int = 1

    mastery_xp: float = 0.0