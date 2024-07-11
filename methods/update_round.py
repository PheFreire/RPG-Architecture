def update_global_player_life(player_g_life: int) -> tuple[int, int]:
        '''
        returns:
            player_g_life: int
            player_life: int
        '''

        player_g_life += 5
        return (player_g_life, player_g_life)

def update_global_monster_life(monsters_killed: int) -> tuple[int, int]:
        '''
        returns:
            monsters_killed: int
            monsters_life: int
        '''

        monsters_killed += 1
        monsters_life = 20 + (10 * monsters_killed)
        return (monsters_killed, monsters_life)


def exit_game():
    exit()