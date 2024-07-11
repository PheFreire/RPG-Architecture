import os

def get_player_status(player_life: int, power_bar: int):
    print("-"*30)
    print(f"Player Life: " + "❤ " * player_life)
    print("-"*30)
    print(f"Power Bar: " + "🟦" * power_bar)


def get_monster_status(monster_life: int):
    print("-"*30)
    print(f"Monster Life: " + " ☠️ " * monster_life)

def get_monster_killed(monsters_killed: int):
    print("-"*30)
    print(f"Monsters Killed: " + "❌" * monsters_killed)
    input()
    os.system("clear")
