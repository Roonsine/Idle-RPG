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


    def add_item(self, item_id, amount):

        if item_id not in self.items:
            self.items[item_id] = 0

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

        return self.items.get(item_id, 0) >= amount


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

    def has_category(
        self,
        category,
        amount,
        game_data
    ):

        total = 0

        for item_id, quantity in self.items.items():

            item = game_data.items.get(
                item_id
            )

            if item.category == category:

                total += quantity


        return total >= amount

    def remove_category(
    self,
    category,
    amount,
    game_data
    ):

        remaining = amount


        for item_id, quantity in list(self.items.items()):

            item = game_data.items.get(
                item_id
            )


            if item.category != category:
                continue


            remove = min(
                quantity,
                remaining
            )


            self.remove_item(
                item_id,
                remove
            )


            remaining -= remove


            if remaining <= 0:
                break

    def __str__(self):

        if not self.items:
            return "Inventory is empty."

        return str(dict(self.items))