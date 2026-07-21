from pathlib import Path

from PySide6.QtWidgets import QApplication

from Engine.game import Game
from UI.main_window import MainWindow



def main():

    app = QApplication([])


    game = Game(
        Path("Data")
    )


    game.start()


    window = MainWindow(
        game
    )


    window.show()


    app.exec()



if __name__ == "__main__":
    main()