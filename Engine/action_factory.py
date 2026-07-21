from Systems import WoodcuttingAction
from Systems import MiningAction

class ActionFactory:

    def __init__(self):
        pass

    def create_tree_action(
        self,
        tree_id,
        game_data
    ):
        tree = game_data.trees.get(tree_id)

        return WoodcuttingAction(tree) 
    
    def create_rock_action(
        self,
        rock_id,
        game_data
    ):
        rock = game_data.rocks.get(rock_id)

        return MiningAction(rock)