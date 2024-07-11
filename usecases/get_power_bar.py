from methods.pre_turn import power_bar_gen


def get_power_bar(is_wizard: bool) -> tuple[int, int]:
    pb = power_bar_gen(is_wizard)
    return pb, pb
