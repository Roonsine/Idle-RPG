class ActionRegistry:
    """
    Registers all available action creators.
    """

    def __init__(self):
        self._creators = {}

    def register(self, action_type: str, creator):
        if action_type in self._creators:
            raise ValueError(
                f"Action '{action_type}' is already registered."
            )

        self._creators[action_type] = creator

    def create(self, action_type: str, *args, **kwargs):
        if action_type not in self._creators:
            raise KeyError(
                f"No creator registered for '{action_type}'."
            )

        return self._creators[action_type](
            *args,
            **kwargs
        )

    def registered_actions(self):
        return tuple(self._creators.keys())