from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Toggle


class starting_pairs(Range):
    """number of pairs you start unlocked"""
    display_name = "Pairs Unlocked"
    range_start = 1
    range_end = 24
    default = 1


class starting_girls(Range):
    """number of girls you start unlocked Note will prioritise fulfilling the amount of starting pairs so may be higher then set"""
    display_name = "Girls Unlocked"
    range_start = 2
    range_end = 12
    default = 3


class starting_seed_blue(Range):
    """number of blue note seeds given at start"""
    display_name = "Number of blue note seeds given at start"
    range_start = 0
    range_end = 999
    default = 25


class starting_seed_green(Range):
    """number of green star seeds given at start"""
    display_name = "Number of green star seeds given at start"
    range_start = 0
    range_end = 999
    default = 25


class starting_seed_orange(Range):
    """number of orange moon seeds given at start"""
    display_name = "Number of orange moon seeds given at start"
    range_start = 0
    range_end = 999
    default = 25


class starting_seed_red(Range):
    """number of red flame seeds given at start"""
    display_name = "Number of red flame seeds given at start"
    range_start = 0
    range_end = 999
    default = 25

class shop_items(Range):
    """number of archipelago items in the shop Note if there is not enough locations for items it will add shop locations to satisfy the locations needed, MAX is 494 so total locations isn't over 1000"""
    display_name = "shop items"
    range_start = 0
    range_end = 494
    default = 20

class enable_question_locations(Toggle):
    """enable having items locked behind asking girls their favourite stuff Note if there is not enough locations for items it will add shop locations to satisfy the locations needed"""
    display_name = "enable having items locked behind asking girls their favourite stuff Note if there is not enough locations for items it will add shop locations to satisfy the locations needed"
    default = True

class disable_baggage(Toggle):
    """disable baggage completely"""
    display_name = "disable baggage completely"
    default = False


@dataclass
class HP2Options(PerGameCommonOptions):
    number_of_staring_girls: starting_girls
    number_of_staring_pairs: starting_pairs
    number_blue_seed: starting_seed_blue
    number_green_seed: starting_seed_green
    number_orange_seed: starting_seed_orange
    number_red_seed: starting_seed_red
    number_shop_items: shop_items
    enable_questions: enable_question_locations
    disable_baggage: disable_baggage
