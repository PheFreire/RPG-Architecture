from random import randint

def get_player_action() -> str:
    return input("atack(1) defense(2) heal(3) rest(4) exit(5) -> ")
    
def auth_player_action(action: str) -> bool:
    return False if action != "1" and action != "2" and action != "3" and action != "4" and action != "5" else True

def auth_power_bar(pb: int, reduce: int) -> bool:
    return pb - reduce >= 0

def reduce_power_bar(pb: int, reduce: int) -> int:
    return pb - reduce

def atack(is_wizard: bool, monsters_killed: int) -> int:
    aditional = 3 * monsters_killed
    return randint(1, 8+aditional) if is_wizard else randint(3, 10+aditional)

def defense():
    return True

def get_heal(player_life: int, is_wizard: bool) -> int:
    return player_life + (4 if is_wizard else 2)

def fix_life_bar(player_life: int, total_life: int) -> int:
    return total_life if player_life > total_life else player_life

def get_rest(player_power_bar: int) -> int:
    return player_power_bar + randint(1,5)

def fix_power_bar(player_power_bar: int, total_power_bar: int):
    return total_power_bar if player_power_bar > total_power_bar else player_power_bar

def exit_game():
    exit()










