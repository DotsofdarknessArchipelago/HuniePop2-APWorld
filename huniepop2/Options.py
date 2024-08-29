from Options import PerGameCommonOptions, Range


class starting_girls(Range):
    """number of girls you start unlocked"""
    display_name = "Girls Unlocked At Start"
    range_start = 2
    range_end = 12
    default = 3

class starting_pairs(Range):
    """number of pairs you start unlocked"""
    display_name = "Pairs Unlocked At Start"
    range_start = 1
    range_end = 24
    default = 1

class HP2Options(PerGameCommonOptions):

    number_of_staring_girls: starting_girls
    number_of_staring_pairs: starting_pairs