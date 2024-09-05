import random

from BaseClasses import ItemClassification, Region, CollectionState
from Utils import visualize_regions
from worlds.AutoWorld import World
from .Items import item_table, HP2Item, fairy_wings_table, gift_unique_table, girl_unlock_table, pair_unlock_table, \
    tokekn_lvup_table, gift_shoe_table, baggage_table

from .Locations import location_table, HP2Location
from .Options import HP2Options, starting_pairs, starting_girls
from ..generic.Rules import forbid_item, set_rule


class HuniePop2(World):
    game = "Hunie Pop 2"
    item_name_to_id = item_table

    options_dataclass = HP2Options
    options = HP2Options

    startingpairs = []
    startinggirls = []
    shopslots = 0
    trashitems = 0


    location_name_to_id = location_table

    pair_order = (
        "(abia/lola)",
        "(lola/nora)",
        "(candace/nora)",
        "(ashley/polly)",
        "(ashley/lillian)",
        "(lillian/zoey)",
        "(lailani/sarah)",
        "(jessie/lailani)",
        "(brooke/jessie)",
        "(jessie/lola)",
        "(lola/zoey)",
        "(abia/jessie)",
        "(lailani/lillian)",
        "(abia/lillian)",
        "(sarah/zoey)",
        "(polly/zoey)",
        "(nora/sarah)",
        "(brooke/sarah)",
        "(candace/lailani)",
        "(abia/candace)",
        "(candace/polly)",
        "(ashley/nora)",
        "(ashley/brooke)",
        "(brooke/polly)"
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


    def generate_early(self):
        numpairs = self.options.number_of_staring_pairs.value
        numgirls = self.options.number_of_staring_girls.value

        pair_girls = (
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
            ("(brooke/polly)", "brooke", "polly"),
        )

        pairs = random.sample(pair_girls, k=numpairs)
        tempgirl = []
        for i in pairs:
            self.startingpairs.append(f"Pair Unlock {i[0]}")
            tempgirl.append(i[1])
            tempgirl.append(i[2])
        y = 1
        for x in tempgirl:
            if y > numgirls:
                break
            xstr = f"Unlock Girl({x})"
            if not xstr in self.startinggirls:
                self.startinggirls.append(xstr)
                y += 1
        x = 0
        while y <= numgirls and x<100:
            x += 1
            zstr = f"Unlock Girl({self.girl_order[random.randrange(0, 12)]})"
            if not zstr in self.startinggirls:
                self.startinggirls.append(zstr)
                y += 1

        totallocations = 0
        totalitems = 0

        if True: #fairy wings
            totalitems += 24
        if True: #tokenlvups
            totalitems += 32
        if True: #girl unlocks
            totalitems += 12 - len(self.startinggirls)
        if True: #pair unlocks
            totalitems += 24 - len(self.startingpairs)
        if True: #gift unique
            totalitems += 48
        if True: #gift shoe
            totalitems += 48
        if not self.options.disable_baggage.value: #baggagage
            totalitems += 36

        if True: #pair attracted/lovers
            totallocations += 48
        if True: #unique gift
            totallocations += 48
        if True: #shoe gift
            totallocations += 48
        if self.options.enable_questions.value: #favroute question
            totallocations += 240
        if self.options.number_shop_items.value > 0: #shop locations
            totallocations += self.options.number_shop_items.value

        print(f"total items:{totalitems}")
        print(f"total locations:{totallocations}")

        if totallocations != totalitems:
            if totallocations > totalitems:
                self.trashitems = totallocations-totalitems
                self.shopslots = self.options.number_shop_items.value
            else:
                self.shopslots = totalitems - (totallocations - self.options.number_shop_items.value)

    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        hub_region = Region("Hub Region", self.player, self.multiworld)
        menu_region.connect(hub_region, "menu-hub")

        boss_region = Region("Boss Region", self.player, self.multiworld)
        boss_region.add_locations({"boss_location": 69420505}, HP2Location)


        print(f"total shop slots:{self.shopslots}")
        if self.shopslots > 0:
            shop_region = Region("Shop Region", self.player, self.multiworld)
            hub_region.connect(shop_region, "hub-shop")
            for i in range(self.shopslots):
                self.location_name_to_id[f"shop_location: {i+1}"] = 69420506+i
                shop_region.add_locations({f"shop_location: {i+1}" : 69420506+i}, HP2Location)

        for pair in self.pair_order:
            pairregion = Region(f"{pair} Region", self.player, self.multiworld)
            pairregion.add_locations({
                f"Pair Attracted {pair}":self.location_name_to_id[f"Pair Attracted {pair}"],
                f"Pair Lovers {pair}":self.location_name_to_id[f"Pair Lovers {pair}"]
            }, HP2Location)
            hub_region.connect(pairregion, f"hub-pair{pair}")

        for girl in self.girl_order:
            girlregion = Region(f"{girl} Region", self.player, self.multiworld)
            if self.options.enable_questions:
                girlregion.add_locations({
                    f"{girl} favourite drink": self.location_name_to_id[f"{girl} favourite drink"],
                    f"{girl} favourite Ice Cream Flavor": self.location_name_to_id[f"{girl} favourite Ice Cream Flavor"],
                    f"{girl} favourite Music Genre": self.location_name_to_id[f"{girl} favourite Music Genre"],
                    f"{girl} favourite Movie Genre": self.location_name_to_id[f"{girl} favourite Movie Genre"],
                    f"{girl} favourite Online Activity": self.location_name_to_id[f"{girl} favourite Online Activity"],
                    f"{girl} favourite Phone App": self.location_name_to_id[f"{girl} favourite Phone App"],
                    f"{girl} favourite Type Of Exercise": self.location_name_to_id[f"{girl} favourite Type Of Exercise"],
                    f"{girl} favourite Outdoor Activity": self.location_name_to_id[f"{girl} favourite Outdoor Activity"],
                    f"{girl} favourite Theme Park Ride": self.location_name_to_id[f"{girl} favourite Theme Park Ride"],
                    f"{girl} favourite Friday Night": self.location_name_to_id[f"{girl} favourite Friday Night"],
                    f"{girl} favourite Sunday Morning": self.location_name_to_id[f"{girl} favourite Sunday Morning"],
                    f"{girl} favourite Weather": self.location_name_to_id[f"{girl} favourite Weather"],
                    f"{girl} favourite Holiday": self.location_name_to_id[f"{girl} favourite Holiday"],
                    f"{girl} favourite Pet": self.location_name_to_id[f"{girl} favourite Pet"],
                    f"{girl} favourite School Subject": self.location_name_to_id[f"{girl} favourite School Subject"],
                    f"{girl} favourite Place to shop": self.location_name_to_id[f"{girl} favourite Place to shop"],
                    f"{girl} favourite Trait In Partner": self.location_name_to_id[f"{girl} favourite Trait In Partner"],
                    f"{girl} favourite Own Body Part": self.location_name_to_id[f"{girl} favourite Own Body Part"],
                    f"{girl} favourite Sex Position": self.location_name_to_id[f"{girl} favourite Sex Position"],
                    f"{girl} favourite Porn Category": self.location_name_to_id[f"{girl} favourite Porn Category"]
                }, HP2Location)

            girlregion.add_locations({
                f"{girl} unique gift 1": self.location_name_to_id[f"{girl} unique gift 1"],
                f"{girl} unique gift 2": self.location_name_to_id[f"{girl} unique gift 2"],
                f"{girl} unique gift 3": self.location_name_to_id[f"{girl} unique gift 3"],
                f"{girl} unique gift 4": self.location_name_to_id[f"{girl} unique gift 4"],
                f"{girl} shoe gift 1": self.location_name_to_id[f"{girl} shoe gift 1"],
                f"{girl} shoe gift 2": self.location_name_to_id[f"{girl} shoe gift 2"],
                f"{girl} shoe gift 3": self.location_name_to_id[f"{girl} shoe gift 3"],
                f"{girl} shoe gift 4": self.location_name_to_id[f"{girl} shoe gift 4"]}, HP2Location)

            hub_region.connect(girlregion, f"hub-{girl}")


            #girlshoe1region = Region(f"{girl} Shoe 1 Region", self.player, self.multiworld)
            #girlshoe1region.add_locations({f"{girl} shoe gift 1": self.location_name_to_id[f"{girl} shoe gift 1"]})
            #girlregion.connect(girlshoe1region, f"{girl}-shoe1")
            #girlshoe2region = Region(f"{girl} Shoe 2 Region", self.player, self.multiworld)
            #girlshoe2region.add_locations({f"{girl} shoe gift 2": self.location_name_to_id[f"{girl} shoe gift 2"]})
            #girlregion.connect(girlshoe2region, f"{girl}-shoe2")
            #girlshoe3region = Region(f"{girl} Shoe 3 Region", self.player, self.multiworld)
            #girlshoe3region.add_locations({f"{girl} shoe gift 3": self.location_name_to_id[f"{girl} shoe gift 3"]})
            #girlregion.connect(girlshoe3region, f"{girl}-shoe3")
            #girlshoe4region = Region(f"{girl} Shoe 4 Region", self.player, self.multiworld)
            #girlshoe4region.add_locations({f"{girl} shoe gift 4": self.location_name_to_id[f"{girl} shoe gift 4"]})
            #girlregion.connect(girlshoe4region, f"{girl}-shoe4")


        hub_region.connect(boss_region, "hub-boss", lambda state: state.count_from_list(("Fairy Wings (abia/lola)" , "Fairy Wings (lola/nora)" , "Fairy Wings (candace/nora)" , "Fairy Wings (ashley/polly)" , "Fairy Wings (ashley/lillian)" , "Fairy Wings (lillian/zoey)" , "Fairy Wings (lailani/sarah)" , "Fairy Wings (jessie/lailani)" , "Fairy Wings (brooke/jessie)" , "Fairy Wings (jessie/lola)" , "Fairy Wings (lola/zoey)" , "Fairy Wings (abia/jessie)" , "Fairy Wings (lailani/lillian)" , "Fairy Wings (abia/lillian)" , "Fairy Wings (sarah/zoey)" , "Fairy Wings (polly/zoey)" , "Fairy Wings (nora/sarah)" , "Fairy Wings (brooke/sarah)" , "Fairy Wings (candace/lailani)" , "Fairy Wings (abia/candace)" , "Fairy Wings (candace/polly)" , "Fairy Wings (ashley/nora)" , "Fairy Wings (ashley/brooke)" , "Fairy Wings (brooke/polly)"), self.player) == 24)




    def create_item(self, name: str) -> HP2Item:
        if (name ==  "Victory"):
            return HP2Item(name, ItemClassification.progression, 69420346, self.player)
        if girl_unlock_table.get(name) is not None or pair_unlock_table.get(name) is not None or fairy_wings_table.get(name) is not None or gift_unique_table.get(name) is not None or gift_shoe_table.get(name) is not None:
            return HP2Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        if tokekn_lvup_table.get(name) is not None :
            return HP2Item(name, ItemClassification.useful, self.item_name_to_id[name], self.player)
        return HP2Item(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_items(self):
        for pair in pair_unlock_table:
            if pair in self.startingpairs:
                self.multiworld.push_precollected(self.create_item(pair))
            else:
                self.multiworld.itempool.append(self.create_item(pair))

        for girl in girl_unlock_table:
            if girl in self.startinggirls:
                self.multiworld.push_precollected(self.create_item(girl))
            else:
                self.multiworld.itempool.append(self.create_item(girl))

        if True:
            for wing in fairy_wings_table:
                self.multiworld.itempool.append(self.create_item(wing))

        if True:
            for token in tokekn_lvup_table:
                self.multiworld.itempool.append(self.create_item(token))

        if True:
            for bag in baggage_table:
                self.multiworld.itempool.append(self.create_item(bag))

        if True:
            for unique in gift_unique_table:
                self.multiworld.itempool.append(self.create_item(unique))

        if True:
            for shoe in gift_shoe_table:
                self.multiworld.itempool.append(self.create_item(shoe))


        print(f"total trash items:{self.trashitems}")
        print(f"total itempool done:{len(self.multiworld.itempool)}")
        print(f"total unfilled done:{len(self.multiworld.get_unfilled_locations(self.player))}")
        if self.trashitems > 0:
            self.multiworld.itempool += [self.create_item("nothing") for _ in range(self.trashitems)]


    def set_rules(self):


        self.multiworld.get_location("boss_location", self.player).place_locked_item(self.create_item("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)


        girl_pairs = {
            "lola": ("(abia/lola)", "(lola/nora)", "(jessie/lola)", "(lola/zoey)"),
            "jessie": ("(jessie/lailani)", "(brooke/jessie)", "(jessie/lola)", "(abia/jessie)"),
            "lillian": ("(ashley/lillian)", "(lillian/zoey)", "(lailani/lillian)", "(abia/lillian)"),
            "zoey": ("(lillian/zoey)", "(lola/zoey)", "(sarah/zoey)", "(polly/zoey)"),
            "sarah": ("(lailani/sarah)", "(sarah/zoey)", "(nora/sarah)", "(brooke/sarah)"),
            "lailani": ("(lailani/sarah)", "(jessie/lailani)", "(lailani/lillian)", "(candace/lailani)"),
            "candace": ("(candace/nora)", "(candace/lailani)", "(abia/candace)", "(candace/polly)"),
            "nora": ("(lola/nora)", "(candace/nora)", "(nora/sarah)", "(ashley/nora)"),
            "brooke": ("(brooke/jessie)", "(brooke/sarah)", "(ashley/brooke)", "(brooke/polly)"),
            "ashley": ("(ashley/polly)", "(ashley/lillian)", "(ashley/nora)", "(ashley/brooke)"),
            "abia": ("(abia/candace)", "(abia/lillian)", "(abia/lola)", "(abia/jessie)"),
            "polly": ("(brooke/polly)""(candace/polly)", "(polly/zoey)", "(ashley/polly)")
        }
        for girl in self.girl_order:
            forbid_item(self.multiworld.get_location(f"{girl} unique gift 1", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} unique gift 2", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} unique gift 3", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} unique gift 4", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} shoe gift 1", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} shoe gift 2", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} shoe gift 3", self.player), f"Unlock Girl({girl})", self.player)
            forbid_item(self.multiworld.get_location(f"{girl} shoe gift 4", self.player), f"Unlock Girl({girl})", self.player)
            if self.options.enable_questions:
                forbid_item(self.multiworld.get_location(f"{girl} favourite drink", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Ice Cream Flavor", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Music Genre", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Movie Genre", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Online Activity", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Phone App", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Type Of Exercise", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Outdoor Activity", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Theme Park Ride", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Friday Night", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Sunday Morning", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Weather", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Holiday", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Pet", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite School Subject", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Place to shop", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Trait In Partner", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Own Body Part", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Sex Position", self.player), f"Unlock Girl({girl})", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} favourite Porn Category", self.player), f"Unlock Girl({girl})", self.player)
            for pair in girl_pairs[girl]:
                forbid_item(self.multiworld.get_location(f"{girl} unique gift 1", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} unique gift 2", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} unique gift 3", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} unique gift 4", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} shoe gift 1", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} shoe gift 2", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} shoe gift 3", self.player), f"Pair Unlock {pair}", self.player)
                forbid_item(self.multiworld.get_location(f"{girl} shoe gift 4", self.player), f"Pair Unlock {pair}", self.player)
                if self.options.enable_questions:
                    forbid_item(self.multiworld.get_location(f"{girl} favourite drink", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Ice Cream Flavor", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Music Genre", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Movie Genre", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Online Activity", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Phone App", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Type Of Exercise", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Outdoor Activity", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Theme Park Ride", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Friday Night", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Sunday Morning", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Weather", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Holiday", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Pet", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite School Subject", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Place to shop", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Trait In Partner", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Own Body Part", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Sex Position", self.player), f"Pair Unlock {pair}", self.player)
                    forbid_item(self.multiworld.get_location(f"{girl} favourite Porn Category", self.player), f"Pair Unlock {pair}", self.player)
        girl_girlpair = {
            "lola": (("Pair Unlock (abia/lola)", "Unlock Girl(abia)"),("Pair Unlock (lola/nora)", "Unlock Girl(nora)"),("Pair Unlock (jessie/lola)", "Unlock Girl(jessie)"),("Pair Unlock (lola/zoey)", "Unlock Girl(zoey)")),
            "jessie": (("Pair Unlock (jessie/lailani)", "Unlock Girl(lailani)"),("Pair Unlock (brooke/jessie)", "Unlock Girl(brooke)"),("Pair Unlock (jessie/lola)", "Unlock Girl(lola)"),("Pair Unlock (abia/jessie)", "Unlock Girl(abia)")),
            "lillian": (("Pair Unlock (ashley/lillian)", "Unlock Girl(ashley)"),("Pair Unlock (lillian/zoey)", "Unlock Girl(zoey)"),("Pair Unlock (lailani/lillian)", "Unlock Girl(lailani)"),("Pair Unlock (abia/lillian)", "Unlock Girl(abia)")),
            "zoey": (("Pair Unlock (lillian/zoey)", "Unlock Girl(lillian)"),("Pair Unlock (lola/zoey)", "Unlock Girl(lola)"),("Pair Unlock (sarah/zoey)", "Unlock Girl(sarah)"),("Pair Unlock (polly/zoey)", "Unlock Girl(polly)")),
            "sarah": (("Pair Unlock (lailani/sarah)", "Unlock Girl(lailani)"),("Pair Unlock (sarah/zoey)", "Unlock Girl(zoey)"),("Pair Unlock (nora/sarah)", "Unlock Girl(nora)"),("Pair Unlock (brooke/sarah)", "Unlock Girl(brooke)")),
            "lailani": (("Pair Unlock (lailani/sarah)", "Unlock Girl(sarah)"),("Pair Unlock (jessie/lailani)", "Unlock Girl(jessie)"),("Pair Unlock (lailani/lillian)", "Unlock Girl(lillian)"),("Pair Unlock (candace/lailani)", "Unlock Girl(candace)")),
            "candace": (("Pair Unlock (candace/nora)", "Unlock Girl(nora)"),("Pair Unlock (candace/lailani)", "Unlock Girl(lailani)"),("Pair Unlock (abia/candace)", "Unlock Girl(abia)"),("Pair Unlock (candace/polly)", "Unlock Girl(polly)")),
            "nora": (("Pair Unlock (lola/nora)", "Unlock Girl(lola)"),("Pair Unlock (candace/nora)", "Unlock Girl(candace)"),("Pair Unlock (nora/sarah)", "Unlock Girl(sarah)"),("Pair Unlock (ashley/nora)", "Unlock Girl(ashley)")),
            "brooke": (("Pair Unlock (brooke/jessie)", "Unlock Girl(jessie)"),("Pair Unlock (brooke/sarah)", "Unlock Girl(sarah)"),("Pair Unlock (ashley/brooke)", "Unlock Girl(ashley)"),("Pair Unlock (brooke/polly)", "Unlock Girl(polly)")),
            "ashley": (("Pair Unlock (ashley/polly)", "Unlock Girl(polly)"),("Pair Unlock (ashley/lillian)", "Unlock Girl(lillian)"),("Pair Unlock (ashley/nora)", "Unlock Girl(nora)"),("Pair Unlock (ashley/brooke)", "Unlock Girl(brooke)")),
            "abia": (("Pair Unlock (abia/candace)", "Unlock Girl(candace)"),("Pair Unlock (abia/lillian)", "Unlock Girl(lillian)"),("Pair Unlock (abia/lola)", "Unlock Girl(lola)"),("Pair Unlock (abia/jessie)", "Unlock Girl(jessie)")),
            "polly": (("Pair Unlock (brooke/polly)", "Unlock Girl(brooke)"),("Pair Unlock (candace/polly)", "Unlock Girl(candace)"),("Pair Unlock (polly/zoey)", "Unlock Girl(zoey)"),("Pair Unlock (ashley/polly)", "Unlock Girl(ashley)"))
        }
        for girl in girl_girlpair:
            set_rule(self.multiworld.get_entrance(f"hub-{girl}", self.player), lambda state: (state.has(f"Unlock Girl({girl})", self.player) and ( state.has_all(girl_girlpair[girl][0], self.player) or state.has_all(girl_girlpair[girl][1], self.player) or state.has_all(girl_girlpair[girl][2], self.player) or state.has_all(girl_girlpair[girl][3], self.player))))

            set_rule(self.multiworld.get_location(f"{girl} unique gift 1", self.player), lambda state: state.has(f"{girl} unique item 1", self.player))
            set_rule(self.multiworld.get_location(f"{girl} unique gift 2", self.player), lambda state: state.has(f"{girl} unique item 2", self.player))
            set_rule(self.multiworld.get_location(f"{girl} unique gift 3", self.player), lambda state: state.has(f"{girl} unique item 3", self.player))
            set_rule(self.multiworld.get_location(f"{girl} unique gift 4", self.player), lambda state: state.has(f"{girl} unique item 4", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 1", self.player), lambda state: state.has(f"{girl} shoe item 1", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 2", self.player), lambda state: state.has(f"{girl} shoe item 2", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 3", self.player), lambda state: state.has(f"{girl} shoe item 3", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 4", self.player), lambda state: state.has(f"{girl} shoe item 4", self.player))


            #set_rule(self.multiworld.get_entrance(f"{girl}-unique1", self.player), lambda state: state.has(f"{girl} unique item 1", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-unique2", self.player), lambda state: state.has(f"{girl} unique item 2", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-unique3", self.player), lambda state: state.has(f"{girl} unique item 3", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-unique4", self.player), lambda state: state.has(f"{girl} unique item 4", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-shoe1", self.player), lambda state: state.has(f"{girl} shoe item 1", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-shoe2", self.player), lambda state: state.has(f"{girl} shoe item 2", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-shoe3", self.player), lambda state: state.has(f"{girl} shoe item 3", self.player))
            #set_rule(self.multiworld.get_entrance(f"{girl}-shoe4", self.player), lambda state: state.has(f"{girl} shoe item 4", self.player))



        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def fill_slot_data(self) -> dict:
        returndict = {
            "number_blue_fruit": self.options.number_blue_fruit.value,
            "number_green_fruit": self.options.number_green_fruit.value,
            "number_orange_fruit": self.options.number_orange_fruit.value,
            "number_red_fruit": self.options.number_red_fruit.value,
            "number_shop_items": self.options.number_shop_items.value,
            "enable_questions": self.options.enable_questions.value,
            "disable_baggage": self.options.disable_baggage.value
        }
        return returndict