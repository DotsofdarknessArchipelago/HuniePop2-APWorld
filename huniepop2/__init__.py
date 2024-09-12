import random

from BaseClasses import ItemClassification, Region, CollectionState
from Utils import visualize_regions
from worlds.AutoWorld import World
from .Items import item_table, HP2Item, fairy_wings_table, gift_unique_table, girl_unlock_table, pair_unlock_table, \
    tokekn_lvup_table, gift_shoe_table, baggage_table

from .Locations import location_table, HP2Location
from .Options import HP2Options, starting_pairs, starting_girls
from ..generic.Rules import forbid_item, set_rule, add_rule


class HuniePop2(World):
    game = "Hunie Pop 2"
    item_name_to_id = item_table

    options_dataclass = HP2Options
    options: HP2Options

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

    girls_enabled = set()
    pairs_enabled = set()


    def generate_early(self):
        numpairs = self.options.number_of_staring_pairs.value
        numgirls = self.options.number_of_staring_girls.value

        self.startingpairs = []
        self.startinggirls = []

        self.girls_enabled = self.options.enabled_girls.value

        pair_girls = set()

        if "lola" in self.girls_enabled:
            if "abia" in self.girls_enabled:
                pair_girls.add(("(abia/lola)", "abia", "lola"))
            if "nora" in self.girls_enabled:
                pair_girls.add(("(lola/nora)", "lola", "nora"))
            if "jessie" in self.girls_enabled:
                pair_girls.add(("(jessie/lola)", "jessie", "lola"))
            if "zoey" in self.girls_enabled:
                pair_girls.add(("(lola/zoey)", "lola", "zoey"))
        if "jessie" in self.girls_enabled:
            if "lailani" in self.girls_enabled:
                pair_girls.add(("(jessie/lailani)", "jessie", "lailani"))
            if "brooke" in self.girls_enabled:
                pair_girls.add(("(brooke/jessie)", "brooke", "jessie"))
            #if "lola" in self.girls_enabled:
            #    pair_girls.add(("(jessie/lola)", "jessie", "lola"))
            if "abia" in self.girls_enabled:
                pair_girls.add(("(abia/jessie)", "abia", "jessie"))
        if "lillian" in self.girls_enabled:
            if "ashley" in self.girls_enabled:
                pair_girls.add(("(ashley/lillian)", "ashley", "lillian"))
            if "zoey" in self.girls_enabled:
                pair_girls.add(("(lillian/zoey)", "lillian", "zoey"))
            if "lailani" in self.girls_enabled:
                pair_girls.add(("(lailani/lillian)", "lailani", "lillian"))
            if "abia" in self.girls_enabled:
                pair_girls.add(("(abia/lillian)", "abia", "lillian"))
        if "zoey" in self.girls_enabled:
            #if "lillian" in self.girls_enabled:
            #    pair_girls.add(("(lillian/zoey)", "lillian", "zoey"))
            #if "lola" in self.girls_enabled:
            #    pair_girls.add(("(lola/zoey)", "lola", "zoey"))
            if "sarah" in self.girls_enabled:
                pair_girls.add(("(sarah/zoey)", "sarah", "zoey"))
            if "polly" in self.girls_enabled:
                pair_girls.add(("(polly/zoey)", "polly", "zoey"))
        if "sarah" in self.girls_enabled:
            if "lailani" in self.girls_enabled:
                pair_girls.add(("(lailani/sarah)", "lailani", "sarah"))
            #if "zoey" in self.girls_enabled:
            #    pair_girls.add(("(sarah/zoey)", "sarah", "zoey"))
            if "nora" in self.girls_enabled:
                pair_girls.add(("(nora/sarah)", "nora", "sarah"))
            if "brooke" in self.girls_enabled:
                pair_girls.add(("(brooke/sarah)", "brooke", "sarah"))
        if "lailani" in self.girls_enabled:
            #if "sarah" in self.girls_enabled:
            #    pair_girls.add(("(lailani/sarah)", "lailani", "sarah"))
            #if "jessie" in self.girls_enabled:
            #    pair_girls.add(("(jessie/lailani)", "jessie", "lailani"))
            #if "lillian" in self.girls_enabled:
            #    pair_girls.add(("(lailani/lillian)", "lailani", "lillian"))
            if "candace" in self.girls_enabled:
                pair_girls.add(("(candace/lailani)", "candace", "lailani"))
        if "candace" in self.girls_enabled:
            if "nora" in self.girls_enabled:
                pair_girls.add(("(candace/nora)", "candace", "nora"))
            #if "lailani" in self.girls_enabled:
            #    pair_girls.add(("(candace/lailani)", "candace", "lailani"))
            if "abia" in self.girls_enabled:
                pair_girls.add(("(abia/candace)", "abia", "candace"))
            if "polly" in self.girls_enabled:
                pair_girls.add(("(candace/polly)", "candace", "polly"))
        if "nora" in self.girls_enabled:
            #if "lola" in self.girls_enabled:
            #    pair_girls.add(("(lola/nora)", "lola", "nora"))
            #if "candace" in self.girls_enabled:
            #    pair_girls.add(("(candace/nora)", "candace", "nora"))
            #if "sarah" in self.girls_enabled:
            #    pair_girls.add(("(nora/sarah)", "nora", "sarah"))
            if "ashley" in self.girls_enabled:
                pair_girls.add(("(ashley/nora)", "ashley", "nora"))
        if "brooke" in self.girls_enabled:
            #if "jessie" in self.girls_enabled:
            #    pair_girls.add(("(brooke/jessie)", "brooke", "jessie"))
            #if "sarah" in self.girls_enabled:
            #    pair_girls.add(("(brooke/sarah)", "brooke", "sarah"))
            if "ashley" in self.girls_enabled:
                pair_girls.add(("(ashley/brooke)", "ashley", "brooke"))
            if "polly" in self.girls_enabled:
                pair_girls.add(("(brooke/polly)", "brooke", "polly"))
        if "ashley" in self.girls_enabled:
            if "polly" in self.girls_enabled:
                pair_girls.add(("(ashley/polly)", "ashley", "polly"))
            #if "lillian" in self.girls_enabled:
            #    pair_girls.add(("(ashley/lillian)", "ashley", "lillian"))
            #if "nora" in self.girls_enabled:
            #    pair_girls.add(("(ashley/nora)", "ashley", "nora"))
            #if "brooke" in self.girls_enabled:
            #    pair_girls.add(("(ashley/brooke)", "ashley", "brooke"))
        if "abia" in self.girls_enabled:
            hi=""
            #if "lola" in self.girls_enabled:
            #    pair_girls.add(("(abia/lola)", "abia", "lola"))
            #if "jessie" in self.girls_enabled:
            #    pair_girls.add(("(abia/jessie)", "abia", "jessie"))
            #if "lillian" in self.girls_enabled:
            #    pair_girls.add(("(abia/lillian)", "abia", "lillian"))
            #if "candace" in self.girls_enabled:
            #    pair_girls.add(("(abia/candace)", "abia", "candace"))
        if "polly" in self.girls_enabled:
            hi=""
            #if "ashley" in self.girls_enabled:
            #    pair_girls.add(("(ashley/polly)", "ashley", "polly"),)
            #if "zoey" in self.girls_enabled:
            #    pair_girls.add(("(polly/zoey)", "polly", "zoey"))
            #if "candace" in self.girls_enabled:
            #    pair_girls.add(("(candace/polly)", "candace", "polly"))
            #if "brooke" in self.girls_enabled:
            #    pair_girls.add(("(brooke/polly)", "brooke", "polly"))

        for pair in pair_girls:
            self.pairs_enabled.add(pair[0])

        #get random number of pairs based on what's set in options
        temppairs = pair_girls.copy()
        tempgirl = []
        i=1
        while i<=numpairs:
            pair = temppairs.pop()
            self.startingpairs.append(f"Pair Unlock {pair[0]}")
            tempgirl.append(pair[1])
            tempgirl.append(pair[2])
            i+=1

        #add all the girls required for the starting pairs
        y = 0
        for g in tempgirl:
            xstr = f"Unlock Girl({g})"
            if not xstr in self.startinggirls:
                self.startinggirls.append(xstr)
                y += 1

        # add more starting girls if needed
        if y < numgirls:
            girllist = self.girls_enabled.copy()
            while y < numgirls:
                girl = girllist.pop()
                gstr = f"Unlock Girl({girl})"
                if not gstr in self.startinggirls:
                    self.startinggirls.append(gstr)
                    y += 1

                if len(girllist)<1:
                    break

        totallocations = 0
        totalitems = 0

        #get number of items that will in the itempool
        if not self.options.lovers_instead_wings.value: #fairy wings
            totalitems += len(self.pairs_enabled)
        if True: #tokenlvups
            totalitems += 32
        if True: #girl unlocks
            totalitems += len(self.girls_enabled) - len(self.startinggirls)
        if True: #pair unlocks
            totalitems += len(self.pairs_enabled) - len(self.startingpairs)
        if True: #gift unique
            totalitems += (len(self.girls_enabled) * 4)
        if True: #gift shoe
            totalitems += (len(self.girls_enabled) * 4)
        if not self.options.disable_baggage.value: #baggagage
            totalitems += (len(self.girls_enabled) * 3)
        if not self.options.disable_outfits.value:
            totalitems += (len(self.girls_enabled) * 4)

        #get the number of location that will be in the starting pool
        if True: #pair attracted/lovers
            totallocations += (len(self.pairs_enabled) * 2)
        if True: #unique gift
            totallocations += (len(self.girls_enabled) * 4)
        if True: #shoe gift
            totallocations += (len(self.girls_enabled) * 4)
        if self.options.enable_questions.value: #favroute question
            totallocations += (len(self.girls_enabled) * 20)
        if self.options.number_shop_items.value > 0: #shop locations
            totallocations += self.options.number_shop_items.value
        if not self.options.disable_outfits.value:
            totallocations += (len(self.girls_enabled) * 5)

        if totallocations != totalitems:
            if totallocations > totalitems:
                self.trashitems = totallocations-totalitems
                self.shopslots = self.options.number_shop_items.value
            else:
                self.shopslots = totalitems - (totallocations - self.options.number_shop_items.value)

        self.options.number_shop_items.value = self.shopslots

    def create_regions(self):
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        hub_region = Region("Hub Region", self.player, self.multiworld)
        menu_region.connect(hub_region, "menu-hub")

        boss_region = Region("Boss Region", self.player, self.multiworld)
        boss_region.add_locations({"boss_location": 69420505}, HP2Location)
        hub_region.connect(boss_region, "hub-boss")

        #print(f"total shop slots:{self.shopslots}")
        if self.shopslots > 0:
            shop_region = Region("Shop Region", self.player, self.multiworld)
            hub_region.connect(shop_region, "hub-shop")
            for i in range(self.shopslots):
                #self.location_name_to_id[f"shop_location: {i+1}"] = 69420506+i
                shop_region.add_locations({f"shop_location: {i+1}" : 69420506+i}, HP2Location)

        for pair in self.pairs_enabled:
            pairregion = Region(f"{pair} Region", self.player, self.multiworld)
            pairregion.add_locations({
                f"Pair Attracted {pair}":self.location_name_to_id[f"Pair Attracted {pair}"],
                f"Pair Lovers {pair}":self.location_name_to_id[f"Pair Lovers {pair}"]
            }, HP2Location)
            hub_region.connect(pairregion, f"hub-pair{pair}")

        for girl in self.girls_enabled:
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

            if not self.options.disable_outfits.value:
                girlregion.add_locations({
                    f"{girl} outfit 1": self.location_name_to_id[f"{girl} outfit 1"],
                    f"{girl} outfit 2": self.location_name_to_id[f"{girl} outfit 2"],
                    f"{girl} outfit 3": self.location_name_to_id[f"{girl} outfit 3"],
                    f"{girl} outfit 4": self.location_name_to_id[f"{girl} outfit 4"],
                    f"{girl} outfit 5": self.location_name_to_id[f"{girl} outfit 5"]}, HP2Location)


            hub_region.connect(girlregion, f"hub-{girl}")





    def create_item(self, name: str) -> HP2Item:
        if (name ==  "Victory"):
            return HP2Item(name, ItemClassification.progression, 69420346, self.player)
        if girl_unlock_table.get(name) is not None or pair_unlock_table.get(name) is not None or fairy_wings_table.get(name) is not None or gift_unique_table.get(name) is not None or gift_shoe_table.get(name) is not None:
            #print(f"{name}: is progression")
            return HP2Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        if tokekn_lvup_table.get(name) is not None :
            #print(f"{name}: is useful")
            return HP2Item(name, ItemClassification.useful, self.item_name_to_id[name], self.player)
        #print(f"{name}: is none")
        return HP2Item(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_items(self):
        for pair in self.pairs_enabled:
            if f"Pair Unlock {pair}" in self.startingpairs:
                self.multiworld.push_precollected(self.create_item(f"Pair Unlock {pair}"))
            else:
                self.multiworld.itempool.append(self.create_item(f"Pair Unlock {pair}"))

        for girl in self.girls_enabled:
            if f"Unlock Girl({girl})" in self.startinggirls:
                self.multiworld.push_precollected(self.create_item(f"Unlock Girl({girl})"))
            else:
                self.multiworld.itempool.append(self.create_item(f"Unlock Girl({girl})"))

            if not self.options.disable_baggage.value:
                self.multiworld.itempool.append(self.create_item(f"{girl} baggage 1"))
                self.multiworld.itempool.append(self.create_item(f"{girl} baggage 2"))
                self.multiworld.itempool.append(self.create_item(f"{girl} baggage 3"))

            self.multiworld.itempool.append(self.create_item(f"{girl} shoe item 1"))
            self.multiworld.itempool.append(self.create_item(f"{girl} shoe item 2"))
            self.multiworld.itempool.append(self.create_item(f"{girl} shoe item 3"))
            self.multiworld.itempool.append(self.create_item(f"{girl} shoe item 4"))

            self.multiworld.itempool.append(self.create_item(f"{girl} unique item 1"))
            self.multiworld.itempool.append(self.create_item(f"{girl} unique item 2"))
            self.multiworld.itempool.append(self.create_item(f"{girl} unique item 3"))
            self.multiworld.itempool.append(self.create_item(f"{girl} unique item 4"))

            if not self.options.disable_outfits.value:
                if girl == "polly":
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 1"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 2"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 3"))
                    #self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 4"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 5"))
                elif girl == "abia" or girl == "nora" or girl == "zoey":
                    #self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 1"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 2"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 3"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 4"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 5"))
                else:
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 1"))
                    #self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 2"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 3"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 4"))
                    self.multiworld.itempool.append(self.create_item(f"{girl} outfit item 5"))


        if not self.options.lovers_instead_wings.value:
            for pair in self.pairs_enabled:
                self.multiworld.itempool.append(self.create_item(f"Fairy Wings {pair}"))

        if True:
            for token in tokekn_lvup_table:
                self.multiworld.itempool.append(self.create_item(token))

        if self.trashitems > 0:
            for i in range(self.trashitems):
                self.multiworld.itempool.append(self.create_item("nothing"))



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

        girl_girlpair = {
            "lola": (("Pair Unlock (abia/lola)", "Unlock Girl(abia)"), ("Pair Unlock (lola/nora)", "Unlock Girl(nora)"), ("Pair Unlock (jessie/lola)", "Unlock Girl(jessie)"), ("Pair Unlock (lola/zoey)", "Unlock Girl(zoey)")),
            "jessie": (("Pair Unlock (jessie/lailani)", "Unlock Girl(lailani)"), ("Pair Unlock (brooke/jessie)", "Unlock Girl(brooke)"), ("Pair Unlock (jessie/lola)", "Unlock Girl(lola)"), ("Pair Unlock (abia/jessie)", "Unlock Girl(abia)")),
            "lillian": (("Pair Unlock (ashley/lillian)", "Unlock Girl(ashley)"), ("Pair Unlock (lillian/zoey)", "Unlock Girl(zoey)"), ("Pair Unlock (lailani/lillian)", "Unlock Girl(lailani)"), ("Pair Unlock (abia/lillian)", "Unlock Girl(abia)")),
            "zoey": (("Pair Unlock (lillian/zoey)", "Unlock Girl(lillian)"), ("Pair Unlock (lola/zoey)", "Unlock Girl(lola)"), ("Pair Unlock (sarah/zoey)", "Unlock Girl(sarah)"), ("Pair Unlock (polly/zoey)", "Unlock Girl(polly)")),
            "sarah": (("Pair Unlock (lailani/sarah)", "Unlock Girl(lailani)"), ("Pair Unlock (sarah/zoey)", "Unlock Girl(zoey)"), ("Pair Unlock (nora/sarah)", "Unlock Girl(nora)"), ("Pair Unlock (brooke/sarah)", "Unlock Girl(brooke)")),
            "lailani": (("Pair Unlock (lailani/sarah)", "Unlock Girl(sarah)"), ("Pair Unlock (jessie/lailani)", "Unlock Girl(jessie)"), ("Pair Unlock (lailani/lillian)", "Unlock Girl(lillian)"), ("Pair Unlock (candace/lailani)", "Unlock Girl(candace)")),
            "candace": (("Pair Unlock (candace/nora)", "Unlock Girl(nora)"), ("Pair Unlock (candace/lailani)", "Unlock Girl(lailani)"), ("Pair Unlock (abia/candace)", "Unlock Girl(abia)"), ("Pair Unlock (candace/polly)", "Unlock Girl(polly)")),
            "nora": (("Pair Unlock (lola/nora)", "Unlock Girl(lola)"), ("Pair Unlock (candace/nora)", "Unlock Girl(candace)"), ("Pair Unlock (nora/sarah)", "Unlock Girl(sarah)"), ("Pair Unlock (ashley/nora)", "Unlock Girl(ashley)")),
            "brooke": (("Pair Unlock (brooke/jessie)", "Unlock Girl(jessie)"), ("Pair Unlock (brooke/sarah)", "Unlock Girl(sarah)"), ("Pair Unlock (ashley/brooke)", "Unlock Girl(ashley)"), ("Pair Unlock (brooke/polly)", "Unlock Girl(polly)")),
            "ashley": (("Pair Unlock (ashley/polly)", "Unlock Girl(polly)"), ("Pair Unlock (ashley/lillian)", "Unlock Girl(lillian)"), ("Pair Unlock (ashley/nora)", "Unlock Girl(nora)"), ("Pair Unlock (ashley/brooke)", "Unlock Girl(brooke)")),
            "abia": (("Pair Unlock (abia/candace)", "Unlock Girl(candace)"), ("Pair Unlock (abia/lillian)", "Unlock Girl(lillian)"), ("Pair Unlock (abia/lola)", "Unlock Girl(lola)"), ("Pair Unlock (abia/jessie)", "Unlock Girl(jessie)")),
            "polly": (("Pair Unlock (brooke/polly)", "Unlock Girl(brooke)"), ("Pair Unlock (candace/polly)", "Unlock Girl(candace)"), ("Pair Unlock (polly/zoey)", "Unlock Girl(zoey)"), ("Pair Unlock (ashley/polly)", "Unlock Girl(ashley)"))
        }

        for girl in self.girls_enabled:
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


            #set_rule(self.multiworld.get_entrance(f"hub-{girl}", self.player), lambda state: (state.has(f"Unlock Girl({girl})", self.player) and ((state.has(girl_girlpair[girl][0][0], self.player) and state.has(girl_girlpair[girl][0][1], self.player)) or(state.has(girl_girlpair[girl][1][0], self.player) and state.has(girl_girlpair[girl][1][1], self.player)) or(state.has(girl_girlpair[girl][2][0], self.player) and state.has(girl_girlpair[girl][2][1], self.player)) or(state.has(girl_girlpair[girl][3][0], self.player) and state.has(girl_girlpair[girl][3][1], self.player)))))

            set_rule(self.multiworld.get_location(f"{girl} unique gift 1", self.player), lambda state: state.has(f"{girl} unique item 1", self.player))
            set_rule(self.multiworld.get_location(f"{girl} unique gift 2", self.player), lambda state: state.has(f"{girl} unique item 2", self.player))
            set_rule(self.multiworld.get_location(f"{girl} unique gift 3", self.player), lambda state: state.has(f"{girl} unique item 3", self.player))
            set_rule(self.multiworld.get_location(f"{girl} unique gift 4", self.player), lambda state: state.has(f"{girl} unique item 4", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 1", self.player), lambda state: state.has(f"{girl} shoe item 1", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 2", self.player), lambda state: state.has(f"{girl} shoe item 2", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 3", self.player), lambda state: state.has(f"{girl} shoe item 3", self.player))
            set_rule(self.multiworld.get_location(f"{girl} shoe gift 4", self.player), lambda state: state.has(f"{girl} shoe item 4", self.player))


        #set_rule(self.multiworld.get_entrance(f"hub-lola", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-lola", self.player), lambda state: (state.has_all(("Unlock Girl(lola)", "Unlock Girl(abia)", "Pair Unlock (abia/lola)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-lola", self.player), lambda state: (state.has_all(("Unlock Girl(lola)", "Unlock Girl(nora)", "Pair Unlock (lola/nora)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-lola", self.player), lambda state: (state.has_all(("Unlock Girl(lola)", "Unlock Girl(jessie)", "Pair Unlock (jessie/lola)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-lola", self.player), lambda state: (state.has_all(("Unlock Girl(lola)", "Unlock Girl(zoey)", "Pair Unlock (lola/zoey)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-jessie", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-jessie", self.player), lambda state: (state.has_all(("Unlock Girl(jessie)", "Unlock Girl(lailani)", "Pair Unlock (jessie/lailani)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-jessie", self.player), lambda state: (state.has_all(("Unlock Girl(jessie)", "Unlock Girl(brooke)", "Pair Unlock (brooke/jessie)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-jessie", self.player), lambda state: (state.has_all(("Unlock Girl(jessie)", "Unlock Girl(lola)", "Pair Unlock (jessie/lola)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-jessie", self.player), lambda state: (state.has_all(("Unlock Girl(jessie)", "Unlock Girl(abia)", "Pair Unlock (abia/jessie)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-lillian", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-lillian", self.player), lambda state: (state.has_all(("Unlock Girl(lillian)", "Unlock Girl(ashley)", "Pair Unlock (ashley/lillian)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-lillian", self.player), lambda state: (state.has_all(("Unlock Girl(lillian)", "Unlock Girl(zoey)", "Pair Unlock (lillian/zoey)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-lillian", self.player), lambda state: (state.has_all(("Unlock Girl(lillian)", "Unlock Girl(lailani)", "Pair Unlock (lailani/lillian)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-lillian", self.player), lambda state: (state.has_all(("Unlock Girl(lillian)", "Unlock Girl(abia)", "Pair Unlock (abia/lillian)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-zoey", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-zoey", self.player), lambda state: (state.has_all(("Unlock Girl(zoey)", "Unlock Girl(lillian)", "Pair Unlock (lillian/zoey)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-zoey", self.player), lambda state: (state.has_all(("Unlock Girl(zoey)", "Unlock Girl(lola)", "Pair Unlock (lola/zoey)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-zoey", self.player), lambda state: (state.has_all(("Unlock Girl(zoey)", "Unlock Girl(sarah)", "Pair Unlock (sarah/zoey)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-zoey", self.player), lambda state: (state.has_all(("Unlock Girl(zoey)", "Unlock Girl(polly)", "Pair Unlock (polly/zoey)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-sarah", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-sarah", self.player), lambda state: (state.has_all(("Unlock Girl(sarah)", "Unlock Girl(lailani)", "Pair Unlock (lailani/sarah)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-sarah", self.player), lambda state: (state.has_all(("Unlock Girl(sarah)", "Unlock Girl(zoey)", "Pair Unlock (sarah/zoey)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-sarah", self.player), lambda state: (state.has_all(("Unlock Girl(sarah)", "Unlock Girl(nora)", "Pair Unlock (nora/sarah)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-sarah", self.player), lambda state: (state.has_all(("Unlock Girl(sarah)", "Unlock Girl(brooke)", "Pair Unlock (brooke/sarah)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-lailani", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-lailani", self.player), lambda state: (state.has_all(("Unlock Girl(lailani)", "Unlock Girl(sarah)", "Pair Unlock (lailani/sarah)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-lailani", self.player), lambda state: (state.has_all(("Unlock Girl(lailani)", "Unlock Girl(jessie)", "Pair Unlock (jessie/lailani)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-lailani", self.player), lambda state: (state.has_all(("Unlock Girl(lailani)", "Unlock Girl(lillian)", "Pair Unlock (lailani/lillian)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-lailani", self.player), lambda state: (state.has_all(("Unlock Girl(lailani)", "Unlock Girl(candace)", "Pair Unlock (candace/lailani)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-candace", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-candace", self.player), lambda state: (state.has_all(("Unlock Girl(candace)", "Unlock Girl(nora)", "Pair Unlock (candace/nora)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-candace", self.player), lambda state: (state.has_all(("Unlock Girl(candace)", "Unlock Girl(lailani)", "Pair Unlock (candace/lailani)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-candace", self.player), lambda state: (state.has_all(("Unlock Girl(candace)", "Unlock Girl(abia)", "Pair Unlock (abia/candace)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-candace", self.player), lambda state: (state.has_all(("Unlock Girl(candace)", "Unlock Girl(polly)", "Pair Unlock (candace/polly)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-nora", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-nora", self.player), lambda state: (state.has_all(("Unlock Girl(nora)", "Unlock Girl(lola)", "Pair Unlock (lola/nora)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-nora", self.player), lambda state: (state.has_all(("Unlock Girl(nora)", "Unlock Girl(candace)", "Pair Unlock (candace/nora)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-nora", self.player), lambda state: (state.has_all(("Unlock Girl(nora)", "Unlock Girl(sarah)", "Pair Unlock (nora/sarah)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-nora", self.player), lambda state: (state.has_all(("Unlock Girl(nora)", "Unlock Girl(ashley)", "Pair Unlock (ashley/nora)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-brooke", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-brooke", self.player), lambda state: (state.has_all(("Unlock Girl(brooke)", "Unlock Girl(jessie)", "Pair Unlock (brooke/jessie)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-brooke", self.player), lambda state: (state.has_all(("Unlock Girl(brooke)", "Unlock Girl(sarah)", "Pair Unlock (brooke/sarah)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-brooke", self.player), lambda state: (state.has_all(("Unlock Girl(brooke)", "Unlock Girl(ashley)", "Pair Unlock (ashley/brooke)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-brooke", self.player), lambda state: (state.has_all(("Unlock Girl(brooke)", "Unlock Girl(polly)", "Pair Unlock (brooke/polly)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-ashley", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-ashley", self.player), lambda state: (state.has_all(("Unlock Girl(ashley)", "Unlock Girl(polly)", "Pair Unlock (ashley/polly)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-ashley", self.player), lambda state: (state.has_all(("Unlock Girl(ashley)", "Unlock Girl(lillian)", "Pair Unlock (ashley/lillian)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-ashley", self.player), lambda state: (state.has_all(("Unlock Girl(ashley)", "Unlock Girl(nora)", "Pair Unlock (ashley/nora)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-ashley", self.player), lambda state: (state.has_all(("Unlock Girl(ashley)", "Unlock Girl(brooke)", "Pair Unlock (ashley/brooke)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-abia", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-abia", self.player), lambda state: (state.has_all(("Unlock Girl(abia)", "Unlock Girl(lola)", "Pair Unlock (abia/lola)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-abia", self.player), lambda state: (state.has_all(("Unlock Girl(abia)", "Unlock Girl(jessie)", "Pair Unlock (abia/jessie)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-abia", self.player), lambda state: (state.has_all(("Unlock Girl(abia)", "Unlock Girl(lillian)", "Pair Unlock (abia/lillian)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-abia", self.player), lambda state: (state.has_all(("Unlock Girl(abia)", "Unlock Girl(candace)", "Pair Unlock (abia/candace)"), self.player)), "or")
        #set_rule(self.multiworld.get_entrance(f"hub-polly", self.player), lambda state: (
        set_rule(self.multiworld.get_entrance(f"hub-polly", self.player), lambda state: (state.has_all(("Unlock Girl(polly)", "Unlock Girl(ashley)", "Pair Unlock (ashley/polly)"), self.player)))
        add_rule(self.multiworld.get_entrance(f"hub-polly", self.player), lambda state: (state.has_all(("Unlock Girl(polly)", "Unlock Girl(zoey)", "Pair Unlock (polly/zoey)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-polly", self.player), lambda state: (state.has_all(("Unlock Girl(polly)", "Unlock Girl(candace)", "Pair Unlock (candace/polly)"), self.player)), "or")
        add_rule(self.multiworld.get_entrance(f"hub-polly", self.player), lambda state: (state.has_all(("Unlock Girl(polly)", "Unlock Girl(brooke)", "Pair Unlock (brooke/polly)"), self.player)), "or")


        if self.options.lovers_instead_wings.value:
            for pair in self.pairs_enabled:
                add_rule(self.multiworld.get_entrance("hub-boss", self.player), lambda state: state.has(f"Pair Unlock {pair}", self.player))
            for girl in self.girls_enabled:
                add_rule(self.multiworld.get_entrance("hub-boss", self.player), lambda state: state.has(f"Unlock Girl({girl})", self.player))
        else:
            for pair in self.pairs_enabled:
                add_rule(self.multiworld.get_entrance("hub-boss", self.player), lambda state: state.has(f"Fairy Wings {pair}", self.player))


        #visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def fill_slot_data(self) -> dict:
        returndict = {
            "number_blue_seed": self.options.number_blue_seed.value,
            "number_green_seed": self.options.number_green_seed.value,
            "number_orange_seed": self.options.number_orange_seed.value,
            "number_red_seed": self.options.number_red_seed.value,
            "number_shop_items": self.options.number_shop_items.value,
            "enable_questions": self.options.enable_questions.value,
            "disable_baggage": self.options.disable_baggage.value,
            "lovers_instead_wings": self.options.lovers_instead_wings.value,
            "affection_start": self.options.puzzle_goal_start.value,
            "affection_add": self.options.puzzle_goal_add.value,
            "boss_affection": self.options.puzzle_goal_boss.value,
            "start_moves": self.options.puzzle_moves.value
        }

        if "lola" in self.girls_enabled:
            returndict["lola"] = 0
        else:
            returndict["lola"] = 1

        if "jessie" in self.girls_enabled:
            returndict["jessie"] = 0
        else:
            returndict["jessie"] = 1

        if "lillian" in self.girls_enabled:
            returndict["lillian"] = 0
        else:
            returndict["lillian"] = 1

        if "zoey" in self.girls_enabled:
            returndict["zoey"] = 0
        else:
            returndict["zoey"] = 1

        if "sarah" in self.girls_enabled:
            returndict["sarah"] = 0
        else:
            returndict["sarah"] = 1

        if "lailani" in self.girls_enabled:
            returndict["lailani"] = 0
        else:
            returndict["lailani"] = 1

        if "candace" in self.girls_enabled:
            returndict["candace"] = 0
        else:
            returndict["candace"] = 1

        if "nora" in self.girls_enabled:
            returndict["nora"] = 0
        else:
            returndict["nora"] = 1

        if "brooke" in self.girls_enabled:
            returndict["brooke"] = 0
        else:
            returndict["brooke"] = 1

        if "ashley" in self.girls_enabled:
            returndict["ashley"] = 0
        else:
            returndict["ashley"] = 1

        if "abia" in self.girls_enabled:
            returndict["abia"] = 0
        else:
            returndict["abia"] = 1

        if "polly" in self.girls_enabled:
            returndict["polly"] = 0
        else:
            returndict["polly"] = 1

        return returndict