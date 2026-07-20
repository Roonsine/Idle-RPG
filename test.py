from config import DATA_DIR

from Engine.game import Game


game = Game(
    DATA_DIR
)


game.start()


print(game.data)

print()

print(game.player)

print()

print(game.player.skills)