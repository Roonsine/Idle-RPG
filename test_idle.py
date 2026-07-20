import time

from config import DATA_DIR

from Engine.game import Game

from Systems import WoodcuttingAction



game = Game(DATA_DIR)

game.start()


action = WoodcuttingAction(
    "normal_tree"
)


game.action_manager.start(
    action
)


for i in range(15):

    result = game.update()


    if result:

        print(
            "Completed chop:",
            result
        )

        print(
            "Inventory:",
            game.player.inventory
        )

        print(
            "XP:",
            game.player.skills["woodcutting"].xp
        )


    time.sleep(0.5)