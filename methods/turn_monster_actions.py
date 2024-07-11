from random import randint


def monster_atack(player_life: int, monsters_killed: int) -> int:
    return player_life - (5 + (5*monsters_killed))

def monster_defending() -> bool:
    return True

def monster_choice() -> bool:
    return randint(0, 1)   
