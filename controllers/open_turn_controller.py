from usecases.get_turn_results import get_turn_results
from usecases.monster_action_orchestrator import monster_action_orchestrator
from usecases.player_actions_orchestrator import player_action_orchestrator


def open_turn(
    player_g_life: int,
    player_life: int,
    is_wizard: bool,
    monsters_killed: int,
    power_bar: int,
    g_power_bar: int,
    monster_life: int,
) -> tuple[int, int, bool, int, int, int, int, bool, bool]:
    (
        turn_player_life, 
        power_bar, 
        is_defending,
        turn_monster_life
    ) = player_action_orchestrator(
        player_g_life,
        player_life,
        is_wizard,
        monsters_killed,
        power_bar,
        g_power_bar,
        monster_life,
    )
    
    (
        turn_player_life, 
        monster_is_defending
    ) = monster_action_orchestrator(turn_player_life, monsters_killed)

    (
        player_life, 
        monster_life,
        player_is_alive,
        monster_is_alive,
    ) = get_turn_results(
        player_life,
        turn_player_life,
        is_defending,
        monster_life,
        turn_monster_life,
        monster_is_defending,
    )
    
    return (
        player_g_life,
        player_life,
        is_wizard,
        monsters_killed,
        power_bar,
        g_power_bar,
        monster_life,
        player_is_alive,
        monster_is_alive,
    )
