import pickle

class SaveLoadSystem:
    def save_game(self, player):
        with open("savegame.pickle", "wb") as file:
            pickle.dump(player, file)

    def load_game(self):
        try:
            with open("savegame.pickle", "rb") as file:
                player = pickle.load(file)
                return player
        except FileNotFoundError:
            return None
