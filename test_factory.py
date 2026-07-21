import time

from config import DATA_DIR

from Engine.game import Game


game = Game(DATA_DIR)

game.start()


action = game.start_action(
    "normal_tree"
)


print(
    "Started:",
    action.name
)


while True:

    result = game.update()


    if result:

        print(result)

        print(
            game.player.inventory
        )

        print(
            game.player.skills[
                "woodcutting"
            ]
        )


    time.sleep(0.5)