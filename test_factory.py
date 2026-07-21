import time

from config import DATA_DIR

from Engine.game import Game

game = Game(DATA_DIR)

game.start()

game.start_action("normal_tree")

game.save()