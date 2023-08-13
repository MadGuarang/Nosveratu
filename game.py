import random
from character import Character
from capital import Capital
from ui import UI
from save_load_system import SaveLoadSystem

class Game:
    def __init__(self):
        self.player = None
        self.capital = None
        self.ui = UI()
        self.save_load_system = SaveLoadSystem()

    # ... rest of the code ...
