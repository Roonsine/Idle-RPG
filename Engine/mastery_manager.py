class MasteryManager:

    def __init__(self):
        pass


    def add_mastery_xp(
        self,
        skill,
        amount: float
    ):

        old_level = skill.mastery_level

        skill.mastery_xp += amount


        new_level = self.level_from_mastery_xp(
            skill.mastery_xp
        )

        skill.mastery_level = new_level


        result = {
            "skill_id": skill.skill_id,
            "xp_gained": amount,
            "old_mastery_level": old_level,
            "new_mastery_level": new_level,
            "level_up": new_level > old_level
        }


        print(
            "MASTERY EVENT:",
            result
        )


        return result


    def level_from_mastery_xp(
        self,
        xp: float
    ):

        level = 0

        while xp >= self.xp_for_level(level + 1):
            level += 1

        return level


    def xp_for_level(
        self,
        level: int
    ):

        return level * level * 100