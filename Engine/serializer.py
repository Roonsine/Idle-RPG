from datetime import datetime

from Engine.save_data import SaveData


class Serializer:

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

        save.inventory = dict(player.inventory.items)

        save.equipment = dict(player.equipment)

        if action_state is not None:

            save.current_action = {
                "action_id": action_state.action_id,
                "completed": action_state.completed_count,
                "started_at": action_state.started_at.isoformat(),
                "completes_at": action_state.completes_at.isoformat()
            }

        save.last_saved = datetime.now().isoformat()

        return save