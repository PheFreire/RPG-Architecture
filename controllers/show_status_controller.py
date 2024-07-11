from methods.show_data import get_monster_killed, get_monster_status, get_player_status


def show_status(
    player_life: int,
    monster_life: int,
    monsters_killed: int,
    power_bar: int,
):
    get_player_status(player_life, power_bar)
    get_monster_status(monster_life)
    get_monster_killed(monsters_killed)
    



