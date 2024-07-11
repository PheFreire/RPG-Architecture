def is_alive(life: int) -> bool:
    return life > 0

def get_player_continue_choice(objeto: str) -> str:
    return input(f"O {objeto} morreu :(\nContinuar (1) | Sair (2)\n-> ")

