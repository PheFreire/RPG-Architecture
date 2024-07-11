from random import randint


def get_character_entrypoint() -> str:
    return input("Mago (1) ou guerreiro (2) -> ")

def auth_character_entrypoint(character: str) -> bool:
    return False if character != "1" and character != "2" else True

def is_wizard(choice: str) -> bool:
    return True if choice == "1" else False

def power_bar_gen(is_wizard: bool) -> int:
    return randint(7, 15) if is_wizard else randint(5, 10)
