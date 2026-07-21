import sys

from pathlib import Path

from PySide6.QtWidgets import QApplication

from Engine.game import Game
from UI.main_window import MainWindow



app = QApplication(sys.argv)


game = Game(
    Path("Data")
)


game.start()


window = MainWindow(
    game
)


window.show()


sys.exit(
    app.exec()
)