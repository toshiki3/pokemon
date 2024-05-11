import random

class Player:
    def __init__(self, name):
        self.name = name
        self.active_pokemon = None

    def choose_move(self):
        # プレイヤーが技をランダムに選択する場合
        if self.active_pokemon:
            return random.choice(self.active_pokemon.moves)
        else:
            return None