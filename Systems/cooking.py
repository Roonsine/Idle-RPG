from Systems.action import Action


class CookingAction(Action):

    def __init__(self, recipe):

        self.recipe = recipe

        super().__init__(
            id=recipe.id,
            name=recipe.name,
            category="cooking",
            interval=recipe.interval
        )


    def can_execute(
        self,
        player,
        game_data
    ):

        cooking = player.skills["cooking"]

        if cooking.level < self.recipe.level_required:
            return False


        for item, amount in self.recipe.inputs.items():

            if not player.inventory.has_item(
                item,
                amount
            ):
                return False


        if not player.inventory.has_category(
            "log",
            1,
            game_data
        ):
            return False


        return True

    def execute(
        self,
        player,
        game_data
    ):

        if not self.can_execute(
            player,
            game_data
        ):
            return {
                "success": False,
                "message": "Missing materials."
            }


        # Remove ingredients

        for item_id, amount in self.recipe.inputs.items():

            player.inventory.remove_item(
                item_id,
                amount
            )


        # Remove fuel

        for category, amount in self.recipe.tools.items():

            player.inventory.remove_category(
                category,
                amount,
                game_data
            )


        # Add outputs

        for item_id, amount in self.recipe.outputs.items():

            player.inventory.add_item(
                item_id,
                amount
            )


        # Give XP

        player.skills["cooking"].add_xp(
            self.recipe.xp
        )


        item_id, amount = next(
            iter(self.recipe.outputs.items())
        )


        return {
            "xp": self.recipe.xp,
            "item": item_id,
            "amount": amount
        }

    def get_reward(self):

        item_id, amount = next(
            iter(self.recipe.outputs.items())
        )

        return {
            "item": item_id,
            "amount": amount,
            "xp": self.recipe.xp
        }