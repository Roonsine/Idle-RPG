class ActivityRegistry:

    def __init__(self):

        self.activities = {}


    def register(
        self,
        skill_id,
        provider
    ):

        self.activities[skill_id] = provider


    def get(self, skill_id):

        return self.activities.get(skill_id)