import sys

from PySide6.QtWidgets import QApplication

from Engine.game import Game
from UI.main_window import MainWindow

from pathlib import Path



def main():

    app = QApplication(sys.argv)

    game = Game(
        Path("Data")
    )

    game.load()

    game.start()


    window = MainWindow(
        game
    )

    window.show()


    sys.exit(
        app.exec()
    )



if __name__ == "__main__":
    main()