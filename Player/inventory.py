from collections import defaultdict


class Inventory:
    """
    Stores items owned by the player.

    Uses item IDs rather than Item objects.

    Example:

    {
        "oak_log": 50,
        "bird_nest": 2
    }
    """

    def __init__(self):

        self.items = defaultdict(int)


    def add_item(self, item_id: str, amount: int = 1):
        """
        Add items to inventory.
        """

        self.items[item_id] += amount


    def remove_item(self, item_id: str, amount: int = 1):
        """
        Remove items if available.
        """

        if not self.has_item(item_id, amount):
            return False

        self.items[item_id] -= amount

        if self.items[item_id] <= 0:
            del self.items[item_id]

        return True


    def has_item(self, item_id: str, amount: int = 1):
        """
        Check if inventory contains enough.
        """

        return self.items[item_id] >= amount


    def get_amount(self, item_id: str):
        """
        Return quantity of an item.
        """

        return self.items[item_id]


    def all_items(self):
        """
        Return all stored items.
        """

        return dict(self.items)


    def __str__(self):

        if not self.items:
            return "Inventory is empty."

        return str(dict(self.items))