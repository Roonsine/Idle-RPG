from pathlib import Path

from Engine.game import Game


game = Game(
    Path("Data")
)

game.start()


print("Starting action...")

game.start_action(
    "woodcutting",
    "normal_tree"
)


print(game.action_state)


print("\nSaving...")

game.save()


print("\nSaved action:")
print(game.action_state)