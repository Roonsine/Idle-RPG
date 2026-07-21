from Systems.woodcutting import WoodcuttingAction


class ActionFactory:
    """
    Creates actions from game data.
    """


    def create_tree_action(
        self,
        tree_id,
        game_data
    ):

        tree = game_data.trees.get(
            tree_id
        )


        return WoodcuttingAction(
            tree
        )