from methods.pre_turn import *

def get_initial_values() -> tuple[bool, int, int, int, int]:
    while True:
        character_entrypoint = get_character_entrypoint()
        if auth_character_entrypoint(character_entrypoint):
            return is_wizard(character_entrypoint), 20, 20, 20, 0

