from methods.turn_conditions import get_player_continue_choice


def final_turn_orchestrator(player_is_alive: bool, monster_is_alive: bool):
    '''
        -> tuple[bool, bool]
        first boolean -> start_next_turn
        seccond boolean -> player_is_alive
        third boolean -> monster_is_alive
    '''
    if not player_is_alive or not monster_is_alive:
        objeto = "Jogador" if not player_is_alive else "Monstro"
        action = get_player_continue_choice(objeto)
        return True if action == "1" else False

    return True
