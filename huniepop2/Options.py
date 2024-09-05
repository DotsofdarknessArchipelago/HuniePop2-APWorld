from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Toggle


class starting_pairs(Range):
    """number of pairs you start unlocked"""
    display_name = "Pairs Unlocked At Start"
    range_start = 1
    range_end = 24
    default = 1


class starting_girls(Range):
    """number of girls you start unlocked Note will prioritise fulfilling the amount of starting pairs so may be higher then set"""
    display_name = "Girls Unlocked At Start Note will prioritise fulfilling the amount of starting pairs so may be higher then set"
    range_start = 2
    range_end = 12
    default = 3


class starting_fruit_blue(Range):
    """number of blue note fruits given at start"""
    display_name = "Number of blue note fruits given at start"
    range_start = 0
    range_end = 999
    default = 25


class starting_fruit_green(Range):
    """number of green star fruits given at start"""
    display_name = "Number of green star fruits given at start"
    range_start = 0
    range_end = 999
    default = 25


class starting_fruit_orange(Range):
    """number of orange moon fruits given at start"""
    display_name = "Number of orange moon fruits given at start"
    range_start = 0
    range_end = 999
    default = 25


class starting_fruit_red(Range):
    """number of red flame fruits given at start"""
    display_name = "Number of red flame fruits given at start"
    range_start = 0
    range_end = 999
    default = 25

class shop_items(Range):
    """number of archipelago items in the shop Note if there is not enough locations for items it will add shop locations to satisfy the locations needed"""
    display_name = "number of archipelago items in the shop Note if there is not enough locations for items it will add shop locations to satisfy the locations needed"
    range_start = 0
    range_end = 999
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
    number_blue_fruit: starting_fruit_blue
    number_green_fruit: starting_fruit_green
    number_orange_fruit: starting_fruit_orange
    number_red_fruit: starting_fruit_red
    number_shop_items: shop_items
    enable_questions: enable_question_locations
    disable_baggage: disable_baggage
