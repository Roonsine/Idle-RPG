from datetime import datetime

from Engine.save_data import SaveData
from Player import Player
from Models.player_skill import PlayerSkill


class Serializer:
    """
    Converts game objects to and from save data.
    """


    @staticmethod
    def create_save(player, action_state=None):

        save = SaveData()

        save.player_name = player.name

        save.gold = player.gold


        save.skills = {
            skill_id: {
                "level": skill.level,
                "xp": skill.xp,
                "mastery_level": skill.mastery_level,
                "mastery_xp": skill.mastery_xp
            }
            for skill_id, skill in player.skills.items()
        }


        save.inventory = dict(
            player.inventory.items
        )


        save.equipment = dict(
            player.equipment
        )


        if action_state is not None:

            save.current_action = {

                "action_id": action_state.action_id,

                "action_type": action_state.action_type,

                "target_id": action_state.target_id,

                "action_name": action_state.action_name,

                "completed": action_state.completed_count,

                "started_at": (
                    action_state.started_at.isoformat()
                ),

                "completes_at": (
                    action_state.completes_at.isoformat()
                )
            }


        save.last_saved = (
            datetime.now().isoformat()
        )


        return save



    @staticmethod
    def load_player(data):
        """
        Rebuilds a Player object from save data.
        """

        player = Player(
            name=data["player_name"]
        )


        player.gold = data.get(
            "gold",
            0
        )


        for skill_id, skill_data in data.get(
            "skills",
            {}
        ).items():

            player.skills[skill_id] = PlayerSkill(

                skill_id=skill_id,

                level=skill_data["level"],

                xp=skill_data["xp"],

                mastery_level=skill_data.get(
                    "mastery_level",
                    1
                ),

                mastery_xp=skill_data.get(
                    "mastery_xp",
                    0
                )
            )


        player.inventory.items = data.get(
            "inventory",
            {}
        )


        player.equipment = data.get(
            "equipment",
            {}
        )


        return player