class UnlockManager:


    def check_unlocks(
        self,
        skill_event,
        game_data
    ):

        skill_id = skill_event["skill_id"]

        old_level = skill_event["old_level"]

        new_level = skill_event["new_level"]


        unlocks = []


        if skill_id == "fishing":

            for fish in game_data.fish.values():

                if (
                    old_level < fish.level_required
                    and
                    new_level >= fish.level_required
                ):

                    unlocks.append(
                        {
                            "type": "fish",
                            "id": fish.id,
                            "name": fish.name
                        }
                    )


        if skill_id == "woodcutting":

            for tree in game_data.trees.values():

                if (
                    old_level < tree.level_required
                    and
                    new_level >= tree.level_required
                ):

                    unlocks.append(
                        {
                            "type": "tree",
                            "id": tree.id,
                            "name": tree.name
                        }
                    )


        if skill_id == "cooking":

            for recipe in game_data.recipes.values():

                if (
                    old_level < recipe.level_required
                    and
                    new_level >= recipe.level_required
                ):

                    unlocks.append(
                        {
                            "type": "recipe",
                            "id": recipe.id,
                            "name": recipe.name
                        }
                    )


        return unlocks