from controllers.check_turn_status_controller import check_turn_status
from controllers.open_turn_controller import open_turn
from controllers.show_status_controller import show_status
from controllers.start_game_controller import start_game

(
    is_wizard, 
    player_g_life, 
    player_life, 
    monster_life, 
    monsters_killed, 
    g_power_bar,
    power_bar,
) = start_game()


while True:
    show_status(
        player_life,
        monster_life,
        monsters_killed,
        power_bar
    )
    
    (
        player_g_life, player_life, is_wizard,
        monsters_killed, power_bar, g_power_bar,
        monster_life, player_is_alive, monster_is_alive,
    ) = open_turn(
        player_g_life,
        player_life,
        is_wizard,
        monsters_killed,
        power_bar,
        g_power_bar,
        monster_life,
    )

    (
        player_g_life, player_life,
        monsters_killed, monsters_life
    ) = check_turn_status(
        player_g_life,
        player_life,
        monsters_killed,
        monster_life,
        player_is_alive,
        monster_is_alive,
    )

    
# Consertar curar