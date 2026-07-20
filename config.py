"""
Global Game Configuration

This file should only contain constants.
No gameplay logic belongs here.

"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------------

ROOT_DIR = Path(__file__).parent

DATA_DIR = ROOT_DIR / "data"
SAVE_DIR = ROOT_DIR / "saves"
ASSEST_DIR = ROOT_DIR  / "assets"

ICON_DIR = ASSEST_DIR / "icons"
SPRITE_DIR = ASSEST_DIR / "sprites"
FONT_DIR = ASSEST_DIR / "fonts"
AUDIO_DIR = ASSEST_DIR / "audio"

# ------------------------------------------------------------------
# Window
# ------------------------------------------------------------------

WINDOW_TITLE = "Idle RPG"

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

FPS = 60
VERSION = "0.0.1"

# ------------------------------------------------------------------
# Saving
# ------------------------------------------------------------------

SAVE_FILE = SAVE_DIR / "save.json"

AUTOSAVE_SECONDS = 60

# ------------------------------------------------------------------
# Player
# ------------------------------------------------------------------

STARTING_GOLD = 0
STARTING_BANK_SLOTS = 20
STARTING_INVENTORY_SLOTS = 28
MAX_LEVEL = 99

# ------------------------------------------------------------------
# Game Timing
# ------------------------------------------------------------------

GAME_TICK = 0.10
OFFLINE_PROGRESS_LIMIT = 24 * 60 * 60

# ------------------------------------------------------------------
# Experience
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# Debug
# ------------------------------------------------------------------

DEBUG = True