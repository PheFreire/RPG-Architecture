from methods.turn_player_actions import *

def player_action_orchestrator(
    player_g_life: int,
    player_life: int,
    is_wizard: bool,
    monsters_killed: int,
    power_bar: int,
    g_power_bar: int,
    monster_life: int,
):
    is_defending = False

    while True:
        action = get_player_action()
        if auth_player_action(action):
            break
        
    if action == "1":
        if auth_power_bar(power_bar, 2):
            power_bar = reduce_power_bar(power_bar, 2)
            monster_life -= atack(is_wizard, monsters_killed)
    
    elif action == "2":
        is_defending = defense()
    
    elif action == "3":
        player_life = fix_life_bar(get_heal(player_life, is_wizard), player_g_life)
    
    elif action == "4":
        power_bar = fix_power_bar(get_rest(power_bar), g_power_bar)

    elif action == "5":
        exit_game()
        
    return player_life, power_bar, is_defending, monster_life
