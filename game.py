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

    def start_game(self):
        self.ui.display_start_screen()
        self.create_character()
        self.select_capital()
        self.main_menu()

    def create_character(self):
        self.ui.display_character_creation_screen()
        name = self.ui.get_character_name()
        attributes = self.randomize_attributes()
        self.player = Character(name, *attributes)
        self.save_load_system.save_game(self.player)

    def select_capital(self):
        self.capital = self.ui.get_capital_choice()
        self.capital.difficulty_factor = self.capital.get_difficulty_factor()

    def main_menu(self):
        while True:
            self.ui.display_stats(self.player)
            self.ui.display_thirst_level(self.player)
            choice = self.ui.get_main_menu_choice()
            if choice == "HUNT":
                self.hunt()
            elif choice == "RECON":
                self.recon()
            elif choice == "PRAY":
                self.pray()
            elif choice == "MOVE":
                self.move_capital()
            elif choice == "STATS":
                self.ui.display_stats(self.player)
            elif choice == "END":
                self.end_turn()

    def hunt(self):
        self.ui.display_hunting_screen()
        result = random.choice(["SUCCESS", "FAILURE"])
        if result == "SUCCESS":
            self.player.hunger -= 10
            self.player.thirst += 5
            self.ui.display_message("You successfully hunted for food.")
        else:
            self.player.hunger += 5
            self.player.thirst += 5
            self.ui.display_message("You failed to hunt for food.")

    def recon(self):
        self.ui.display_recon_screen()
        result = random.choice(["SUCCESS", "FAILURE"])
        if result == "SUCCESS":
            self.player.thirst += 5
            self.ui.display_message("You successfully scouted the area.")
        else:
            self.player.thirst += 10
            self.ui.display_message("You failed to scout the area.")

    def pray(self):
        self.ui.display_pray_screen()
        result = random.choice(["SUCCESS", "FAILURE"])
        if result == "SUCCESS":
            self.player.thirst += 5
            self.ui.display_message("Your prayer has been answered.")
        else:
            self.player.thirst += 10
            self.ui.display_message("Your prayer went unanswered.")

    def move_capital(self):
        self.capital = self.ui.get_capital_choice()
        self.capital.difficulty_factor = self.capital.get_difficulty_factor()

    def end_turn(self):
        self.player.thirst += 10
        self.player.hunger += 10
        self.ui.display_message("You ended your turn.")

    def randomize_attributes(self):
        attributes = []
        for _ in range(3):
            attributes.append(random.randint(1, 10))
        return attributes

game = Game()
game.start_game()
