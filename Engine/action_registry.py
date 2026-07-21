class ActionRegistry:


    def __init__(self):

        self.actions = {}



    def register(
        self,
        action_type,
        factory
    ):

        self.actions[action_type] = factory



    def create(
        self,
        action_type,
        target_id,
        game_data
    ):

        factory = self.actions[action_type]

        return factory(
            target_id,
            game_data
        )