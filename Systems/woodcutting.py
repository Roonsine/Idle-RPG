from Systems.action import Action


class WoodcuttingAction(Action):
    """
    Represents chopping a specific tree.
    """


    def __init__(self, tree):

        self.tree = tree


        super().__init__(
            id=f"woodcutting_{tree.id}",
            name=f"Chopping {tree.name}",
            category="woodcutting",
            interval=tree.interval
        )


    def can_execute(self, player, game_data):

        woodcutting = (
            player.skills["woodcutting"]
        )


        return (
            woodcutting.level
            >=
            self.tree.level_required
        )


    def execute(self, player, game_data):

        player.skills["woodcutting"].add_xp(
            self.tree.xp
        )

        player.inventory.add_item(
            self.tree.log_item_id,
            1
        )

        return {
            "item": self.tree.log_item_id,
            "amount": 1,
            "xp": self.tree.xp
        }