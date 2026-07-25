import math
import config

MAX_LEVEL = config.MAX_LEVEL


def xp_for_level(level: int) -> int:

    if level <= 1:
        return 0

    total = 0

    for i in range(1, level):

        total += math.floor(
            i + 300 * (2 ** (i / 7))
        )

    return math.floor(
        total / 4
    )


def level_from_xp(xp: float) -> int:

    level = 1

    for i in range(1, MAX_LEVEL + 1):

        if xp >= xp_for_level(i):

            level = i

        else:

            break

    return level