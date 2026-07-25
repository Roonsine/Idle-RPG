from dataclasses import dataclass

from Engine.xp_table import (
    level_from_xp
)


@dataclass
class PlayerSkill:

    skill_id: str

    level: int = 1

    xp: float = 0

    mastery_level: int = 1

    mastery_xp: float = 0


    def add_xp(
        self,
        amount: float
    ):

        old_level = self.level


        self.xp += amount


        self.level = level_from_xp(
            self.xp
        )


        result = {
            "skill_id": self.skill_id,
            "xp_gained": amount,
            "old_level": old_level,
            "new_level": self.level,
            "level_up": self.level > old_level
        }


        print(
            "XP EVENT:",
            result
        )


        return result