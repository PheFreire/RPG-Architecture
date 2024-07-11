from methods.turn_conditions import is_alive

def get_turn_results(
    player_life: int,
    turn_player_life: int,
    is_defending: bool,
    monster_life: int,
    turn_monster_life: int,
    monster_is_defending: bool,
) -> tuple[int, int, bool, bool]:
    if not is_defending:
        player_life = turn_player_life
        print(f"You didn't defend!")
    else:
        print(f"You defend!")

    print("-="*30)

    if not monster_is_defending:
        monster_life = turn_monster_life
        print(f"Monster didn't defend!")
    else:
        print(f"Monster defended!")

    print("-="*30)
    
    print(f"Your life {player_life}!")
    print(f"Monster life {monster_life}!")
    print("-="*30)
    
    return (
        player_life, monster_life,
        is_alive(player_life), is_alive(monster_life)
    )


