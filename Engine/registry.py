class Registry:
    """
    Stores game objects by ID.

    Example:

    items["oak_log"]
    trees["oak_tree"]
    monsters["cow"]
    """

    def __init__(self):
        self._objects = {}

    def register(self, obj):
        """
        Add an object to the registry.
        """

        self._objects[obj.id] = obj

    def get(self, object_id):
        """
        Retrieve an object by ID.
        """

        if object_id not in self._objects:
            raise KeyError(
                f"Unknown object ID: {object_id}"
            )

        return self._objects[object_id]

    def all(self):
        """
        Return all objects.
        """

        return self._objects.values()

    def values(self):
        return self._objects.values()


    def items(self):
        return self._objects.items()

    def __contains__(self, object_id):
        return object_id in self._objects

    def __len__(self):
        return len(self._objects)
    
    def __iter__(self):
        return iter(self._objects)