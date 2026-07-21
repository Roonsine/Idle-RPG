from pathlib import Path
import time

from Engine.game import Game


game = Game(
    Path("Data")
)

game.start()


game.start_action(
    "woodcutting",
    "normal_tree"
)


print(
    "Before save:",
    game.player.inventory.items
)


game.save()


print(
    "Saved. Waiting..."
)


time.sleep(10)


game2 = Game(
    Path("Data")
)


game2.start()


print(
    "After offline:",
    game2.player.inventory.items
)


print(
    game2.player.skills["woodcutting"]
)