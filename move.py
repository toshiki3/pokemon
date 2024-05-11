class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

    def calculate_damage(attacker, defender, move):
        # ダメージ計算ロジックをここに追加（例: 単純な式での計算）
        damage = (2 * attacker.level / 5 + 2) * move.power * (attacker.attack / defender.defense) / 50 + 2
        return damage