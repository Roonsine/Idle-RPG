from Systems.action import Action


class FishingAction(Action):

    def __init__(
        self,
        spot,
        fish_id,
        fish_registry,
        name
    ):

        self.spot = spot
        self.fish_id = fish_id
        self.fish_registry = fish_registry
        self.fish_name = name


        super().__init__(
            id=f"fishing_{spot.id}_{fish_id}",
            name=f"Fishing {name}",
            category="fishing",
            interval=spot.interval
        )


    def can_execute(
        self,
        player,
        game_data
    ):

        fishing = player.skills["fishing"]

        return (
            fishing.level >= self.spot.level_required
        )


    def execute(
        self,
        player,
        game_data
    ):

        if not self.can_execute(
            player,
            game_data
        ):

            raise Exception(
                "Fishing level too low."
            )


        fish = self.fish_registry.get(
            self.fish_id
        )


        player.inventory.add_item(
            fish.item_id,
            1
        )


        player.skills["fishing"].add_xp(
            fish.xp
        )


        return {

            "item": fish.item_id,

            "amount": 1,

            "xp": fish.xp

        }