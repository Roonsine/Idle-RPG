from config import MAX_LEVEL


class XPSystem:
    """
    Handles all experience calculations.

    Uses a precomputed XP table.
    """

    def __init__(self):

        self.table = self._generate_table()

    def _generate_table(self):

        table = [0]

        points = 0

        for level in range(1, MAX_LEVEL + 1):

            points += int(level + 300 * (2 ** (level / 7)))

            table.append(points // 4)

        return table
    
    def xp_for_level(self, level: int) -> int:
        return self.table[level - 1]

    def level_for_xp(self, xp: int) -> int:
        level = 1

        for i, required in enumerate(self.table):

            if xp >= required:

                level = i + 1

        return min(level, MAX_LEVEL)