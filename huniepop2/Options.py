from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Toggle, OptionSet, Visibility


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
    display_name = "starting blue note seeds"
    range_start = 0
    range_end = 999
    default = 25


class starting_seed_green(Range):
    """number of green star seeds given at start"""
    display_name = "starting green star seeds"
    range_start = 0
    range_end = 999
    default = 25


class starting_seed_orange(Range):
    """number of orange moon seeds given at start"""
    display_name = "starting orange moon seeds"
    range_start = 0
    range_end = 999
    default = 25


class starting_seed_red(Range):
    """number of red flame seeds given at start"""
    display_name = "starting red flame seeds"
    range_start = 0
    range_end = 999
    default = 25

class shop_items(Range):
    """number of archipelago items in the shop Note if there is not enough locations for items it will add shop locations to satisfy the locations needed, MAX is 494 so total locations isn't over 1000"""
    display_name = "shop items"
    range_start = 0
    range_end = 494
    default = 0

class enable_question_locations(Toggle):
    """enable having items locked behind asking girls their favourite stuff Note if there is not enough locations for items it will add shop locations to satisfy the locations needed"""
    display_name = "fav questions have items"
    default = True

class disable_outfits(Toggle):
    """disable having outfits as locations/items"""
    display_name = "outfits disabled"
    default = False

class disable_baggage(Toggle):
    """disable baggage completely"""
    display_name = "disable baggage"
    default = False

class lovers_instead_wings(Toggle):
    """require player to get all available pairs to lovers instead of collecting wings"""
    display_name = "lovers instead of wings"
    default = False

class enabled_girls(OptionSet):
    """girls enabled to be accessed"""
    display_name = "enabled girls"
    valid_keys = [
        "lola",
        "jessie",
        "lillian",
        "zoey",
        "sarah",
        "lailani",
        "candace",
        "nora",
        "brooke",
        "ashley",
        "abia",
        "polly"
    ]
    default = valid_keys.copy()

class puzzle_goal_start(Range):
    """Starting affection goal for date puzzles"""
    display_name = "goal start"
    range_start = 1
    range_end = 9999
    default = 200

class puzzle_goal_add(Range):
    """affection added to the starting goal based on how many pairs you have taken on dates"""
    display_name = "goal addition"
    range_start = 1
    range_end = 999
    default = 25

class puzzle_goal_boss(Range):
    """affection goal for boss puzzles"""
    display_name = "goal boss"
    range_start = 1
    range_end = 9999
    default = 5000

class puzzle_moves(Range):
    """moves you start a puzzle with (EASY MODE=30, NORMAL MODE=25, HARD MODE=20) NOTE: boss fight will start with 4x this number caped at 999"""
    display_name = "puzzle moves"
    range_start = 10
    range_end = 999
    default = 25


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
    enabled_girls: enabled_girls
    lovers_instead_wings: lovers_instead_wings
    puzzle_goal_start: puzzle_goal_start
    puzzle_goal_add: puzzle_goal_add
    puzzle_goal_boss: puzzle_goal_boss
    disable_outfits: disable_outfits
    puzzle_moves: puzzle_moves