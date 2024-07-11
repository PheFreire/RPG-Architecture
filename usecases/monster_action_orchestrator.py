from methods.turn_monster_actions import *


def monster_action_orchestrator(player_life: int, monsters_killed: int):
    if monster_choice():
        return (monster_atack(player_life, monsters_killed), False)

    return (player_life, monster_defending())
                                                                                                