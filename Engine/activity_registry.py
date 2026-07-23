class ActivityRegistry:

    def __init__(self):

        self.activities = {}


    def register(
        self,
        skill_id,
        provider,
        icon,
        activity_type="direct"
    ):

        self.activities[skill_id] = {
            "provider": provider,
            "icon": icon,
            "type": activity_type
        }


    def get(self, skill_id):

        return self.activities.get(skill_id)