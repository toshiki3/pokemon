import player as pl
import pokemon as poke
import move as mo
import random

def main():
    # プレイヤーと敵のポケモンを作成
    player = pl.Player("Player")
    enemy = poke.Pokemon("カメックス", 50, "みず", 186, 79, 121, 105, 172, 98, [])

    # プレイヤーのメガニウムを設定
    meganium_moves = [mo.Move("のしかかり", "ノーマル", 80), mo.Move("リーフストーム", "くさ", 130), mo.Move("アイアンテール", "はがね", 100),mo.Move("リフレクター","エスパー",-2)]
    meganium = poke.Pokemon("メガニウム", 50, "くさ", 187, 78, 167, 103, 121, 100, meganium_moves)
    player.active_pokemon = meganium

    # プレイヤーの技を選択
    selected_move = player.choose_move()

    # ダメージ計算
    if selected_move:
        damage = calculate_damage(player.active_pokemon, enemy, selected_move)
        print(f"{player.active_pokemon.name} の {selected_move.name}！")
        print(f"{enemy.name} に {damage} のダメージ！")
    else:
        print("技が選択されていません。")

def calculate_damage(attacker, defender, move):
    # ダメージ計算ロジックをここに追加（例: 単純な式での計算）
    damage = int(int(int(int(2 * attacker.level / 5 + 2) * move.power * (attacker.attack / defender.defense)) / 50 + 2) * random.uniform(0.85,1.00))
    return damage

if __name__ == "__main__":
    main()