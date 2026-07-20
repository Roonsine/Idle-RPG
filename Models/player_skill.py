from dataclasses import dataclass


@dataclass
class PlayerSkill:
    """
    Represents a player's progress in one skill.
    """

    skill_id: str

    level: int = 1

    xp: float = 0

    mastery_level: int = 1

    mastery_xp: float = 0


    def add_xp(self, amount: float):
        """
        Add experience and check for level ups.
        """

        self.xp += amount

        self.check_level_up()


    def check_level_up(self):
        """
        Checks whether the player should gain levels.

        Temporary formula.
        Will be replaced by the Melvor/OSRS XP curve.
        """

        while self.xp >= self.xp_for_next_level():

            self.level += 1


    def xp_for_next_level(self):
        """
        Temporary XP requirement.

        Level 1 -> 2 = 100 XP
        Level 2 -> 3 = 200 XP
        etc.

        This will later be replaced.
        """

        return self.level * 100