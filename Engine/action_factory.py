from Systems.woodcutting import WoodcuttingAction
from Systems.mining import MiningAction


class ActionFactory:


    def create_tree_action(
        self,
        target_id,
        game_data
    ):

        tree = game_data.trees.get(
            target_id
        )

        return WoodcuttingAction(
            tree
        )


    def create_rock_action(
        self,
        target_id,
        game_data
    ):

        rock = game_data.rocks.get(
            target_id
        )

        return MiningAction(
            rock
        )