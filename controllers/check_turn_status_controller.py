from usecases.get_new_round_values import get_new_round_values
from usecases.close_game import close_game
from usecases.final_turn_orchestrator import final_turn_orchestrator


# Receber 
def check_turn_status(
    player_g_life: int,
    player_life: int,
    monsters_killed: int,
    monster_life: int,
    player_is_alive: bool,
    monster_is_alive: bool,
) -> tuple[int, int, int, int]:
    should_open_new_turn = final_turn_orchestrator(player_is_alive, monster_is_alive)
    
    if not should_open_new_turn:
        close_game()

    return get_new_round_values(
        player_g_life,
        player_life,
        monster_life,
        monsters_killed,
        player_is_alive,
        monster_is_alive,
    )
