import random
from typing import Any, Dict

from BaseClasses import ItemClassification, Region
from Utils import visualize_regions
from worlds.AutoWorld import World
from .Items import item_table, HP2Item, fairy_wings_table, gift_unique_table, girl_unlock_table, pair_unlock_table, \
    tokekn_lvup_table

from .Locations import location_table, HP2Location, shoe_item_locaion_table, unique_item_location_table
from .Options import HP2Options
from ..generic.Rules import forbid_item


class HuniePop2(World):
    game = "Hunie Pop 2"
    item_name_to_id = {item: item_table[item].code for item in item_table}

    #item_name_groups = group_name
    location_name_to_id = {item: location_table[item].code for item in location_table}

    options = HP2Options

    pair_order = (
        ("(abia/lola)", "abia", "lola"),
        ("(lola/nora)", "lola", "nora"),
        ("(candace/nora)", "candace", "nora"),
        ("(ashley/polly)", "ashley", "polly"),
        ("(ashley/lillian)", "ashley", "lillian"),
        ("(lillian/zoey)", "lillian", "zoey"),
        ("(lailani/sarah)", "lailani", "sarah"),
        ("(jessie/lailani)", "jessie", "lailani"),
        ("(brooke/jessie)", "brooke", "jessie"),
        ("(jessie/lola)", "jessie", "lola"),
        ("(lola/zoey)", "lola", "zoey"),
        ("(abia/jessie)", "abia", "jessie"),
        ("(lailani/lillian)", "lailani", "lillian"),
        ("(abia/lillian)", "abia", "lillian"),
        ("(sarah/zoey)", "sarah", "zoey"),
        ("(polly/zoey)", "polly", "zoey"),
        ("(nora/sarah)", "nora", "sarah"),
        ("(brooke/sarah)", "brooke", "sarah"),
        ("(candace/lailani)", "candace", "lailani"),
        ("(abia/candace)", "abia", "candace"),
        ("(candace/polly)", "candace", "polly"),
        ("(ashley/nora)", "ashley", "nora"),
        ("(ashley/brooke)", "ashley", "brooke"),
        ("(brooke/polly)", "brooke", "polly")
    )
    girl_order = (
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
    )

    """
    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        for x in range(24):
            pair_region = Region(self.pair_order[x][0] + " Region", self.player, self.multiworld)
            pair_region.add_locations({"Pair Attracted " + self.pair_order[x][0]: location_table["Pair Attracted " + self.pair_order[x][0]].code}, HP2Location)
            pair_region.add_locations({"Pair Lovers " + self.pair_order[x][0]: location_table["Pair Lovers " + self.pair_order[x][0]].code}, HP2Location)
            menu_region.connect(pair_region, pair_region.name, lambda state: state.has("Pair Unlock " + self.pair_order[x][0], self.player) and state.has("Unlock Girl(" + self.pair_order[x][1] + ")", self.player) and state.has("Unlock Girl(" + self.pair_order[x][1] + ")", self.player))

        for x in range(12):
            girl_region = Region(self.girl_order[x] + " Region", self.player, self.multiworld)
            pair1 = ""
            pair2 = ""
            pair3 = ""
            pair4 = ""
            for pair in self.pair_order:
                if (pair[1] == self.girl_order[x] or pair[2] == self.girl_order[x]):
                    if (pair1==""):
                        pair1 = pair[0]
                    elif (pair2==""):
                        pair2 = pair[0]
                    elif (pair3==""):
                        pair3 = pair[0]
                    else:
                        pair4 = pair[0]

            for item in location_table:
                if location_table[item].girl1 == self.girl_order[x] and location_table[item].girl2 is None:
                    girl_region.add_locations({item: location_table[item].code}, HP2Location)
            menu_region.connect(girl_region, girl_region.name, lambda state: (state.has("Unlock Girl(" + self.girl_order[x] + ")", self.player) and (state.has("Pair Unlock " + pair1, self.player) or state.has("Pair Unlock " + pair2, self.player) or state.has("Pair Unlock " + pair3, self.player) or state.has("Pair Unlock " + pair4, self.player))))

        boss_region = Region("Boss Region", self.player, self.multiworld)
        menu_region.connect(boss_region, boss_region.name)#, lambda state: state.has_group_unique("fairy wings", self.player, 24))

        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")
    """

    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        hub_region = Region("Hub Region", self.player, self.multiworld)

        boss_region = Region("Boss Region", self.player, self.multiworld)

        boss_region.add_locations({"boss_location": 69420505}, HP2Location)

        pair_region1 = Region("Pair Region (abia/lola)", self.player, self.multiworld)
        pair_region2 = Region("Pair Region (lola/nora)", self.player, self.multiworld)
        pair_region3 = Region("Pair Region (candace/nora)", self.player, self.multiworld)
        pair_region4 = Region("Pair Region (ashley/polly)", self.player, self.multiworld)
        pair_region5 = Region("Pair Region (ashley/lillian)", self.player, self.multiworld)
        pair_region6 = Region("Pair Region (lillian/zoey)", self.player, self.multiworld)
        pair_region7 = Region("Pair Region (lailani/sarah)", self.player, self.multiworld)
        pair_region8 = Region("Pair Region (jessie/lailani)", self.player, self.multiworld)
        pair_region9 = Region("Pair Region (brooke/jessie)", self.player, self.multiworld)
        pair_region10 = Region("Pair Region (jessie/lola)", self.player, self.multiworld)
        pair_region11 = Region("Pair Region (lola/zoey)", self.player, self.multiworld)
        pair_region12 = Region("Pair Region (abia/jessie)", self.player, self.multiworld)
        pair_region13 = Region("Pair Region (lailani/lillian)", self.player, self.multiworld)
        pair_region14 = Region("Pair Region (abia/lillian)", self.player, self.multiworld)
        pair_region15 = Region("Pair Region (sarah/zoey)", self.player, self.multiworld)
        pair_region16 = Region("Pair Region (polly/zoey)", self.player, self.multiworld)
        pair_region17 = Region("Pair Region (nora/sarah)", self.player, self.multiworld)
        pair_region18 = Region("Pair Region (brooke/sarah)", self.player, self.multiworld)
        pair_region19 = Region("Pair Region (candace/lailani)", self.player, self.multiworld)
        pair_region20 = Region("Pair Region (abia/candace)", self.player, self.multiworld)
        pair_region21 = Region("Pair Region (candace/polly)", self.player, self.multiworld)
        pair_region22 = Region("Pair Region (ashley/nora)", self.player, self.multiworld)
        pair_region23 = Region("Pair Region (ashley/brooke)", self.player, self.multiworld)
        pair_region24 = Region("Pair Region (brooke/polly)", self.player, self.multiworld)

        pair_region1.add_locations({"Pair Attracted (abia/lola)": 69420001, "Pair Lovers (abia/lola)": 69420025},HP2Location)
        pair_region2.add_locations({"Pair Attracted (lola/nora)": 69420002, "Pair Lovers (lola/nora)": 69420026},HP2Location)
        pair_region3.add_locations({"Pair Attracted (candace/nora)": 69420003, "Pair Lovers (candace/nora)": 69420027},HP2Location)
        pair_region4.add_locations({"Pair Attracted (ashley/polly)": 69420004, "Pair Lovers (ashley/polly)": 69420028},HP2Location)
        pair_region5.add_locations({"Pair Attracted (ashley/lillian)": 69420005, "Pair Lovers (ashley/lillian)": 69420029}, HP2Location)
        pair_region6.add_locations({"Pair Attracted (lillian/zoey)": 69420006, "Pair Lovers (lillian/zoey)": 69420030},HP2Location)
        pair_region7.add_locations({"Pair Attracted (lailani/sarah)": 69420007, "Pair Lovers (lailani/sarah)": 69420031}, HP2Location)
        pair_region8.add_locations({"Pair Attracted (jessie/lailani)": 69420008, "Pair Lovers (jessie/lailani)": 69420032}, HP2Location)
        pair_region9.add_locations({"Pair Attracted (brooke/jessie)": 69420009, "Pair Lovers (brooke/jessie)": 69420033}, HP2Location)
        pair_region10.add_locations({"Pair Attracted (jessie/lola)": 69420010, "Pair Lovers (jessie/lola)": 69420034},HP2Location)
        pair_region11.add_locations({"Pair Attracted (lola/zoey)": 69420011, "Pair Lovers (lola/zoey)": 69420035},HP2Location)
        pair_region12.add_locations({"Pair Attracted (abia/jessie)": 69420012, "Pair Lovers (abia/jessie)": 69420036},HP2Location)
        pair_region13.add_locations({"Pair Attracted (lailani/lillian)": 69420013, "Pair Lovers (lailani/lillian)": 69420037}, HP2Location)
        pair_region14.add_locations({"Pair Attracted (abia/lillian)": 69420014, "Pair Lovers (abia/lillian)": 69420038},HP2Location)
        pair_region15.add_locations({"Pair Attracted (sarah/zoey)": 69420015, "Pair Lovers (sarah/zoey)": 69420039},HP2Location)
        pair_region16.add_locations({"Pair Attracted (polly/zoey)": 69420016, "Pair Lovers (polly/zoey)": 69420040},HP2Location)
        pair_region17.add_locations({"Pair Attracted (nora/sarah)": 69420017, "Pair Lovers (nora/sarah)": 69420041},HP2Location)
        pair_region18.add_locations({"Pair Attracted (brooke/sarah)": 69420018, "Pair Lovers (brooke/sarah)": 69420042},HP2Location)
        pair_region19.add_locations({"Pair Attracted (candace/lailani)": 69420019, "Pair Lovers (candace/lailani)": 69420043}, HP2Location)
        pair_region20.add_locations({"Pair Attracted (abia/candace)": 69420020, "Pair Lovers (abia/candace)": 69420044},HP2Location)
        pair_region21.add_locations({"Pair Attracted (candace/polly)": 69420021, "Pair Lovers (candace/polly)": 69420045}, HP2Location)
        pair_region22.add_locations({"Pair Attracted (ashley/nora)": 69420022, "Pair Lovers (ashley/nora)": 69420046},HP2Location)
        pair_region23.add_locations({"Pair Attracted (ashley/brooke)": 69420023, "Pair Lovers (ashley/brooke)": 69420047}, HP2Location)
        pair_region24.add_locations({"Pair Attracted (brooke/polly)": 69420024, "Pair Lovers (brooke/polly)": 69420048}, HP2Location)

        girl_region1 = Region("lola region", self.player, self.multiworld)
        girl_region2 = Region("jessie region", self.player, self.multiworld)
        girl_region3 = Region("lillian region", self.player, self.multiworld)
        girl_region4 = Region("zoey region", self.player, self.multiworld)
        girl_region5 = Region("sarah region", self.player, self.multiworld)
        girl_region6 = Region("lailani region", self.player, self.multiworld)
        girl_region7 = Region("candace region", self.player, self.multiworld)
        girl_region8 = Region("nora region", self.player, self.multiworld)
        girl_region9 = Region("brooke region", self.player, self.multiworld)
        girl_region10 = Region("ashley region", self.player, self.multiworld)
        girl_region11 = Region("abia region", self.player, self.multiworld)
        girl_region12 = Region("polly region", self.player, self.multiworld)

        girl_region1.add_locations(
            {"lola unique item 1": 69420049, "lola unique item 2": 69420050, "lola unique item 3": 69420051,
             "lola unique item 4": 69420052, "lola shoe item 1": 69420097, "lola shoe item 2": 69420098,
             "lola shoe item 3": 69420099, "lola shoe item 4": 69420100, "lola favourite drink": 69420145,
             "lola favourite Ice Cream Flavor": 69420146, "lola favourite Music Genre": 69420147,
             "lola favourite Movie Genre": 69420148, "lola favourite Online Activity": 69420149,
             "lola favourite Phone App": 69420150, "lola favourite Type Of Exercise": 69420151,
             "lola favourite Outdoor Activity": 69420152, "lola favourite Theme Park Ride": 69420153,
             "lola favourite Friday Night": 69420154, "lola favourite Sunday Morning": 69420155,
             "lola favourite Weather": 69420156, "lola favourite Holiday": 69420157, "lola favourite Pet": 69420158,
             "lola favourite School Subject": 69420159, "lola favourite Place to shop": 69420160,
             "lola favourite Trait In Partner": 69420161, "lola favourite Own Body Part": 69420162,
             "lola favourite Sex Position": 69420163, "lola favourite Porn Category": 69420164}, HP2Location)
        girl_region2.add_locations(
            {"jessie unique item 1": 69420053, "jessie unique item 2": 69420054, "jessie unique item 3": 69420055,
             "jessie unique item 4": 69420056, "jessie shoe item 1": 69420101, "jessie shoe item 2": 69420102,
             "jessie shoe item 3": 69420103, "jessie shoe item 4": 69420104, "jessie favourite drink": 69420165,
             "jessie favourite Ice Cream Flavor": 69420166, "jessie favourite Music Genre": 69420167,
             "jessie favourite Movie Genre": 69420168, "jessie favourite Online Activity": 69420169,
             "jessie favourite Phone App": 69420170, "jessie favourite Type Of Exercise": 69420171,
             "jessie favourite Outdoor Activity": 69420172, "jessie favourite Theme Park Ride": 69420173,
             "jessie favourite Friday Night": 69420174, "jessie favourite Sunday Morning": 69420175,
             "jessie favourite Weather": 69420176, "jessie favourite Holiday": 69420177,
             "jessie favourite Pet": 69420178, "jessie favourite School Subject": 69420179,
             "jessie favourite Place to shop": 69420180, "jessie favourite Trait In Partner": 69420181,
             "jessie favourite Own Body Part": 69420182, "jessie favourite Sex Position": 69420183,
             "jessie favourite Porn Category": 69420184}, HP2Location)
        girl_region3.add_locations(
            {"lillian unique item 1": 69420057, "lillian unique item 2": 69420058, "lillian unique item 3": 69420059,
             "lillian unique item 4": 69420060, "lillian shoe item 1": 69420105, "lillian shoe item 2": 69420106,
             "lillian shoe item 3": 69420107, "lillian shoe item 4": 69420108, "lillian favourite drink": 69420185,
             "lillian favourite Ice Cream Flavor": 69420186, "lillian favourite Music Genre": 69420187,
             "lillian favourite Movie Genre": 69420188, "lillian favourite Online Activity": 69420189,
             "lillian favourite Phone App": 69420190, "lillian favourite Type Of Exercise": 69420191,
             "lillian favourite Outdoor Activity": 69420192, "lillian favourite Theme Park Ride": 69420193,
             "lillian favourite Friday Night": 69420194, "lillian favourite Sunday Morning": 69420195,
             "lillian favourite Weather": 69420196, "lillian favourite Holiday": 69420197,
             "lillian favourite Pet": 69420198, "lillian favourite School Subject": 69420199,
             "lillian favourite Place to shop": 69420200, "lillian favourite Trait In Partner": 69420201,
             "lillian favourite Own Body Part": 69420202, "lillian favourite Sex Position": 69420203,
             "lillian favourite Porn Category": 69420204}, HP2Location)
        girl_region4.add_locations(
            {"zoey unique item 1": 69420061, "zoey unique item 2": 69420062, "zoey unique item 3": 69420063,
             "zoey unique item 4": 69420064, "zoey shoe item 1": 69420109, "zoey shoe item 2": 69420110,
             "zoey shoe item 3": 69420111, "zoey shoe item 4": 69420112, "zoey favourite drink": 69420205,
             "zoey favourite Ice Cream Flavor": 69420206, "zoey favourite Music Genre": 69420207,
             "zoey favourite Movie Genre": 69420208, "zoey favourite Online Activity": 69420209,
             "zoey favourite Phone App": 69420210, "zoey favourite Type Of Exercise": 69420211,
             "zoey favourite Outdoor Activity": 69420212, "zoey favourite Theme Park Ride": 69420213,
             "zoey favourite Friday Night": 69420214, "zoey favourite Sunday Morning": 69420215,
             "zoey favourite Weather": 69420216, "zoey favourite Holiday": 69420217, "zoey favourite Pet": 69420218,
             "zoey favourite School Subject": 69420219, "zoey favourite Place to shop": 69420220,
             "zoey favourite Trait In Partner": 69420221, "zoey favourite Own Body Part": 69420222,
             "zoey favourite Sex Position": 69420223, "zoey favourite Porn Category": 69420224}, HP2Location)
        girl_region5.add_locations(
            {"sarah unique item 1": 69420065, "sarah unique item 2": 69420066, "sarah unique item 3": 69420067,
             "sarah unique item 4": 69420068, "sarah shoe item 1": 69420113, "sarah shoe item 2": 69420114,
             "sarah shoe item 3": 69420115, "sarah shoe item 4": 69420116, "sarah favourite drink": 69420225,
             "sarah favourite Ice Cream Flavor": 69420226, "sarah favourite Music Genre": 69420227,
             "sarah favourite Movie Genre": 69420228, "sarah favourite Online Activity": 69420229,
             "sarah favourite Phone App": 69420230, "sarah favourite Type Of Exercise": 69420231,
             "sarah favourite Outdoor Activity": 69420232, "sarah favourite Theme Park Ride": 69420233,
             "sarah favourite Friday Night": 69420234, "sarah favourite Sunday Morning": 69420235,
             "sarah favourite Weather": 69420236, "sarah favourite Holiday": 69420237, "sarah favourite Pet": 69420238,
             "sarah favourite School Subject": 69420239, "sarah favourite Place to shop": 69420240,
             "sarah favourite Trait In Partner": 69420241, "sarah favourite Own Body Part": 69420242,
             "sarah favourite Sex Position": 69420243, "sarah favourite Porn Category": 69420244}, HP2Location)
        girl_region6.add_locations(
            {"lailani unique item 1": 69420069, "lailani unique item 2": 69420070, "lailani unique item 3": 69420071,
             "lailani unique item 4": 69420072, "lailani shoe item 1": 69420117, "lailani shoe item 2": 69420118,
             "lailani shoe item 3": 69420119, "lailani shoe item 4": 69420120, "lailani favourite drink": 69420245,
             "lailani favourite Ice Cream Flavor": 69420246, "lailani favourite Music Genre": 69420247,
             "lailani favourite Movie Genre": 69420248, "lailani favourite Online Activity": 69420249,
             "lailani favourite Phone App": 69420250, "lailani favourite Type Of Exercise": 69420251,
             "lailani favourite Outdoor Activity": 69420252, "lailani favourite Theme Park Ride": 69420253,
             "lailani favourite Friday Night": 69420254, "lailani favourite Sunday Morning": 69420255,
             "lailani favourite Weather": 69420256, "lailani favourite Holiday": 69420257,
             "lailani favourite Pet": 69420258, "lailani favourite School Subject": 69420259,
             "lailani favourite Place to shop": 69420260, "lailani favourite Trait In Partner": 69420261,
             "lailani favourite Own Body Part": 69420262, "lailani favourite Sex Position": 69420263,
             "lailani favourite Porn Category": 69420264}, HP2Location)
        girl_region7.add_locations(
            {"candace unique item 1": 69420073, "candace unique item 2": 69420074, "candace unique item 3": 69420075,
             "candace unique item 4": 69420076, "candace shoe item 1": 69420121, "candace shoe item 2": 69420122,
             "candace shoe item 3": 69420123, "candace shoe item 4": 69420124, "candace favourite drink": 69420265,
             "candace favourite Ice Cream Flavor": 69420266, "candace favourite Music Genre": 69420267,
             "candace favourite Movie Genre": 69420268, "candace favourite Online Activity": 69420269,
             "candace favourite Phone App": 69420270, "candace favourite Type Of Exercise": 69420271,
             "candace favourite Outdoor Activity": 69420272, "candace favourite Theme Park Ride": 69420273,
             "candace favourite Friday Night": 69420274, "candace favourite Sunday Morning": 69420275,
             "candace favourite Weather": 69420276, "candace favourite Holiday": 69420277,
             "candace favourite Pet": 69420278, "candace favourite School Subject": 69420279,
             "candace favourite Place to shop": 69420280, "candace favourite Trait In Partner": 69420281,
             "candace favourite Own Body Part": 69420282, "candace favourite Sex Position": 69420283,
             "candace favourite Porn Category": 69420284}, HP2Location)
        girl_region8.add_locations(
            {"nora unique item 1": 69420077, "nora unique item 2": 69420078, "nora unique item 3": 69420079,
             "nora unique item 4": 69420080, "nora shoe item 1": 69420125, "nora shoe item 2": 69420126,
             "nora shoe item 3": 69420127, "nora shoe item 4": 69420128, "nora favourite drink": 69420285,
             "nora favourite Ice Cream Flavor": 69420286, "nora favourite Music Genre": 69420287,
             "nora favourite Movie Genre": 69420288, "nora favourite Online Activity": 69420289,
             "nora favourite Phone App": 69420290, "nora favourite Type Of Exercise": 69420291,
             "nora favourite Outdoor Activity": 69420292, "nora favourite Theme Park Ride": 69420293,
             "nora favourite Friday Night": 69420294, "nora favourite Sunday Morning": 69420295,
             "nora favourite Weather": 69420296, "nora favourite Holiday": 69420297, "nora favourite Pet": 69420298,
             "nora favourite School Subject": 69420299, "nora favourite Place to shop": 69420300,
             "nora favourite Trait In Partner": 69420301, "nora favourite Own Body Part": 69420302,
             "nora favourite Sex Position": 69420303, "nora favourite Porn Category": 69420304}, HP2Location)
        girl_region9.add_locations(
            {"brooke unique item 1": 69420081, "brooke unique item 2": 69420082, "brooke unique item 3": 69420083,
             "brooke unique item 4": 69420084, "brooke shoe item 1": 69420129, "brooke shoe item 2": 69420130,
             "brooke shoe item 3": 69420131, "brooke shoe item 4": 69420132, "brooke favourite drink": 69420305,
             "brooke favourite Ice Cream Flavor": 69420306, "brooke favourite Music Genre": 69420307,
             "brooke favourite Movie Genre": 69420308, "brooke favourite Online Activity": 69420309,
             "brooke favourite Phone App": 69420310, "brooke favourite Type Of Exercise": 69420311,
             "brooke favourite Outdoor Activity": 69420312, "brooke favourite Theme Park Ride": 69420313,
             "brooke favourite Friday Night": 69420314, "brooke favourite Sunday Morning": 69420315,
             "brooke favourite Weather": 69420316, "brooke favourite Holiday": 69420317,
             "brooke favourite Pet": 69420318, "brooke favourite School Subject": 69420319,
             "brooke favourite Place to shop": 69420320, "brooke favourite Trait In Partner": 69420321,
             "brooke favourite Own Body Part": 69420322, "brooke favourite Sex Position": 69420323,
             "brooke favourite Porn Category": 69420324}, HP2Location)
        girl_region10.add_locations(
            {"ashley unique item 1": 69420085, "ashley unique item 2": 69420086, "ashley unique item 3": 69420087,
             "ashley unique item 4": 69420088, "ashley shoe item 1": 69420133, "ashley shoe item 2": 69420134,
             "ashley shoe item 3": 69420135, "ashley shoe item 4": 69420136, "ashley favourite drink": 69420325,
             "ashley favourite Ice Cream Flavor": 69420326, "ashley favourite Music Genre": 69420327,
             "ashley favourite Movie Genre": 69420328, "ashley favourite Online Activity": 69420329,
             "ashley favourite Phone App": 69420330, "ashley favourite Type Of Exercise": 69420331,
             "ashley favourite Outdoor Activity": 69420332, "ashley favourite Theme Park Ride": 69420333,
             "ashley favourite Friday Night": 69420334, "ashley favourite Sunday Morning": 69420335,
             "ashley favourite Weather": 69420336, "ashley favourite Holiday": 69420337,
             "ashley favourite Pet": 69420338, "ashley favourite School Subject": 69420339,
             "ashley favourite Place to shop": 69420340, "ashley favourite Trait In Partner": 69420341,
             "ashley favourite Own Body Part": 69420342, "ashley favourite Sex Position": 69420343,
             "ashley favourite Porn Category": 69420344}, HP2Location)
        girl_region11.add_locations(
            {"abia unique item 1": 69420089, "abia unique item 2": 69420090, "abia unique item 3": 69420091,
             "abia unique item 4": 69420092, "abia shoe item 1": 69420137, "abia shoe item 2": 69420138,
             "abia shoe item 3": 69420139, "abia shoe item 4": 69420140, "abia favourite drink": 69420345,
             "abia favourite Ice Cream Flavor": 69420346, "abia favourite Music Genre": 69420347,
             "abia favourite Movie Genre": 69420348, "abia favourite Online Activity": 69420349,
             "abia favourite Phone App": 69420350, "abia favourite Type Of Exercise": 69420351,
             "abia favourite Outdoor Activity": 69420352, "abia favourite Theme Park Ride": 69420353,
             "abia favourite Friday Night": 69420354, "abia favourite Sunday Morning": 69420355,
             "abia favourite Weather": 69420356, "abia favourite Holiday": 69420357, "abia favourite Pet": 69420358,
             "abia favourite School Subject": 69420359, "abia favourite Place to shop": 69420360,
             "abia favourite Trait In Partner": 69420361, "abia favourite Own Body Part": 69420362,
             "abia favourite Sex Position": 69420363, "abia favourite Porn Category": 69420364}, HP2Location)
        girl_region12.add_locations(
            {"polly unique item 1": 69420093, "polly unique item 2": 69420094, "polly unique item 3": 69420095,
             "polly unique item 4": 69420096, "polly shoe item 1": 69420141, "polly shoe item 2": 69420142,
             "polly shoe item 3": 69420143, "polly shoe item 4": 69420144, "polly favourite drink": 69420365,
             "polly favourite Ice Cream Flavor": 69420366, "polly favourite Music Genre": 69420367,
             "polly favourite Movie Genre": 69420368, "polly favourite Online Activity": 69420369,
             "polly favourite Phone App": 69420370, "polly favourite Type Of Exercise": 69420371,
             "polly favourite Outdoor Activity": 69420372, "polly favourite Theme Park Ride": 69420373,
             "polly favourite Friday Night": 69420374, "polly favourite Sunday Morning": 69420375,
             "polly favourite Weather": 69420376, "polly favourite Holiday": 69420377, "polly favourite Pet": 69420378,
             "polly favourite School Subject": 69420379, "polly favourite Place to shop": 69420380,
             "polly favourite Trait In Partner": 69420381, "polly favourite Own Body Part": 69420382,
             "polly favourite Sex Position": 69420383, "polly favourite Porn Category": 69420384}, HP2Location)

        menu_region.connect(hub_region, "menu-hub")

        hub_region.connect(pair_region1, "hub-pair(abia/lola)",
                           lambda state: state.has("Pair Unlock (abia/lola)", self.player))
        hub_region.connect(pair_region2, "hub-pair(lola/nora)",
                           lambda state: state.has("Pair Unlock (lola/nora)", self.player))
        hub_region.connect(pair_region3, "hub-pair(candace/nora)",
                           lambda state: state.has("Pair Unlock (candace/nora)", self.player))
        hub_region.connect(pair_region4, "hub-pair(ashley/polly)",
                           lambda state: state.has("Pair Unlock (ashley/polly)", self.player))
        hub_region.connect(pair_region5, "hub-pair(ashley/lillian)",
                           lambda state: state.has("Pair Unlock (ashley/lillian)", self.player))
        hub_region.connect(pair_region6, "hub-pair(lillian/zoey)",
                           lambda state: state.has("Pair Unlock (lillian/zoey)", self.player))
        hub_region.connect(pair_region7, "hub-pair(lailani/sarah)",
                           lambda state: state.has("Pair Unlock (lailani/sarah)", self.player))
        hub_region.connect(pair_region8, "hub-pair(jessie/lailani)",
                           lambda state: state.has("Pair Unlock (jessie/lailani)", self.player))
        hub_region.connect(pair_region9, "hub-pair(brooke/jessie)",
                           lambda state: state.has("Pair Unlock (brooke/jessie)", self.player))
        hub_region.connect(pair_region10, "hub-pair(jessie/lola)",
                           lambda state: state.has("Pair Unlock (jessie/lola)", self.player))
        hub_region.connect(pair_region11, "hub-pair(lola/zoey)",
                           lambda state: state.has("Pair Unlock (lola/zoey)", self.player))
        hub_region.connect(pair_region12, "hub-pair(abia/jessie)",
                           lambda state: state.has("Pair Unlock (abia/jessie)", self.player))
        hub_region.connect(pair_region13, "hub-pair(lailani/lillian)",
                           lambda state: state.has("Pair Unlock (lailani/lillian)", self.player))
        hub_region.connect(pair_region14, "hub-pair(abia/lillian)",
                           lambda state: state.has("Pair Unlock (abia/lillian)", self.player))
        hub_region.connect(pair_region15, "hub-pair(sarah/zoey)",
                           lambda state: state.has("Pair Unlock (sarah/zoey)", self.player))
        hub_region.connect(pair_region16, "hub-pair(polly/zoey)",
                           lambda state: state.has("Pair Unlock (polly/zoey)", self.player))
        hub_region.connect(pair_region17, "hub-pair(nora/sarah)",
                           lambda state: state.has("Pair Unlock (nora/sarah)", self.player))
        hub_region.connect(pair_region18, "hub-pair(brooke/sarah)",
                           lambda state: state.has("Pair Unlock (brooke/sarah)", self.player))
        hub_region.connect(pair_region19, "hub-pair(candace/lailani)",
                           lambda state: state.has("Pair Unlock (candace/lailani)", self.player))
        hub_region.connect(pair_region20, "hub-pair(abia/candace)",
                           lambda state: state.has("Pair Unlock (abia/candace)", self.player))
        hub_region.connect(pair_region21, "hub-pair(candace/polly)",
                           lambda state: state.has("Pair Unlock (candace/polly)", self.player))
        hub_region.connect(pair_region22, "hub-pair(ashley/nora)",
                           lambda state: state.has("Pair Unlock (ashley/nora)", self.player))
        hub_region.connect(pair_region23, "hub-pair(ashley/brooke)",
                           lambda state: state.has("Pair Unlock (ashley/brooke)", self.player))
        hub_region.connect(pair_region24, "hub-pair(brooke/polly)",
                           lambda state: state.has("Pair Unlock (brooke/polly)", self.player))

        hub_region.connect(girl_region1, "hub-lola", lambda state: (state.has("Unlock Girl(lola)", self.player) and ((state.has("Pair Unlock (abia/lola)",self.player) and state.has("Unlock Girl(abia)",self.player)) or (state.has("Pair Unlock (lola/nora)",self.player) and state.has("Unlock Girl(nora)",self.player)) or (state.has("Pair Unlock (jessie/lola)",self.player) and state.has("Unlock Girl(jessie)",self.player)) or (state.has("Pair Unlock (lola/zoey)",self.player) and state.has("Unlock Girl(zoey)",self.player)))))
        hub_region.connect(girl_region2, "hub-jessie", lambda state: (state.has("Unlock Girl(jessie)", self.player) and ((state.has("Pair Unlock (jessie/lailani)",self.player) and state.has("Unlock Girl(lailani)",self.player)) or (state.has("Pair Unlock (brooke/jessie)",self.player) and state.has("Unlock Girl(brooke)", self.player)) or (state.has("Pair Unlock (jessie/lola)",self.player) and state.has("Unlock Girl(lola)",self.player)) or (state.has("Pair Unlock (abia/jessie)",self.player) and state.has("Unlock Girl(abia)", self.player)))))
        hub_region.connect(girl_region3, "hub-lillian", lambda state: (state.has("Unlock Girl(lillian)", self.player) and ((state.has("Pair Unlock (ashley/lillian)",self.player) and state.has("Unlock Girl(ashley)", self.player)) or (state.has("Pair Unlock (lillian/zoey)",self.player) and state.has("Unlock Girl(zoey)",self.player)) or (state.has("Pair Unlock (lailani/lillian)",self.player) and state.has("Unlock Girl(lailani)",self.player)) or (state.has("Pair Unlock (abia/lillian)", self.player) and state.has("Unlock Girl(abia)", self.player)))))
        hub_region.connect(girl_region4, "hub-zoey", lambda state: (state.has("Unlock Girl(zoey)", self.player) and ((state.has("Pair Unlock (lillian/zoey)",self.player) and state.has("Unlock Girl(lillian)",self.player)) or (state.has("Pair Unlock (lola/zoey)",self.player) and state.has("Unlock Girl(lola)",self.player)) or (state.has("Pair Unlock (sarah/zoey)",self.player) and state.has("Unlock Girl(sarah)",self.player)) or (state.has("Pair Unlock (polly/zoey)",self.player) and state.has("Unlock Girl(polly)",self.player)))))
        hub_region.connect(girl_region5, "hub-sarah", lambda state: (state.has("Unlock Girl(sarah)", self.player) and ((state.has("Pair Unlock (lailani/sarah)",self.player) and state.has("Unlock Girl(lailani)",self.player)) or (state.has("Pair Unlock (sarah/zoey)",self.player) and state.has("Unlock Girl(zoey)",self.player)) or (state.has("Pair Unlock (nora/sarah)",self.player) and state.has("Unlock Girl(nora)",self.player)) or (state.has("Pair Unlock (brooke/sarah)",self.player) and state.has("Unlock Girl(brooke)",self.player)))))
        hub_region.connect(girl_region6, "hub-lailani", lambda state: (state.has("Unlock Girl(lailani)", self.player) and ((state.has("Pair Unlock (lailani/sarah)",self.player) and state.has("Unlock Girl(sarah)", self.player)) or (state.has("Pair Unlock (jessie/lailani)", self.player) and state.has("Unlock Girl(jessie)", self.player)) or (state.has("Pair Unlock (lailani/lillian)", self.player) and state.has("Unlock Girl(lillian)", self.player)) or (state.has("Pair Unlock (candace/lailani)", self.player) and state.has("Unlock Girl(candace)", self.player)))))
        hub_region.connect(girl_region7, "hub-candace", lambda state: (state.has("Unlock Girl(candace)", self.player) and ((state.has("Pair Unlock (candace/nora)", self.player) and state.has("Unlock Girl(nora)", self.player)) or (state.has("Pair Unlock (candace/lailani)", self.player) and state.has("Unlock Girl(lailani)", self.player)) or (state.has("Pair Unlock (abia/candace)", self.player) and state.has("Unlock Girl(abia)", self.player)) or (state.has("Pair Unlock (candace/polly)", self.player) and state.has("Unlock Girl(polly)", self.player)))))
        hub_region.connect(girl_region8, "hub-nora", lambda state: (state.has("Unlock Girl(nora)", self.player) and ((state.has("Pair Unlock (lola/nora)", self.player) and state.has("Unlock Girl(lola)", self.player)) or (state.has("Pair Unlock (candace/nora)", self.player) and state.has("Unlock Girl(candace)", self.player)) or (state.has("Pair Unlock (nora/sarah)", self.player) and state.has("Unlock Girl(sarah)", self.player)) or (state.has("Pair Unlock (ashley/nora)", self.player) and state.has("Unlock Girl(ashley)", self.player)))))
        hub_region.connect(girl_region9, "hub-brooke", lambda state: (state.has("Unlock Girl(brooke)", self.player) and ((state.has("Pair Unlock (brooke/jessie)", self.player) and state.has("Unlock Girl(jessie)", self.player)) or (state.has("Pair Unlock (brooke/sarah)", self.player) and state.has("Unlock Girl(sarah)", self.player)) or (state.has("Pair Unlock (ashley/brooke)", self.player) and state.has("Unlock Girl(ashley)", self.player)) or (state.has("Pair Unlock (brooke/polly)", self.player) and state.has("Unlock Girl(polly)", self.player)))))
        hub_region.connect(girl_region10, "hub-ashley", lambda state: (state.has("Unlock Girl(ashley)", self.player) and ((state.has("Pair Unlock (ashley/polly)", self.player) and state.has("Unlock Girl(polly)", self.player)) or (state.has("Pair Unlock (ashley/lillian)", self.player) and state.has("Unlock Girl(lillian)", self.player)) or (state.has("Pair Unlock (ashley/nora)", self.player) and state.has("Unlock Girl(nora)", self.player)) or (state.has("Pair Unlock (ashley/brooke)", self.player) and state.has("Unlock Girl(brooke)", self.player)))))
        hub_region.connect(girl_region11, "hub-abia", lambda state: (state.has("Unlock Girl(abia)", self.player) and ((state.has("Pair Unlock (abia/lola)", self.player) and state.has("Unlock Girl(lola)", self.player)) or (state.has("Pair Unlock (abia/jessie)", self.player) and state.has("Unlock Girl(jessie)", self.player)) or (state.has("Pair Unlock (abia/lillian)", self.player) and state.has("Unlock Girl(lillian)", self.player)) or (state.has("Pair Unlock (abia/candace)", self.player) and state.has("Unlock Girl(candace)", self.player)))))
        hub_region.connect(girl_region12, "hub-polly", lambda state: (state.has("Unlock Girl(polly)", self.player) and ((state.has("Pair Unlock (ashley/polly)", self.player) and state.has("Unlock Girl(ashley)", self.player)) or (state.has("Pair Unlock (polly/zoey)", self.player) and state.has("Unlock Girl(zoey)", self.player)) or (state.has("Pair Unlock (candace/polly)", self.player) and state.has("Unlock Girl(candace)", self.player)) or (state.has("Pair Unlock (brooke/polly)", self.player) and state.has("Unlock Girl(brooke)", self.player)))))

        hub_region.connect(boss_region, "hub-boss", lambda state: state.count_from_list(("Fairy Wings (abia/lola)" , "Fairy Wings (lola/nora)" , "Fairy Wings (candace/nora)" , "Fairy Wings (ashley/polly)" , "Fairy Wings (ashley/lillian)" , "Fairy Wings (lillian/zoey)" , "Fairy Wings (lailani/sarah)" , "Fairy Wings (jessie/lailani)" , "Fairy Wings (brooke/jessie)" , "Fairy Wings (jessie/lola)" , "Fairy Wings (lola/zoey)" , "Fairy Wings (abia/jessie)" , "Fairy Wings (lailani/lillian)" , "Fairy Wings (abia/lillian)" , "Fairy Wings (sarah/zoey)" , "Fairy Wings (polly/zoey)" , "Fairy Wings (nora/sarah)" , "Fairy Wings (brooke/sarah)" , "Fairy Wings (candace/lailani)" , "Fairy Wings (abia/candace)" , "Fairy Wings (candace/polly)" , "Fairy Wings (ashley/nora)" , "Fairy Wings (ashley/brooke)" , "Fairy Wings (brooke/polly)"), self.player) == 24)




    def create_item(self, name: str) -> HP2Item:
        if (name ==  "Victory"):
            return HP2Item(name, ItemClassification.progression, 69420346, self.player)
        if girl_unlock_table.get(name) is not None or pair_unlock_table.get(name) is not None or fairy_wings_table.get(name) is not None :
            return HP2Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        if tokekn_lvup_table.get(name) is not None:
            return HP2Item(name, ItemClassification.useful, self.item_name_to_id[name], self.player)
        return HP2Item(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def startingitemshelper(self):
        numpairs = 2 #self.options.number_of_staring_pairs.value
        numgirls = 4 #self.options.number_of_staring_girls.value

        returnlist = []
        pairs = random.sample(self.pair_order, k= numpairs)
        tempgirl = []
        for i in pairs:
            returnlist.append("Pair Unlock " + i[0])
            tempgirl.append(i[1])
            tempgirl.append(i[2])
        y = 1
        for x in tempgirl:
            if y > numgirls:
                break
            xstr = "Unlock Girl(" + x + ")"
            if not xstr in returnlist:
                returnlist.append(xstr)
                y += 1
        while y <= numgirls:
            zstr = "Unlock Girl(" + self.girl_order[random.randrange(0, 12)] + ")"
            if not zstr in returnlist:
                returnlist.append(zstr)
                y += 1
        return returnlist


    def create_items(self):
        starting = self.startingitemshelper()
        for item in map(self.create_item, item_table):
            if item.name in starting:
                self.multiworld.push_precollected(item)
            else:
                self.multiworld.itempool.append(item)
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(self.multiworld.itempool) -1
        self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]

    """
    def set_rules(self):

        for loc in location_table:
            if location_table[loc].girl1 == "lola" or location_table[loc].girl2 == "lola":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(lola)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/lola)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lola/nora)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (jessie/lola)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lola/zoey)", self.player)
            if location_table[loc].girl1 == "jessie" or location_table[loc].girl2 == "jessie":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(jessie)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (jessie/lailani)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (brooke/jessie)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (jessie/lola)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/jessie)", self.player)
            if location_table[loc].girl1 == "lillian" or location_table[loc].girl2 == "lillian":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(lillian)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/lillian)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lillian/zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lailani/lillian)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/lillian)", self.player)
            if location_table[loc].girl1 == "zoey" or location_table[loc].girl2 == "zoey":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lillian/zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lola/zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (sarah/zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (polly/zoey)", self.player)
            if location_table[loc].girl1 == "sarah" or location_table[loc].girl2 == "sarah":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(sarah)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lailani/sarah)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (sarah/zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (nora/sarah)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (brooke/sarah)", self.player)
            if location_table[loc].girl1 == "lailani" or location_table[loc].girl2 == "lailani":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(lailani)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lailani/sarah)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (jessie/lailani)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lailani/lillian)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (candace/lailani)", self.player)
            if location_table[loc].girl1 == "candace" or location_table[loc].girl2 == "candace":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(candace)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (candace/nora)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (candace/lailani", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/candace)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (candace/polly)", self.player)
            if location_table[loc].girl1 == "nora" or location_table[loc].girl2 == "nora":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(nora)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (lola/nora)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (candace/nora)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (nora/sarah)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/nora)", self.player)
            if location_table[loc].girl1 == "brooke" or location_table[loc].girl2 == "brooke":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(brooke)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (brooke/jessie)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (brooke/sarah)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/brooke)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (brooke/polly)", self.player)
            if location_table[loc].girl1 == "ashley" or location_table[loc].girl2 == "ashley":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(ashley)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/polly)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/lillian)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/nora)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/brooke)", self.player)
            if location_table[loc].girl1 == "abia" or location_table[loc].girl2 == "abia":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(abia)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/lola)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/jessie)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/lillian)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (abia/candace)", self.player)
            if location_table[loc].girl1 == "polly" or location_table[loc].girl2 == "polly":
                forbid_item(self.multiworld.get_location(loc, self.player), "Unlock Girl(polly)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (ashley/polly)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (polly/zoey)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (candace/polly)", self.player)
                forbid_item(self.multiworld.get_location(loc, self.player), "Pair Unlock (brooke/polly)", self.player)

        for loc2 in unique_item_location_table:
            if unique_item_location_table[loc2].girl1 == "lola":
                forbid_item(self.multiworld.get_location(loc2, self.player), "lola unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lola unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lola unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lola unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "jessie":
                forbid_item(self.multiworld.get_location(loc2, self.player), "jessie unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "jessie unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "jessie unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "jessie unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "lillian":
                forbid_item(self.multiworld.get_location(loc2, self.player), "lillian unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lillian unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lillian unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lillian unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "zoey":
                forbid_item(self.multiworld.get_location(loc2, self.player), "zoey unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "zoey unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "zoey unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "zoey unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "sarah":
                forbid_item(self.multiworld.get_location(loc2, self.player), "sarah unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "sarah unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "sarah unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "sarah unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "lailani":
                forbid_item(self.multiworld.get_location(loc2, self.player), "lailani unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lailani unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lailani unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "lailani unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "candace":
                forbid_item(self.multiworld.get_location(loc2, self.player), "candace unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "candace unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "candace unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "candace unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "nora":
                forbid_item(self.multiworld.get_location(loc2, self.player), "nora unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "nora unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "nora unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "nora unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "brooke":
                forbid_item(self.multiworld.get_location(loc2, self.player), "brooke unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "brooke unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "brooke unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "brooke unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "ashley":
                forbid_item(self.multiworld.get_location(loc2, self.player), "ashley unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "ashley unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "ashley unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "ashley unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "abia":
                forbid_item(self.multiworld.get_location(loc2, self.player), "abia unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "abia unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "abia unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "abia unique item 4", self.player)
            if unique_item_location_table[loc2].girl1 == "polly":
                forbid_item(self.multiworld.get_location(loc2, self.player), "polly unique item 1", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "polly unique item 2", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "polly unique item 3", self.player)
                forbid_item(self.multiworld.get_location(loc2, self.player), "polly unique item 4", self.player)

        for loc3 in shoe_item_locaion_table:
            if shoe_item_locaion_table[loc3].girl1 == "lola":
                forbid_item(self.multiworld.get_location(loc3, self.player), "lola shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lola shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lola shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lola shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "jessie":
                forbid_item(self.multiworld.get_location(loc3, self.player), "jessie shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "jessie shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "jessie shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "jessie shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "lillian":
                forbid_item(self.multiworld.get_location(loc3, self.player), "lillian shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lillian shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lillian shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lillian shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "zoey":
                forbid_item(self.multiworld.get_location(loc3, self.player), "zoey shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "zoey shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "zoey shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "zoey shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "sarah":
                forbid_item(self.multiworld.get_location(loc3, self.player), "sarah shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "sarah shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "sarah shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "sarah shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "lailani":
                forbid_item(self.multiworld.get_location(loc3, self.player), "lailani shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lailani shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lailani shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "lailani shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "candace":
                forbid_item(self.multiworld.get_location(loc3, self.player), "candace shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "candace shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "candace shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "candace shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "nora":
                forbid_item(self.multiworld.get_location(loc3, self.player), "nora shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "nora shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "nora shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "nora shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "brooke":
                forbid_item(self.multiworld.get_location(loc3, self.player), "brooke shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "brooke shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "brooke shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "brooke shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "ashley":
                forbid_item(self.multiworld.get_location(loc3, self.player), "ashley shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "ashley shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "ashley shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "ashley shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "abia":
                forbid_item(self.multiworld.get_location(loc3, self.player), "abia shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "abia shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "abia shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "abia shoe item 4", self.player)
            if shoe_item_locaion_table[loc3].girl1 == "polly":
                forbid_item(self.multiworld.get_location(loc3, self.player), "polly shoe item 1", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "polly shoe item 2", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "polly shoe item 3", self.player)
                forbid_item(self.multiworld.get_location(loc3, self.player), "polly shoe item 4", self.player)
    """

    def set_rules(self):
        hello = ""

        self.multiworld.get_location("boss_location", self.player).place_locked_item(self.create_item("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)



        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite drink", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite drink", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite drink", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite drink", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite drink", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Ice Cream Flavor", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Music Genre", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Music Genre", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Music Genre", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Music Genre", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Music Genre", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Movie Genre", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Movie Genre", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Movie Genre", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Movie Genre", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Movie Genre", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Online Activity", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Online Activity", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Online Activity", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Online Activity", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Online Activity", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Phone App", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Phone App", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Phone App", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Phone App", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Phone App", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Type Of Exercise", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Type Of Exercise", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Type Of Exercise", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Type Of Exercise", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Outdoor Activity", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Outdoor Activity", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Outdoor Activity", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Outdoor Activity", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Theme Park Ride", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Theme Park Ride", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Theme Park Ride", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Theme Park Ride", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Friday Night", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Friday Night", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Friday Night", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Friday Night", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Friday Night", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sunday Morning", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sunday Morning", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sunday Morning", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sunday Morning", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Weather", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Weather", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Weather", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Weather", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Weather", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Holiday", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Holiday", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Holiday", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Holiday", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Holiday", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Pet", self.player), "Unlock Girl(lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Pet", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Pet", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Pet", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Pet", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite School Subject", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite School Subject", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite School Subject", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite School Subject", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite School Subject", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Place to shop", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Place to shop", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Place to shop", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Place to shop", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Place to shop", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Trait In Partner", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Trait In Partner", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Trait In Partner", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Trait In Partner", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Own Body Part", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Own Body Part", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Own Body Part", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Own Body Part", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Own Body Part", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sex Position", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sex Position", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sex Position", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sex Position", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Sex Position", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Porn Category", self.player), "Unlock Girl(lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("lola favourite Porn Category", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Porn Category", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Porn Category", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("lola favourite Porn Category", self.player),
                    "Pair Unlock (lola/zoey)", self.player)

        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite drink", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite drink", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite drink", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite drink", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite drink", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Ice Cream Flavor", self.player),
                    "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Music Genre", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Music Genre", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Music Genre", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Music Genre", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Music Genre", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Movie Genre", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Movie Genre", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Movie Genre", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Movie Genre", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Movie Genre", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Online Activity", self.player),
                    "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Online Activity", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Online Activity", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Online Activity", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Online Activity", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Phone App", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Phone App", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Phone App", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Phone App", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Phone App", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Type Of Exercise", self.player),
                    "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Type Of Exercise", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Type Of Exercise", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Type Of Exercise", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Outdoor Activity", self.player),
                    "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Outdoor Activity", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Outdoor Activity", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Outdoor Activity", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Theme Park Ride", self.player),
                    "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Theme Park Ride", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Theme Park Ride", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Theme Park Ride", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Friday Night", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Friday Night", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Friday Night", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Friday Night", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Friday Night", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sunday Morning", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sunday Morning", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sunday Morning", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sunday Morning", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Weather", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Weather", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Weather", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Weather", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Weather", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Holiday", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Holiday", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Holiday", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Holiday", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Holiday", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Pet", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Pet", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Pet", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Pet", self.player), "Pair Unlock (jessie/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Pet", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite School Subject", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite School Subject", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite School Subject", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite School Subject", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite School Subject", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Place to shop", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Place to shop", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Place to shop", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Place to shop", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Place to shop", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Trait In Partner", self.player),
                    "Unlock Girl(jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Trait In Partner", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Trait In Partner", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Trait In Partner", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Own Body Part", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Own Body Part", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Own Body Part", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Own Body Part", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Own Body Part", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sex Position", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sex Position", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sex Position", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sex Position", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Sex Position", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Porn Category", self.player), "Unlock Girl(jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Porn Category", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Porn Category", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Porn Category", self.player),
                    "Pair Unlock (jessie/lola)", self.player)
        forbid_item(self.multiworld.get_location("jessie favourite Porn Category", self.player),
                    "Pair Unlock (abia/jessie)", self.player)

        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite drink", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite drink", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite drink", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite drink", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite drink", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Ice Cream Flavor", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Music Genre", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Music Genre", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Music Genre", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Music Genre", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Music Genre", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Movie Genre", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Movie Genre", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Movie Genre", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Movie Genre", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Online Activity", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Online Activity", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Online Activity", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Online Activity", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Online Activity", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Phone App", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Phone App", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Phone App", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Phone App", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Phone App", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Type Of Exercise", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Type Of Exercise", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Type Of Exercise", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Outdoor Activity", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Outdoor Activity", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Outdoor Activity", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Theme Park Ride", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Theme Park Ride", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Theme Park Ride", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Friday Night", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Friday Night", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Friday Night", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Friday Night", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Friday Night", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sunday Morning", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sunday Morning", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sunday Morning", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Weather", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Weather", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Weather", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Weather", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Weather", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Holiday", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Holiday", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Holiday", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Holiday", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Holiday", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Pet", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Pet", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Pet", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Pet", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Pet", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite School Subject", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite School Subject", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite School Subject", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite School Subject", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite School Subject", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Place to shop", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Place to shop", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Place to shop", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Place to shop", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Place to shop", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Trait In Partner", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Trait In Partner", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Trait In Partner", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Own Body Part", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Own Body Part", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Own Body Part", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Own Body Part", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sex Position", self.player), "Unlock Girl(lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sex Position", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sex Position", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sex Position", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Sex Position", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Porn Category", self.player),
                    "Unlock Girl(lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Porn Category", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Porn Category", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Porn Category", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lillian favourite Porn Category", self.player),
                    "Pair Unlock (abia/lillian)", self.player)

        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite drink", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite drink", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite drink", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite drink", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite drink", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Ice Cream Flavor", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Music Genre", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Music Genre", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Music Genre", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Music Genre", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Music Genre", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Movie Genre", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Movie Genre", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Movie Genre", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Movie Genre", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Movie Genre", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Online Activity", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Online Activity", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Online Activity", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Online Activity", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Online Activity", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Phone App", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Phone App", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Phone App", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Phone App", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Phone App", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Type Of Exercise", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Type Of Exercise", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Type Of Exercise", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Type Of Exercise", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Type Of Exercise", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Outdoor Activity", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Outdoor Activity", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Outdoor Activity", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Outdoor Activity", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Outdoor Activity", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Theme Park Ride", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Theme Park Ride", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Theme Park Ride", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Theme Park Ride", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Theme Park Ride", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Friday Night", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Friday Night", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Friday Night", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Friday Night", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Friday Night", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sunday Morning", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sunday Morning", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sunday Morning", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sunday Morning", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sunday Morning", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Weather", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Weather", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Weather", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Weather", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Weather", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Holiday", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Holiday", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Holiday", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Holiday", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Holiday", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Pet", self.player), "Unlock Girl(zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Pet", self.player), "Pair Unlock (lillian/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Pet", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Pet", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Pet", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite School Subject", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite School Subject", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite School Subject", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite School Subject", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite School Subject", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Place to shop", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Place to shop", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Place to shop", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Place to shop", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Place to shop", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Trait In Partner", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Trait In Partner", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Trait In Partner", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Trait In Partner", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Trait In Partner", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Own Body Part", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Own Body Part", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Own Body Part", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Own Body Part", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Own Body Part", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sex Position", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sex Position", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sex Position", self.player), "Pair Unlock (lola/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sex Position", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Sex Position", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Porn Category", self.player), "Unlock Girl(zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Porn Category", self.player),
                    "Pair Unlock (lillian/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Porn Category", self.player),
                    "Pair Unlock (lola/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Porn Category", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("zoey favourite Porn Category", self.player),
                    "Pair Unlock (polly/zoey)", self.player)

        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite drink", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite drink", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite drink", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite drink", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite drink", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Ice Cream Flavor", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Music Genre", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Music Genre", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Music Genre", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Music Genre", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Music Genre", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Movie Genre", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Movie Genre", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Movie Genre", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Movie Genre", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Movie Genre", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Online Activity", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Online Activity", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Online Activity", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Online Activity", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Online Activity", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Phone App", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Phone App", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Phone App", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Phone App", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Phone App", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Type Of Exercise", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Type Of Exercise", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Type Of Exercise", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Type Of Exercise", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Type Of Exercise", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Outdoor Activity", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Outdoor Activity", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Outdoor Activity", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Outdoor Activity", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Outdoor Activity", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Theme Park Ride", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Theme Park Ride", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Theme Park Ride", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Theme Park Ride", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Theme Park Ride", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Friday Night", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Friday Night", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Friday Night", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Friday Night", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Friday Night", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sunday Morning", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sunday Morning", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sunday Morning", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sunday Morning", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sunday Morning", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Weather", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Weather", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Weather", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Weather", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Weather", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Holiday", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Holiday", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Holiday", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Holiday", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Holiday", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Pet", self.player), "Unlock Girl(sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Pet", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Pet", self.player), "Pair Unlock (sarah/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Pet", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Pet", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite School Subject", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite School Subject", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite School Subject", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite School Subject", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite School Subject", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Place to shop", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Place to shop", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Place to shop", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Place to shop", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Place to shop", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Trait In Partner", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Trait In Partner", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Trait In Partner", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Trait In Partner", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Trait In Partner", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Own Body Part", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Own Body Part", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Own Body Part", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Own Body Part", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Own Body Part", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sex Position", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sex Position", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sex Position", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sex Position", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Sex Position", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Porn Category", self.player), "Unlock Girl(sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Porn Category", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Porn Category", self.player),
                    "Pair Unlock (sarah/zoey)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Porn Category", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("sarah favourite Porn Category", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)

        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite drink", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite drink", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite drink", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite drink", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite drink", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Ice Cream Flavor", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Music Genre", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Music Genre", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Music Genre", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Music Genre", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Music Genre", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Movie Genre", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Movie Genre", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Movie Genre", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Movie Genre", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Movie Genre", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Online Activity", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Online Activity", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Online Activity", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Online Activity", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Online Activity", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Phone App", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Phone App", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Phone App", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Phone App", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Phone App", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Type Of Exercise", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Type Of Exercise", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Type Of Exercise", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Type Of Exercise", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Type Of Exercise", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Outdoor Activity", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Outdoor Activity", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Outdoor Activity", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Outdoor Activity", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Outdoor Activity", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Theme Park Ride", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Theme Park Ride", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Theme Park Ride", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Theme Park Ride", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Theme Park Ride", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Friday Night", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Friday Night", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Friday Night", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Friday Night", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Friday Night", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sunday Morning", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sunday Morning", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sunday Morning", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sunday Morning", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sunday Morning", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Weather", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Weather", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Weather", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Weather", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Weather", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Holiday", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Holiday", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Holiday", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Holiday", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Holiday", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Pet", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Pet", self.player), "Pair Unlock (lailani/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Pet", self.player), "Pair Unlock (jessie/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Pet", self.player), "Pair Unlock (lailani/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Pet", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite School Subject", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite School Subject", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite School Subject", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite School Subject", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite School Subject", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Place to shop", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Place to shop", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Place to shop", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Place to shop", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Place to shop", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Trait In Partner", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Trait In Partner", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Trait In Partner", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Trait In Partner", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Trait In Partner", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Own Body Part", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Own Body Part", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Own Body Part", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Own Body Part", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Own Body Part", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sex Position", self.player), "Unlock Girl(lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sex Position", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sex Position", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sex Position", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Sex Position", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Porn Category", self.player),
                    "Unlock Girl(lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Porn Category", self.player),
                    "Pair Unlock (lailani/sarah)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Porn Category", self.player),
                    "Pair Unlock (jessie/lailani)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Porn Category", self.player),
                    "Pair Unlock (lailani/lillian)", self.player)
        forbid_item(self.multiworld.get_location("lailani favourite Porn Category", self.player),
                    "Pair Unlock (candace/lailani)", self.player)

        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite drink", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite drink", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite drink", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite drink", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite drink", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Ice Cream Flavor", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Music Genre", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Music Genre", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Music Genre", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Music Genre", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Music Genre", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Movie Genre", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Movie Genre", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Movie Genre", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Movie Genre", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Movie Genre", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Online Activity", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Online Activity", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Online Activity", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Online Activity", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Online Activity", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Phone App", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Phone App", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Phone App", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Phone App", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Phone App", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Type Of Exercise", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Type Of Exercise", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Type Of Exercise", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Type Of Exercise", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Outdoor Activity", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Outdoor Activity", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Outdoor Activity", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Outdoor Activity", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Theme Park Ride", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Theme Park Ride", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Theme Park Ride", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Theme Park Ride", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Friday Night", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Friday Night", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Friday Night", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Friday Night", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Friday Night", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sunday Morning", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sunday Morning", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sunday Morning", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sunday Morning", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Weather", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Weather", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Weather", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Weather", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Weather", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Holiday", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Holiday", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Holiday", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Holiday", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Holiday", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Pet", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Pet", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Pet", self.player), "Pair Unlock (candace/lailani)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Pet", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Pet", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite School Subject", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite School Subject", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite School Subject", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite School Subject", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite School Subject", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Place to shop", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Place to shop", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Place to shop", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Place to shop", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Place to shop", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Trait In Partner", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Trait In Partner", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Trait In Partner", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Trait In Partner", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Own Body Part", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Own Body Part", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Own Body Part", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Own Body Part", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Own Body Part", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sex Position", self.player), "Unlock Girl(candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sex Position", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sex Position", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sex Position", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Sex Position", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Porn Category", self.player),
                    "Unlock Girl(candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Porn Category", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Porn Category", self.player),
                    "Pair Unlock (candace/lailani)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Porn Category", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("candace favourite Porn Category", self.player),
                    "Pair Unlock (candace/polly)", self.player)

        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite drink", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite drink", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite drink", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite drink", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite drink", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Ice Cream Flavor", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Music Genre", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Music Genre", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Music Genre", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Music Genre", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Music Genre", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Movie Genre", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Movie Genre", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Movie Genre", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Movie Genre", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Online Activity", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Online Activity", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Online Activity", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Online Activity", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Online Activity", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Phone App", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Phone App", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Phone App", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Phone App", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Phone App", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Type Of Exercise", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Type Of Exercise", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Type Of Exercise", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Type Of Exercise", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Outdoor Activity", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Outdoor Activity", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Outdoor Activity", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Outdoor Activity", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Theme Park Ride", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Theme Park Ride", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Theme Park Ride", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Theme Park Ride", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Friday Night", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Friday Night", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Friday Night", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Friday Night", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Friday Night", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sunday Morning", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sunday Morning", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sunday Morning", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sunday Morning", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Weather", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Weather", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Weather", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Weather", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Weather", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Holiday", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Holiday", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Holiday", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Holiday", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Holiday", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Pet", self.player), "Unlock Girl(nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Pet", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Pet", self.player), "Pair Unlock (candace/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Pet", self.player), "Pair Unlock (nora/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Pet", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite School Subject", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite School Subject", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite School Subject", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite School Subject", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite School Subject", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Place to shop", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Place to shop", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Place to shop", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Place to shop", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Place to shop", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Trait In Partner", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Trait In Partner", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Trait In Partner", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Trait In Partner", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Own Body Part", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Own Body Part", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Own Body Part", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Own Body Part", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sex Position", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sex Position", self.player), "Pair Unlock (lola/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sex Position", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sex Position", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Sex Position", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Porn Category", self.player), "Unlock Girl(nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("nora favourite Porn Category", self.player),
                    "Pair Unlock (lola/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Porn Category", self.player),
                    "Pair Unlock (candace/nora)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Porn Category", self.player),
                    "Pair Unlock (nora/sarah)", self.player)
        forbid_item(self.multiworld.get_location("nora favourite Porn Category", self.player),
                    "Pair Unlock (ashley/nora)", self.player)

        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite drink", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite drink", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite drink", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite drink", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite drink", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Ice Cream Flavor", self.player),
                    "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Music Genre", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Music Genre", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Music Genre", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Music Genre", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Music Genre", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Movie Genre", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Movie Genre", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Movie Genre", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Movie Genre", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Online Activity", self.player),
                    "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Online Activity", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Online Activity", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Online Activity", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Online Activity", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Phone App", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Phone App", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Phone App", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Phone App", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Phone App", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Type Of Exercise", self.player),
                    "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Type Of Exercise", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Type Of Exercise", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Type Of Exercise", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Outdoor Activity", self.player),
                    "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Outdoor Activity", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Outdoor Activity", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Outdoor Activity", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Theme Park Ride", self.player),
                    "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Theme Park Ride", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Theme Park Ride", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Theme Park Ride", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Friday Night", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Friday Night", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Friday Night", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Friday Night", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Friday Night", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sunday Morning", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sunday Morning", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sunday Morning", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sunday Morning", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Weather", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Weather", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Weather", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Weather", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Weather", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Holiday", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Holiday", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Holiday", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Holiday", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Holiday", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Pet", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Pet", self.player), "Pair Unlock (brooke/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Pet", self.player), "Pair Unlock (brooke/sarah)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Pet", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Pet", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite School Subject", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite School Subject", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite School Subject", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite School Subject", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite School Subject", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Place to shop", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Place to shop", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Place to shop", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Place to shop", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Place to shop", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Trait In Partner", self.player),
                    "Unlock Girl(brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Trait In Partner", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Trait In Partner", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Trait In Partner", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Own Body Part", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Own Body Part", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Own Body Part", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Own Body Part", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sex Position", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sex Position", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sex Position", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sex Position", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Sex Position", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Porn Category", self.player), "Unlock Girl(brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Porn Category", self.player),
                    "Pair Unlock (brooke/jessie)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Porn Category", self.player),
                    "Pair Unlock (brooke/sarah)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Porn Category", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("brooke favourite Porn Category", self.player),
                    "Pair Unlock (brooke/polly)", self.player)

        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite drink", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite drink", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite drink", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite drink", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite drink", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Ice Cream Flavor", self.player),
                    "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Music Genre", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Music Genre", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Music Genre", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Music Genre", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Music Genre", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Movie Genre", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Online Activity", self.player),
                    "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Online Activity", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Online Activity", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Online Activity", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Online Activity", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Phone App", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Phone App", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Phone App", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Phone App", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Phone App", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Type Of Exercise", self.player),
                    "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Outdoor Activity", self.player),
                    "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Theme Park Ride", self.player),
                    "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Friday Night", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Friday Night", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Friday Night", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Friday Night", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Friday Night", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sunday Morning", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Weather", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Weather", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Weather", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Weather", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Weather", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Holiday", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Holiday", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Holiday", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Holiday", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Holiday", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Pet", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Pet", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Pet", self.player), "Pair Unlock (ashley/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Pet", self.player), "Pair Unlock (ashley/nora)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Pet", self.player), "Pair Unlock (ashley/brooke)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite School Subject", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite School Subject", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite School Subject", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite School Subject", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite School Subject", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Place to shop", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Place to shop", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Place to shop", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Place to shop", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Place to shop", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Trait In Partner", self.player),
                    "Unlock Girl(ashley)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Own Body Part", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sex Position", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sex Position", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sex Position", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sex Position", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Sex Position", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Porn Category", self.player), "Unlock Girl(ashley)",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Porn Category", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Porn Category", self.player),
                    "Pair Unlock (ashley/lillian)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Porn Category", self.player),
                    "Pair Unlock (ashley/nora)", self.player)
        forbid_item(self.multiworld.get_location("ashley favourite Porn Category", self.player),
                    "Pair Unlock (ashley/brooke)", self.player)

        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite drink", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite drink", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite drink", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite drink", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite drink", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Ice Cream Flavor", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Music Genre", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Music Genre", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Music Genre", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Music Genre", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Music Genre", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Movie Genre", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Movie Genre", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Movie Genre", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Movie Genre", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Movie Genre", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Online Activity", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Online Activity", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Online Activity", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Online Activity", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Online Activity", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Phone App", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Phone App", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Phone App", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Phone App", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Phone App", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Type Of Exercise", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Type Of Exercise", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Outdoor Activity", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Outdoor Activity", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Theme Park Ride", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Theme Park Ride", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Friday Night", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Friday Night", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Friday Night", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Friday Night", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Friday Night", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sunday Morning", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sunday Morning", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Weather", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Weather", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Weather", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Weather", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Weather", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Holiday", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Holiday", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Holiday", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Holiday", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Holiday", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Pet", self.player), "Unlock Girl(abia)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Pet", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Pet", self.player), "Pair Unlock (abia/jessie)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Pet", self.player), "Pair Unlock (abia/lillian)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Pet", self.player), "Pair Unlock (abia/candace)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite School Subject", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite School Subject", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite School Subject", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite School Subject", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite School Subject", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Place to shop", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Place to shop", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Place to shop", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Place to shop", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Place to shop", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Trait In Partner", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Trait In Partner", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Own Body Part", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Own Body Part", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Own Body Part", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Own Body Part", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Own Body Part", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sex Position", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sex Position", self.player), "Pair Unlock (abia/lola)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sex Position", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sex Position", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Sex Position", self.player),
                    "Pair Unlock (abia/candace)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Porn Category", self.player), "Unlock Girl(abia)",
                    self.player)
        forbid_item(self.multiworld.get_location("abia favourite Porn Category", self.player),
                    "Pair Unlock (abia/lola)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Porn Category", self.player),
                    "Pair Unlock (abia/jessie)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Porn Category", self.player),
                    "Pair Unlock (abia/lillian)", self.player)
        forbid_item(self.multiworld.get_location("abia favourite Porn Category", self.player),
                    "Pair Unlock (abia/candace)", self.player)

        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite drink", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite drink", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite drink", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite drink", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite drink", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Ice Cream Flavor", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Ice Cream Flavor", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Music Genre", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Music Genre", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Music Genre", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Music Genre", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Music Genre", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Movie Genre", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Movie Genre", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Movie Genre", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Movie Genre", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Movie Genre", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Online Activity", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Online Activity", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Online Activity", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Online Activity", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Online Activity", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Phone App", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Phone App", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Phone App", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Phone App", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Phone App", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Type Of Exercise", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Type Of Exercise", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Type Of Exercise", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Type Of Exercise", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Type Of Exercise", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Outdoor Activity", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Outdoor Activity", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Outdoor Activity", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Outdoor Activity", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Outdoor Activity", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Theme Park Ride", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Theme Park Ride", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Theme Park Ride", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Theme Park Ride", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Theme Park Ride", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Friday Night", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Friday Night", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Friday Night", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Friday Night", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Friday Night", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sunday Morning", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sunday Morning", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sunday Morning", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sunday Morning", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sunday Morning", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Weather", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Weather", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Weather", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Weather", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Weather", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Holiday", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Holiday", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Holiday", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Holiday", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Holiday", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Pet", self.player), "Unlock Girl(polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Pet", self.player), "Pair Unlock (ashley/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Pet", self.player), "Pair Unlock (polly/zoey)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Pet", self.player), "Pair Unlock (candace/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Pet", self.player), "Pair Unlock (brooke/polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite School Subject", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite School Subject", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite School Subject", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite School Subject", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite School Subject", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Place to shop", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Place to shop", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Place to shop", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Place to shop", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Place to shop", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Trait In Partner", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Trait In Partner", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Trait In Partner", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Trait In Partner", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Trait In Partner", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Own Body Part", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Own Body Part", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Own Body Part", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Own Body Part", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Own Body Part", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sex Position", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sex Position", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sex Position", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sex Position", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Sex Position", self.player),
                    "Pair Unlock (brooke/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Porn Category", self.player), "Unlock Girl(polly)",
                    self.player)
        forbid_item(self.multiworld.get_location("polly favourite Porn Category", self.player),
                    "Pair Unlock (ashley/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Porn Category", self.player),
                    "Pair Unlock (polly/zoey)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Porn Category", self.player),
                    "Pair Unlock (candace/polly)", self.player)
        forbid_item(self.multiworld.get_location("polly favourite Porn Category", self.player),
                    "Pair Unlock (brooke/polly)", self.player)

        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "lola unique item 1", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "lola unique item 2", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "lola unique item 3", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 1", self.player), "lola unique item 4", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "lola unique item 1", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "lola unique item 2", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "lola unique item 3", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 2", self.player), "lola unique item 4", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "lola unique item 1", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "lola unique item 2", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "lola unique item 3", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 3", self.player), "lola unique item 4", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "lola unique item 1", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "lola unique item 2", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "lola unique item 3", self.player)
        forbid_item(self.multiworld.get_location("lola unique item 4", self.player), "lola unique item 4", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "lola shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "lola shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "lola shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 1", self.player), "lola shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "lola shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "lola shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "lola shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 2", self.player), "lola shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "lola shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "lola shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "lola shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 3", self.player), "lola shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "lola shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "lola shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "lola shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("lola shoe item 4", self.player), "lola shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "jessie unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "jessie unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "jessie unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 1", self.player), "jessie unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "jessie unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "jessie unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "jessie unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 2", self.player), "jessie unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "jessie unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "jessie unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "jessie unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 3", self.player), "jessie unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "jessie unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "jessie unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "jessie unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie unique item 4", self.player), "jessie unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "jessie shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "jessie shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "jessie shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 1", self.player), "jessie shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "jessie shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "jessie shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "jessie shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 2", self.player), "jessie shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "jessie shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "jessie shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "jessie shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 3", self.player), "jessie shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "jessie shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "jessie shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "jessie shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("jessie shoe item 4", self.player), "jessie shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "lillian unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "lillian unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "lillian unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 1", self.player), "lillian unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "lillian unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "lillian unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "lillian unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 2", self.player), "lillian unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "lillian unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "lillian unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "lillian unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 3", self.player), "lillian unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "lillian unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "lillian unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "lillian unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian unique item 4", self.player), "lillian unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "lillian shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "lillian shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "lillian shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 1", self.player), "lillian shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "lillian shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "lillian shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "lillian shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 2", self.player), "lillian shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "lillian shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "lillian shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "lillian shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 3", self.player), "lillian shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "lillian shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "lillian shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "lillian shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lillian shoe item 4", self.player), "lillian shoe item 4",
                    self.player)

        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "zoey unique item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "zoey unique item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "zoey unique item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 1", self.player), "zoey unique item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "zoey unique item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "zoey unique item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "zoey unique item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 2", self.player), "zoey unique item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "zoey unique item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "zoey unique item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "zoey unique item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 3", self.player), "zoey unique item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "zoey unique item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "zoey unique item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "zoey unique item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey unique item 4", self.player), "zoey unique item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "zoey shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "zoey shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "zoey shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 1", self.player), "zoey shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "zoey shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "zoey shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "zoey shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 2", self.player), "zoey shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "zoey shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "zoey shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "zoey shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 3", self.player), "zoey shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "zoey shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "zoey shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "zoey shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("zoey shoe item 4", self.player), "zoey shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "sarah unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "sarah unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "sarah unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 1", self.player), "sarah unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "sarah unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "sarah unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "sarah unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 2", self.player), "sarah unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "sarah unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "sarah unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "sarah unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 3", self.player), "sarah unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "sarah unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "sarah unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "sarah unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah unique item 4", self.player), "sarah unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "sarah shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "sarah shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "sarah shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 1", self.player), "sarah shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "sarah shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "sarah shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "sarah shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 2", self.player), "sarah shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "sarah shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "sarah shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "sarah shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 3", self.player), "sarah shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "sarah shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "sarah shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "sarah shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("sarah shoe item 4", self.player), "sarah shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "lailani unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "lailani unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "lailani unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 1", self.player), "lailani unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "lailani unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "lailani unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "lailani unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 2", self.player), "lailani unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "lailani unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "lailani unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "lailani unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 3", self.player), "lailani unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "lailani unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "lailani unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "lailani unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani unique item 4", self.player), "lailani unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "lailani shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "lailani shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "lailani shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 1", self.player), "lailani shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "lailani shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "lailani shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "lailani shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 2", self.player), "lailani shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "lailani shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "lailani shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "lailani shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 3", self.player), "lailani shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "lailani shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "lailani shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "lailani shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("lailani shoe item 4", self.player), "lailani shoe item 4",
                    self.player)

        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "candace unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "candace unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "candace unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 1", self.player), "candace unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "candace unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "candace unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "candace unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 2", self.player), "candace unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "candace unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "candace unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "candace unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 3", self.player), "candace unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "candace unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "candace unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "candace unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace unique item 4", self.player), "candace unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "candace shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "candace shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "candace shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 1", self.player), "candace shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "candace shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "candace shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "candace shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 2", self.player), "candace shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "candace shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "candace shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "candace shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 3", self.player), "candace shoe item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "candace shoe item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "candace shoe item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "candace shoe item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("candace shoe item 4", self.player), "candace shoe item 4",
                    self.player)

        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "nora unique item 1", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "nora unique item 2", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "nora unique item 3", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 1", self.player), "nora unique item 4", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "nora unique item 1", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "nora unique item 2", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "nora unique item 3", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 2", self.player), "nora unique item 4", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "nora unique item 1", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "nora unique item 2", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "nora unique item 3", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 3", self.player), "nora unique item 4", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "nora unique item 1", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "nora unique item 2", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "nora unique item 3", self.player)
        forbid_item(self.multiworld.get_location("nora unique item 4", self.player), "nora unique item 4", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "nora shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "nora shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "nora shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 1", self.player), "nora shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "nora shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "nora shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "nora shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 2", self.player), "nora shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "nora shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "nora shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "nora shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 3", self.player), "nora shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "nora shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "nora shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "nora shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("nora shoe item 4", self.player), "nora shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "brooke unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "brooke unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "brooke unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 1", self.player), "brooke unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "brooke unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "brooke unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "brooke unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 2", self.player), "brooke unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "brooke unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "brooke unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "brooke unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 3", self.player), "brooke unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "brooke unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "brooke unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "brooke unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke unique item 4", self.player), "brooke unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "brooke shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "brooke shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "brooke shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 1", self.player), "brooke shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "brooke shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "brooke shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "brooke shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 2", self.player), "brooke shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "brooke shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "brooke shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "brooke shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 3", self.player), "brooke shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "brooke shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "brooke shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "brooke shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("brooke shoe item 4", self.player), "brooke shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "ashley unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "ashley unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "ashley unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 1", self.player), "ashley unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "ashley unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "ashley unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "ashley unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 2", self.player), "ashley unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "ashley unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "ashley unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "ashley unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 3", self.player), "ashley unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "ashley unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "ashley unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "ashley unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley unique item 4", self.player), "ashley unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "ashley shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "ashley shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "ashley shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 1", self.player), "ashley shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "ashley shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "ashley shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "ashley shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 2", self.player), "ashley shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "ashley shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "ashley shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "ashley shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 3", self.player), "ashley shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "ashley shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "ashley shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "ashley shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("ashley shoe item 4", self.player), "ashley shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "abia unique item 1", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "abia unique item 2", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "abia unique item 3", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 1", self.player), "abia unique item 4", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "abia unique item 1", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "abia unique item 2", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "abia unique item 3", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 2", self.player), "abia unique item 4", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "abia unique item 1", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "abia unique item 2", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "abia unique item 3", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 3", self.player), "abia unique item 4", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "abia unique item 1", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "abia unique item 2", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "abia unique item 3", self.player)
        forbid_item(self.multiworld.get_location("abia unique item 4", self.player), "abia unique item 4", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "abia shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "abia shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "abia shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 1", self.player), "abia shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "abia shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "abia shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "abia shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 2", self.player), "abia shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "abia shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "abia shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "abia shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 3", self.player), "abia shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "abia shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "abia shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "abia shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("abia shoe item 4", self.player), "abia shoe item 4", self.player)

        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "polly unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "polly unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "polly unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 1", self.player), "polly unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "polly unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "polly unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "polly unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 2", self.player), "polly unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "polly unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "polly unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "polly unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 3", self.player), "polly unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "polly unique item 1",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "polly unique item 2",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "polly unique item 3",
                    self.player)
        forbid_item(self.multiworld.get_location("polly unique item 4", self.player), "polly unique item 4",
                    self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "polly shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "polly shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "polly shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 1", self.player), "polly shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "polly shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "polly shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "polly shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 2", self.player), "polly shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "polly shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "polly shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "polly shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 3", self.player), "polly shoe item 4", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "polly shoe item 1", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "polly shoe item 2", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "polly shoe item 3", self.player)
        forbid_item(self.multiworld.get_location("polly shoe item 4", self.player), "polly shoe item 4", self.player)



    def fill_slot_data(self) -> Dict[str, Any]:
        return self.fill_json_data()

    def fill_json_data(self) -> Dict[str, Any]:
        return {"test": "this"}