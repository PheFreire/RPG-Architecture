from methods.update_round import update_global_monster_life, update_global_player_life


def get_new_round_values(
        player_g_life: int,
        player_life: int,
        monsters_life: int,
        monsters_killed: int,
        player_is_alive: bool,
        monster_is_alive: bool,
    ) -> tuple[int, int, int, int]:
    '''
    returns
        - player_g_life: int\n
        - player_life: int\n
        - monsters_killed: int\n
        - monsters_life: int\n
    '''

    if player_is_alive and not monster_is_alive:
        player_g_life, player_life = update_global_player_life()
        monsters_killed, monsters_life = update_global_monster_life()
    
    return (
        player_g_life,
        player_life,
        monsters_killed,
        monsters_life,
    )

