from dataclasses import dataclass
import config




@dataclass
class PlayerSkill:

    skill_id: str

    level: int

    xp: float

    mastery_level: int = 1

    mastery_xp: float = 0



    def add_xp(self, amount):

        if self.level >= config.MAX_LEVEL:

            self.level = config.MAX_LEVEL

            self.xp = 0

            return


        self.xp += amount


        while self.level < config.MAX_LEVEL:

            required = self.xp_required(
                self.level
            )


            if self.xp < required:

                break


            self.xp -= required

            self.level += 1



    def xp_required(
        self,
        level
    ):

        return level * level * 100