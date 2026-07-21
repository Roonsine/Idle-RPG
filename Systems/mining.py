from Systems.action import Action


class MiningAction(Action):

    def __init__(self, rock):

        self.rock = rock

        super().__init__(
            id=f"mining_{rock.id}",
            name=f"Mining {rock.name}",
            category="mining",
            interval=rock.interval
        )

    def execute(self, player, game_data):
        """
        Executes one mining cycle.
        """

        player.inventory.add_item(
            self.rock.ore_item_id,
            self.rock.amount
        )

        player.skills["mining"].add_xp(
            self.rock.xp
        )

        return {
            "xp": self.rock.xp,
            "item": self.rock.ore_item_id,
            "amount": self.rock.amount
        }