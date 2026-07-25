class UnlockManager:

    def __init__(self):

        self.skill_sources = {
            "woodcutting": (
                "trees",
                "tree"
            ),

            "mining": (
                "rocks",
                "rock"
            ),

            "fishing": (
                "fish",
                "fish"
            ),

            "cooking": (
                "recipes",
                "recipe"
            ),

            "smithing": (
                "recipes",
                "recipe"
            )
        }

    def check_unlocks(
        self,
        skill_event,
        game_data
    ):

        skill_id = skill_event["skill_id"]

        source = self.skill_sources.get(
            skill_id
        )

        if source is None:
            return []

        registry_name, unlock_type = source

        registry = getattr(
            game_data,
            registry_name
        )

        unlocks = []

        for obj in registry.values():

            if (
                skill_event["old_level"]
                <
                obj.level_required
                <=
                skill_event["new_level"]
            ):

                unlocks.append(
                    {
                        "type": unlock_type,
                        "id": obj.id,
                        "name": obj.name
                    }
                )

        return unlocks