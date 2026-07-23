from Systems.woodcutting import WoodcuttingAction
from Systems.mining import MiningAction
from Systems.fishing import FishingAction



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

    def create_fishing_action(
        self,
        target_id,
        game_data
    ):

        zone_id, fish_id = target_id.split(":")


        spot = game_data.fishing_spots.get(
            zone_id
        )


        return FishingAction(
            spot,
            fish_id,
            game_data.fish,
            game_data.fish.get(fish_id).name
        )