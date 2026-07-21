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