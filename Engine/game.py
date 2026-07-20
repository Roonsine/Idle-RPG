"""
The main Game object.

This owns every major game system.
"""

from config import DATA_DIR

from Engine.resource_loader import ResourceLoader
from Engine.xp import XPSystem


class Game:

    def __init__(self):

        self.loader = ResourceLoader(DATA_DIR)

        self.xp = XPSystem()

        self.player = None

        self.items = {}

        self.trees = {}

        self.monsters = {}

        self.skills = {}

    def load_data(self):
        """Load all JSON resources."""

        self.items = self.loader.items()

        self.trees = self.loader.trees()

        self.monsters = self.loader.monsters()

        self.skills = self.loader.skills()

    def start(self):

        self.load_data()

        print("Game started.")