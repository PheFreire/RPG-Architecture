from usecases.get_power_bar import get_power_bar
from usecases.get_inital_values import get_initial_values


def start_game() -> tuple[bool, int, int, int, int, int, int]:
    (
        is_wizard,
        player_g_life,
        player_life,
        monster_life,
        monsters_killed
    ) =  get_initial_values()

    g_power_bar, power_bar = get_power_bar(is_wizard)

    return (
        is_wizard, player_g_life, 
        player_life, monster_life, 
        monsters_killed, g_power_bar, power_bar,
    ) 
    
