from Systems.action import Action


class WoodcuttingAction(Action):
    """
    Handles chopping trees.
    """


    def __init__(self, tree_id):

        self.tree_id = tree_id

        super().__init__(
            id=f"woodcutting_{tree_id}",
            name="Woodcutting",
            interval=3
        )


    def can_execute(self, player, game_data):

        tree = game_data.trees.get(
            self.tree_id
        )

        player_level = (
            player.skills["woodcutting"].level
        )

        return (
            player_level >= tree.level_required
        )


    def execute(self, player, game_data):

        tree = game_data.trees.get(
            self.tree_id
        )


        if not self.can_execute(
            player,
            game_data
        ):
            raise Exception(
                "Woodcutting level too low."
            )


        # Give XP

        player.skills[
            "woodcutting"
        ].add_xp(
            tree.xp
        )


        # Give logs

        player.inventory.add_item(
            tree.log_item_id,
            1
        )


        return {
            "xp": tree.xp,
            "item": tree.log_item_id,
            "amount": 1
        }