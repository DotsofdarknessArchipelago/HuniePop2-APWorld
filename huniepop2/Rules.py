from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, forbid_item

lola1 = ("Unlock Girl(lola)", "Unlock Girl(abia)", "Pair Unlock (abia/lola)")
lola2 = ("Unlock Girl(lola)", "Unlock Girl(nora)", "Pair Unlock (lola/nora)")
lola3 = ("Unlock Girl(lola)", "Unlock Girl(jessie)", "Pair Unlock (jessie/lola)")
lola4 = ("Unlock Girl(lola)", "Unlock Girl(zoey)", "Pair Unlock (lola/zoey)")
lola0 = ("Unlock Girl(lola)", "Unlock Girl(abia)", "Pair Unlock (abia/lola)", "Unlock Girl(nora)", "Pair Unlock (lola/nora)", "Unlock Girl(jessie)", "Pair Unlock (jessie/lola)", "Unlock Girl(zoey)", "Pair Unlock (lola/zoey)")

jessie1 = ("Unlock Girl(jessie)", "Unlock Girl(lailani)", "Pair Unlock (jessie/lailani)")
jessie2 = ("Unlock Girl(jessie)", "Unlock Girl(brooke)", "Pair Unlock (brooke/jessie)")
jessie3 = ("Unlock Girl(jessie)", "Unlock Girl(lola)", "Pair Unlock (jessie/lola)")
jessie4 = ("Unlock Girl(jessie)", "Unlock Girl(abia)", "Pair Unlock (abia/jessie)")
jessie0 = ("Unlock Girl(jessie)", "Unlock Girl(lailani)", "Pair Unlock (jessie/lailani)", "Unlock Girl(brooke)", "Pair Unlock (brooke/jessie)", "Unlock Girl(lola)", "Pair Unlock (jessie/lola)", "Unlock Girl(abia)", "Pair Unlock (abia/jessie)")

lillian1 = ("Unlock Girl(lillian)", "Unlock Girl(ashley)", "Pair Unlock (ashley/lillian)")
lillian2 = ("Unlock Girl(lillian)", "Unlock Girl(zoey)", "Pair Unlock (lillian/zoey)")
lillian3 = ("Unlock Girl(lillian)", "Unlock Girl(lailani)", "Pair Unlock (lailani/lillian)")
lillian4 = ("Unlock Girl(lillian)", "Unlock Girl(abia)", "Pair Unlock (abia/lillian)")
lillian0 = ("Unlock Girl(lillian)", "Unlock Girl(ashley)", "Pair Unlock (ashley/lillian)", "Unlock Girl(zoey)", "Pair Unlock (lillian/zoey)", "Unlock Girl(lailani)", "Pair Unlock (lailani/lillian)", "Unlock Girl(abia)", "Pair Unlock (abia/lillian)")

zoey1 = ("Unlock Girl(zoey)", "Unlock Girl(lillian)", "Pair Unlock (lillian/zoey)")
zoey2 = ("Unlock Girl(zoey)", "Unlock Girl(lola)", "Pair Unlock (lola/zoey)")
zoey3 = ("Unlock Girl(zoey)", "Unlock Girl(sarah)", "Pair Unlock (sarah/zoey)")
zoey4 = ("Unlock Girl(zoey)", "Unlock Girl(polly)", "Pair Unlock (polly/zoey)")
zoey0 = ("Unlock Girl(zoey)", "Unlock Girl(lillian)", "Pair Unlock (lillian/zoey)", "Unlock Girl(lola)", "Pair Unlock (lola/zoey)", "Unlock Girl(sarah)", "Pair Unlock (sarah/zoey)", "Unlock Girl(polly)", "Pair Unlock (polly/zoey)")

sarah1 = ("Unlock Girl(sarah)", "Unlock Girl(lailani)", "Pair Unlock (lailani/sarah)")
sarah2 = ("Unlock Girl(sarah)", "Unlock Girl(zoey)", "Pair Unlock (sarah/zoey)")
sarah3 = ("Unlock Girl(sarah)", "Unlock Girl(nora)", "Pair Unlock (nora/sarah)")
sarah4 = ("Unlock Girl(sarah)", "Unlock Girl(brooke)", "Pair Unlock (brooke/sarah)")
sarah0 = ("Unlock Girl(sarah)", "Unlock Girl(lailani)", "Pair Unlock (lailani/sarah)", "Unlock Girl(zoey)", "Pair Unlock (sarah/zoey)", "Unlock Girl(nora)", "Pair Unlock (nora/sarah)", "Unlock Girl(brooke)", "Pair Unlock (brooke/sarah)")

lailani1 = ("Unlock Girl(lailani)", "Unlock Girl(sarah)", "Pair Unlock (lailani/sarah)")
lailani2 = ("Unlock Girl(lailani)", "Unlock Girl(jessie)", "Pair Unlock (jessie/lailani)")
lailani3 = ("Unlock Girl(lailani)", "Unlock Girl(lillian)", "Pair Unlock (lailani/lillian)")
lailani4 = ("Unlock Girl(lailani)", "Unlock Girl(candace)", "Pair Unlock (candace/lailani)")
lailani0 = ("Unlock Girl(lailani)", "Unlock Girl(sarah)", "Pair Unlock (lailani/sarah)", "Unlock Girl(jessie)", "Pair Unlock (jessie/lailani)", "Unlock Girl(lillian)", "Pair Unlock (lailani/lillian)", "Unlock Girl(candace)", "Pair Unlock (candace/lailani)")

candace1 = ("Unlock Girl(candace)", "Unlock Girl(nora)", "Pair Unlock (candace/nora)")
candace2 = ("Unlock Girl(candace)", "Unlock Girl(lailani)", "Pair Unlock (candace/lailani)")
candace3 = ("Unlock Girl(candace)", "Unlock Girl(abia)", "Pair Unlock (abia/candace)")
candace4 = ("Unlock Girl(candace)", "Unlock Girl(polly)", "Pair Unlock (candace/polly)")
candace0 = ("Unlock Girl(candace)", "Unlock Girl(nora)", "Pair Unlock (candace/nora)", "Unlock Girl(lailani)", "Pair Unlock (candace/lailani)", "Unlock Girl(abia)", "Pair Unlock (abia/candace)", "Unlock Girl(polly)", "Pair Unlock (candace/polly)")

nora1 = ("Unlock Girl(nora)", "Unlock Girl(lola)", "Pair Unlock (lola/nora)")
nora2 = ("Unlock Girl(nora)", "Unlock Girl(candace)", "Pair Unlock (candace/nora)")
nora3 = ("Unlock Girl(nora)", "Unlock Girl(sarah)", "Pair Unlock (nora/sarah)")
nora4 = ("Unlock Girl(nora)", "Unlock Girl(ashley)", "Pair Unlock (ashley/nora)")
nora0 = ("Unlock Girl(nora)", "Unlock Girl(lola)", "Pair Unlock (lola/nora)", "Unlock Girl(candace)", "Pair Unlock (candace/nora)", "Unlock Girl(sarah)", "Pair Unlock (nora/sarah)", "Unlock Girl(ashley)", "Pair Unlock (ashley/nora)")

brooke1 = ("Unlock Girl(brooke)", "Unlock Girl(jessie)", "Pair Unlock (brooke/jessie)")
brooke2 = ("Unlock Girl(brooke)", "Unlock Girl(sarah)", "Pair Unlock (brooke/sarah)")
brooke3 = ("Unlock Girl(brooke)", "Unlock Girl(ashley)", "Pair Unlock (ashley/brooke)")
brooke4 = ("Unlock Girl(brooke)", "Unlock Girl(polly)", "Pair Unlock (brooke/polly)")
brooke0 = ("Unlock Girl(brooke)", "Unlock Girl(jessie)", "Pair Unlock (brooke/jessie)", "Unlock Girl(sarah)", "Pair Unlock (brooke/sarah)", "Unlock Girl(ashley)", "Pair Unlock (ashley/brooke)", "Unlock Girl(polly)", "Pair Unlock (brooke/polly)")

ashley1 = ("Unlock Girl(ashley)", "Unlock Girl(polly)", "Pair Unlock (ashley/polly)")
ashley2 = ("Unlock Girl(ashley)", "Unlock Girl(lillian)", "Pair Unlock (ashley/lillian)")
ashley3 = ("Unlock Girl(ashley)", "Unlock Girl(nora)", "Pair Unlock (ashley/nora)")
ashley4 = ("Unlock Girl(ashley)", "Unlock Girl(brooke)", "Pair Unlock (ashley/brooke)")
ashley0 = ("Unlock Girl(ashley)", "Unlock Girl(polly)", "Pair Unlock (ashley/polly)", "Unlock Girl(lillian)", "Pair Unlock (ashley/lillian)", "Unlock Girl(nora)", "Pair Unlock (ashley/nora)", "Unlock Girl(brooke)", "Pair Unlock (ashley/brooke)")

abia1 = ("Unlock Girl(abia)", "Unlock Girl(lola)", "Pair Unlock (abia/lola)")
abia2 = ("Unlock Girl(abia)", "Unlock Girl(jessie)", "Pair Unlock (abia/jessie)")
abia3 = ("Unlock Girl(abia)", "Unlock Girl(lillian)", "Pair Unlock (abia/lillian)")
abia4 = ("Unlock Girl(abia)", "Unlock Girl(candace)", "Pair Unlock (abia/candace)")
abia0 = ("Unlock Girl(abia)", "Unlock Girl(lola)", "Pair Unlock (abia/lola)", "Unlock Girl(jessie)", "Pair Unlock (abia/jessie)", "Unlock Girl(lillian)", "Pair Unlock (abia/lillian)", "Unlock Girl(candace)", "Pair Unlock (abia/candace)")

polly1 = ("Unlock Girl(polly)", "Unlock Girl(ashley)", "Pair Unlock (ashley/polly)")
polly2 = ("Unlock Girl(polly)", "Unlock Girl(zoey)", "Pair Unlock (polly/zoey)")
polly3 = ("Unlock Girl(polly)", "Unlock Girl(candace)", "Pair Unlock (candace/polly)")
polly4 = ("Unlock Girl(polly)", "Unlock Girl(brooke)", "Pair Unlock (brooke/polly)")
polly0 = ("Unlock Girl(polly)", "Unlock Girl(ashley)", "Pair Unlock (ashley/polly)", "Unlock Girl(zoey)", "Pair Unlock (polly/zoey)", "Unlock Girl(candace)", "Pair Unlock (candace/polly)", "Unlock Girl(brooke)", "Pair Unlock (brooke/polly)")


def set_rules(multiworld, player, girls, pairs, startpairs):

    print(startpairs)

    #LOLA
    if "lola" in girls:
        set_rule(multiworld.get_entrance("hub-lola1", player), lambda state: state.has_all(lola1, player))
        set_rule(multiworld.get_entrance("hub-lola2", player), lambda state: state.has_all(lola2, player))
        set_rule(multiworld.get_entrance("hub-lola3", player), lambda state: state.has_all(lola3, player))
        set_rule(multiworld.get_entrance("hub-lola4", player), lambda state: state.has_all(lola4, player))
        set_rule(multiworld.get_location("lola unique gift 1", player), lambda state: state.has("lola unique item 1", player))
        set_rule(multiworld.get_location("lola unique gift 2", player), lambda state: state.has("lola unique item 2", player))
        set_rule(multiworld.get_location("lola unique gift 3", player), lambda state: state.has("lola unique item 3", player))
        set_rule(multiworld.get_location("lola unique gift 4", player), lambda state: state.has("lola unique item 4", player))
        set_rule(multiworld.get_location("lola shoe gift 1", player), lambda state: state.has("lola shoe item 1", player))
        set_rule(multiworld.get_location("lola shoe gift 2", player), lambda state: state.has("lola shoe item 2", player))
        set_rule(multiworld.get_location("lola shoe gift 3", player), lambda state: state.has("lola shoe item 3", player))
        set_rule(multiworld.get_location("lola shoe gift 4", player), lambda state: state.has("lola shoe item 4", player))
        for lock in lola0:
            forbid_item(multiworld.get_location("lola unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("lola unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("lola unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("lola unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("lola shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("lola shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("lola shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("lola shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("lola favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("lola outfit 10", player), lock, player)

    #JESSIE
    if "jessie" in girls:
        set_rule(multiworld.get_entrance("hub-jessie1", player), lambda state: state.has_all(jessie1, player))
        set_rule(multiworld.get_entrance("hub-jessie2", player), lambda state: state.has_all(jessie2, player))
        set_rule(multiworld.get_entrance("hub-jessie3", player), lambda state: state.has_all(jessie3, player))
        set_rule(multiworld.get_entrance("hub-jessie4", player), lambda state: state.has_all(jessie4, player))
        set_rule(multiworld.get_location("jessie unique gift 1", player), lambda state: state.has("jessie unique item 1", player))
        set_rule(multiworld.get_location("jessie unique gift 2", player), lambda state: state.has("jessie unique item 2", player))
        set_rule(multiworld.get_location("jessie unique gift 3", player), lambda state: state.has("jessie unique item 3", player))
        set_rule(multiworld.get_location("jessie unique gift 4", player), lambda state: state.has("jessie unique item 4", player))
        set_rule(multiworld.get_location("jessie shoe gift 1", player), lambda state: state.has("jessie shoe item 1", player))
        set_rule(multiworld.get_location("jessie shoe gift 2", player), lambda state: state.has("jessie shoe item 2", player))
        set_rule(multiworld.get_location("jessie shoe gift 3", player), lambda state: state.has("jessie shoe item 3", player))
        set_rule(multiworld.get_location("jessie shoe gift 4", player), lambda state: state.has("jessie shoe item 4", player))
        for lock in jessie0:
            forbid_item(multiworld.get_location("jessie unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("jessie unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("jessie unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("jessie unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("jessie shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("jessie shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("jessie shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("jessie shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("jessie favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("jessie outfit 10", player), lock, player)


    if "lillian" in girls:
        set_rule(multiworld.get_entrance("hub-lillian1", player), lambda state: state.has_all(lillian1, player))
        set_rule(multiworld.get_entrance("hub-lillian2", player), lambda state: state.has_all(lillian2, player))
        set_rule(multiworld.get_entrance("hub-lillian3", player), lambda state: state.has_all(lillian3, player))
        set_rule(multiworld.get_entrance("hub-lillian4", player), lambda state: state.has_all(lillian4, player))
        set_rule(multiworld.get_location("lillian unique gift 1", player), lambda state: state.has("lillian unique item 1", player))
        set_rule(multiworld.get_location("lillian unique gift 2", player), lambda state: state.has("lillian unique item 2", player))
        set_rule(multiworld.get_location("lillian unique gift 3", player), lambda state: state.has("lillian unique item 3", player))
        set_rule(multiworld.get_location("lillian unique gift 4", player), lambda state: state.has("lillian unique item 4", player))
        set_rule(multiworld.get_location("lillian shoe gift 1", player), lambda state: state.has("lillian shoe item 1", player))
        set_rule(multiworld.get_location("lillian shoe gift 2", player), lambda state: state.has("lillian shoe item 2", player))
        set_rule(multiworld.get_location("lillian shoe gift 3", player), lambda state: state.has("lillian shoe item 3", player))
        set_rule(multiworld.get_location("lillian shoe gift 4", player), lambda state: state.has("lillian shoe item 4", player))
        for lock in lillian0:
            forbid_item(multiworld.get_location("lillian unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("lillian unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("lillian unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("lillian unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("lillian shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("lillian shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("lillian shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("lillian shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("lillian favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("lillian outfit 10", player), lock, player)


    if "zoey" in girls:
        set_rule(multiworld.get_entrance("hub-zoey1", player), lambda state: state.has_all(zoey1, player))
        set_rule(multiworld.get_entrance("hub-zoey2", player), lambda state: state.has_all(zoey2, player))
        set_rule(multiworld.get_entrance("hub-zoey3", player), lambda state: state.has_all(zoey3, player))
        set_rule(multiworld.get_entrance("hub-zoey4", player), lambda state: state.has_all(zoey4, player))
        set_rule(multiworld.get_location("zoey unique gift 1", player), lambda state: state.has("zoey unique item 1", player))
        set_rule(multiworld.get_location("zoey unique gift 2", player), lambda state: state.has("zoey unique item 2", player))
        set_rule(multiworld.get_location("zoey unique gift 3", player), lambda state: state.has("zoey unique item 3", player))
        set_rule(multiworld.get_location("zoey unique gift 4", player), lambda state: state.has("zoey unique item 4", player))
        set_rule(multiworld.get_location("zoey shoe gift 1", player), lambda state: state.has("zoey shoe item 1", player))
        set_rule(multiworld.get_location("zoey shoe gift 2", player), lambda state: state.has("zoey shoe item 2", player))
        set_rule(multiworld.get_location("zoey shoe gift 3", player), lambda state: state.has("zoey shoe item 3", player))
        set_rule(multiworld.get_location("zoey shoe gift 4", player), lambda state: state.has("zoey shoe item 4", player))
        for lock in zoey0:
            forbid_item(multiworld.get_location("zoey unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("zoey unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("zoey unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("zoey unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("zoey shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("zoey shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("zoey shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("zoey shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("zoey favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("zoey outfit 10", player), lock, player)


    if "sarah" in girls:
        set_rule(multiworld.get_entrance("hub-sarah1", player), lambda state: state.has_all(sarah1, player))
        set_rule(multiworld.get_entrance("hub-sarah2", player), lambda state: state.has_all(sarah2, player))
        set_rule(multiworld.get_entrance("hub-sarah3", player), lambda state: state.has_all(sarah3, player))
        set_rule(multiworld.get_entrance("hub-sarah4", player), lambda state: state.has_all(sarah4, player))
        set_rule(multiworld.get_location("sarah unique gift 1", player), lambda state: state.has("sarah unique item 1", player))
        set_rule(multiworld.get_location("sarah unique gift 2", player), lambda state: state.has("sarah unique item 2", player))
        set_rule(multiworld.get_location("sarah unique gift 3", player), lambda state: state.has("sarah unique item 3", player))
        set_rule(multiworld.get_location("sarah unique gift 4", player), lambda state: state.has("sarah unique item 4", player))
        set_rule(multiworld.get_location("sarah shoe gift 1", player), lambda state: state.has("sarah shoe item 1", player))
        set_rule(multiworld.get_location("sarah shoe gift 2", player), lambda state: state.has("sarah shoe item 2", player))
        set_rule(multiworld.get_location("sarah shoe gift 3", player), lambda state: state.has("sarah shoe item 3", player))
        set_rule(multiworld.get_location("sarah shoe gift 4", player), lambda state: state.has("sarah shoe item 4", player))
        for lock in sarah0:
            forbid_item(multiworld.get_location("sarah unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("sarah unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("sarah unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("sarah unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("sarah shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("sarah shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("sarah shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("sarah shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("sarah favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("sarah outfit 10", player), lock, player)


    if "lailani" in girls:
        set_rule(multiworld.get_entrance("hub-lailani1", player), lambda state: state.has_all(lailani1, player))
        set_rule(multiworld.get_entrance("hub-lailani2", player), lambda state: state.has_all(lailani2, player))
        set_rule(multiworld.get_entrance("hub-lailani3", player), lambda state: state.has_all(lailani3, player))
        set_rule(multiworld.get_entrance("hub-lailani4", player), lambda state: state.has_all(lailani4, player))
        set_rule(multiworld.get_location("lailani unique gift 1", player), lambda state: state.has("lailani unique item 1", player))
        set_rule(multiworld.get_location("lailani unique gift 2", player), lambda state: state.has("lailani unique item 2", player))
        set_rule(multiworld.get_location("lailani unique gift 3", player), lambda state: state.has("lailani unique item 3", player))
        set_rule(multiworld.get_location("lailani unique gift 4", player), lambda state: state.has("lailani unique item 4", player))
        set_rule(multiworld.get_location("lailani shoe gift 1", player), lambda state: state.has("lailani shoe item 1", player))
        set_rule(multiworld.get_location("lailani shoe gift 2", player), lambda state: state.has("lailani shoe item 2", player))
        set_rule(multiworld.get_location("lailani shoe gift 3", player), lambda state: state.has("lailani shoe item 3", player))
        set_rule(multiworld.get_location("lailani shoe gift 4", player), lambda state: state.has("lailani shoe item 4", player))
        for lock in lailani0:
            forbid_item(multiworld.get_location("lailani unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("lailani unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("lailani unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("lailani unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("lailani shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("lailani shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("lailani shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("lailani shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("lailani favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("lailani outfit 10", player), lock, player)


    if "candace" in girls:
        set_rule(multiworld.get_entrance("hub-candace1", player), lambda state: state.has_all(candace1, player))
        set_rule(multiworld.get_entrance("hub-candace2", player), lambda state: state.has_all(candace2, player))
        set_rule(multiworld.get_entrance("hub-candace3", player), lambda state: state.has_all(candace3, player))
        set_rule(multiworld.get_entrance("hub-candace4", player), lambda state: state.has_all(candace4, player))
        set_rule(multiworld.get_location("candace unique gift 1", player), lambda state: state.has("candace unique item 1", player))
        set_rule(multiworld.get_location("candace unique gift 2", player), lambda state: state.has("candace unique item 2", player))
        set_rule(multiworld.get_location("candace unique gift 3", player), lambda state: state.has("candace unique item 3", player))
        set_rule(multiworld.get_location("candace unique gift 4", player), lambda state: state.has("candace unique item 4", player))
        set_rule(multiworld.get_location("candace shoe gift 1", player), lambda state: state.has("candace shoe item 1", player))
        set_rule(multiworld.get_location("candace shoe gift 2", player), lambda state: state.has("candace shoe item 2", player))
        set_rule(multiworld.get_location("candace shoe gift 3", player), lambda state: state.has("candace shoe item 3", player))
        set_rule(multiworld.get_location("candace shoe gift 4", player), lambda state: state.has("candace shoe item 4", player))
        for lock in candace0:
            forbid_item(multiworld.get_location("candace unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("candace unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("candace unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("candace unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("candace shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("candace shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("candace shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("candace shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("candace favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("candace outfit 10", player), lock, player)


    if "nora" in girls:
        set_rule(multiworld.get_entrance("hub-nora1", player), lambda state: state.has_all(nora1, player))
        set_rule(multiworld.get_entrance("hub-nora2", player), lambda state: state.has_all(nora2, player))
        set_rule(multiworld.get_entrance("hub-nora3", player), lambda state: state.has_all(nora3, player))
        set_rule(multiworld.get_entrance("hub-nora4", player), lambda state: state.has_all(nora4, player))
        set_rule(multiworld.get_location("nora unique gift 1", player), lambda state: state.has("nora unique item 1", player))
        set_rule(multiworld.get_location("nora unique gift 2", player), lambda state: state.has("nora unique item 2", player))
        set_rule(multiworld.get_location("nora unique gift 3", player), lambda state: state.has("nora unique item 3", player))
        set_rule(multiworld.get_location("nora unique gift 4", player), lambda state: state.has("nora unique item 4", player))
        set_rule(multiworld.get_location("nora shoe gift 1", player), lambda state: state.has("nora shoe item 1", player))
        set_rule(multiworld.get_location("nora shoe gift 2", player), lambda state: state.has("nora shoe item 2", player))
        set_rule(multiworld.get_location("nora shoe gift 3", player), lambda state: state.has("nora shoe item 3", player))
        set_rule(multiworld.get_location("nora shoe gift 4", player), lambda state: state.has("nora shoe item 4", player))
        for lock in nora0:
            forbid_item(multiworld.get_location("nora unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("nora unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("nora unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("nora unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("nora shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("nora shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("nora shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("nora shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("nora favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("nora outfit 10", player), lock, player)


    if "brooke" in girls:
        set_rule(multiworld.get_entrance("hub-brooke1", player), lambda state: state.has_all(brooke1, player))
        set_rule(multiworld.get_entrance("hub-brooke2", player), lambda state: state.has_all(brooke2, player))
        set_rule(multiworld.get_entrance("hub-brooke3", player), lambda state: state.has_all(brooke3, player))
        set_rule(multiworld.get_entrance("hub-brooke4", player), lambda state: state.has_all(brooke4, player))
        set_rule(multiworld.get_location("brooke unique gift 1", player), lambda state: state.has("brooke unique item 1", player))
        set_rule(multiworld.get_location("brooke unique gift 2", player), lambda state: state.has("brooke unique item 2", player))
        set_rule(multiworld.get_location("brooke unique gift 3", player), lambda state: state.has("brooke unique item 3", player))
        set_rule(multiworld.get_location("brooke unique gift 4", player), lambda state: state.has("brooke unique item 4", player))
        set_rule(multiworld.get_location("brooke shoe gift 1", player), lambda state: state.has("brooke shoe item 1", player))
        set_rule(multiworld.get_location("brooke shoe gift 2", player), lambda state: state.has("brooke shoe item 2", player))
        set_rule(multiworld.get_location("brooke shoe gift 3", player), lambda state: state.has("brooke shoe item 3", player))
        set_rule(multiworld.get_location("brooke shoe gift 4", player), lambda state: state.has("brooke shoe item 4", player))
        for lock in brooke0:
            forbid_item(multiworld.get_location("brooke unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("brooke unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("brooke unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("brooke unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("brooke shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("brooke shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("brooke shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("brooke shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("brooke favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("brooke outfit 10", player), lock, player)


    if "ashley" in girls:
        set_rule(multiworld.get_entrance("hub-ashley1", player), lambda state: state.has_all(ashley1, player))
        set_rule(multiworld.get_entrance("hub-ashley2", player), lambda state: state.has_all(ashley2, player))
        set_rule(multiworld.get_entrance("hub-ashley3", player), lambda state: state.has_all(ashley3, player))
        set_rule(multiworld.get_entrance("hub-ashley4", player), lambda state: state.has_all(ashley4, player))
        set_rule(multiworld.get_location("ashley unique gift 1", player), lambda state: state.has("ashley unique item 1", player))
        set_rule(multiworld.get_location("ashley unique gift 2", player), lambda state: state.has("ashley unique item 2", player))
        set_rule(multiworld.get_location("ashley unique gift 3", player), lambda state: state.has("ashley unique item 3", player))
        set_rule(multiworld.get_location("ashley unique gift 4", player), lambda state: state.has("ashley unique item 4", player))
        set_rule(multiworld.get_location("ashley shoe gift 1", player), lambda state: state.has("ashley shoe item 1", player))
        set_rule(multiworld.get_location("ashley shoe gift 2", player), lambda state: state.has("ashley shoe item 2", player))
        set_rule(multiworld.get_location("ashley shoe gift 3", player), lambda state: state.has("ashley shoe item 3", player))
        set_rule(multiworld.get_location("ashley shoe gift 4", player), lambda state: state.has("ashley shoe item 4", player))
        for lock in ashley0:
            forbid_item(multiworld.get_location("ashley unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("ashley unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("ashley unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("ashley unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("ashley shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("ashley shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("ashley shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("ashley shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("ashley favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("ashley outfit 10", player), lock, player)


    if "abia" in girls:
        set_rule(multiworld.get_entrance("hub-abia1", player), lambda state: state.has_all(abia1, player))
        set_rule(multiworld.get_entrance("hub-abia2", player), lambda state: state.has_all(abia2, player))
        set_rule(multiworld.get_entrance("hub-abia3", player), lambda state: state.has_all(abia3, player))
        set_rule(multiworld.get_entrance("hub-abia4", player), lambda state: state.has_all(abia4, player))
        set_rule(multiworld.get_location("abia unique gift 1", player), lambda state: state.has("abia unique item 1", player))
        set_rule(multiworld.get_location("abia unique gift 2", player), lambda state: state.has("abia unique item 2", player))
        set_rule(multiworld.get_location("abia unique gift 3", player), lambda state: state.has("abia unique item 3", player))
        set_rule(multiworld.get_location("abia unique gift 4", player), lambda state: state.has("abia unique item 4", player))
        set_rule(multiworld.get_location("abia shoe gift 1", player), lambda state: state.has("abia shoe item 1", player))
        set_rule(multiworld.get_location("abia shoe gift 2", player), lambda state: state.has("abia shoe item 2", player))
        set_rule(multiworld.get_location("abia shoe gift 3", player), lambda state: state.has("abia shoe item 3", player))
        set_rule(multiworld.get_location("abia shoe gift 4", player), lambda state: state.has("abia shoe item 4", player))
        for lock in abia0:
            forbid_item(multiworld.get_location("abia unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("abia unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("abia unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("abia unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("abia shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("abia shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("abia shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("abia shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("abia favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("abia outfit 10", player), lock, player)


    if "polly" in girls:
        set_rule(multiworld.get_entrance("hub-polly1", player), lambda state: state.has_all(polly1, player))
        set_rule(multiworld.get_entrance("hub-polly2", player), lambda state: state.has_all(polly2, player))
        set_rule(multiworld.get_entrance("hub-polly3", player), lambda state: state.has_all(polly3, player))
        set_rule(multiworld.get_entrance("hub-polly4", player), lambda state: state.has_all(polly4, player))
        set_rule(multiworld.get_location("polly unique gift 1", player), lambda state: state.has("polly unique item 1", player))
        set_rule(multiworld.get_location("polly unique gift 2", player), lambda state: state.has("polly unique item 2", player))
        set_rule(multiworld.get_location("polly unique gift 3", player), lambda state: state.has("polly unique item 3", player))
        set_rule(multiworld.get_location("polly unique gift 4", player), lambda state: state.has("polly unique item 4", player))
        set_rule(multiworld.get_location("polly shoe gift 1", player), lambda state: state.has("polly shoe item 1", player))
        set_rule(multiworld.get_location("polly shoe gift 2", player), lambda state: state.has("polly shoe item 2", player))
        set_rule(multiworld.get_location("polly shoe gift 3", player), lambda state: state.has("polly shoe item 3", player))
        set_rule(multiworld.get_location("polly shoe gift 4", player), lambda state: state.has("polly shoe item 4", player))
        for lock in polly0:
            forbid_item(multiworld.get_location("polly unique gift 1", player), lock, player)
            forbid_item(multiworld.get_location("polly unique gift 2", player), lock, player)
            forbid_item(multiworld.get_location("polly unique gift 3", player), lock, player)
            forbid_item(multiworld.get_location("polly unique gift 4", player), lock, player)
            forbid_item(multiworld.get_location("polly shoe gift 1", player), lock, player)
            forbid_item(multiworld.get_location("polly shoe gift 2", player), lock, player)
            forbid_item(multiworld.get_location("polly shoe gift 3", player), lock, player)
            forbid_item(multiworld.get_location("polly shoe gift 4", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite drink", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Ice Cream Flavor", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Music Genre", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Movie Genre", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Online Activity", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Phone App", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Type Of Exercise", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Outdoor Activity", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Theme Park Ride", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Friday Night", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Sunday Morning", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Weather", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Holiday", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Pet", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite School Subject", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Place to shop", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Trait In Partner", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Own Body Part", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Sex Position", player), lock, player)
            forbid_item(multiworld.get_location("polly favourite Porn Category", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 1", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 2", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 3", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 4", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 5", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 6", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 7", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 8", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 9", player), lock, player)
            forbid_item(multiworld.get_location("polly outfit 10", player), lock, player)


    if "(abia/lola)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(abia/lola)", player), lambda state: state.has_all(lola1, player))
        forbid_item(multiworld.get_location("Pair Attracted (abia/lola)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/lola)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/lola)", player), "Pair Unlock (abia/lola)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/lola)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/lola)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/lola)", player), "Pair Unlock (abia/lola)", player)

    if "(lola/nora)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(lola/nora)", player), lambda state: state.has_all(lola2, player))
        forbid_item(multiworld.get_location("Pair Attracted (lola/nora)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lola/nora)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lola/nora)", player), "Pair Unlock (lola/nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lola/nora)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lola/nora)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lola/nora)", player), "Pair Unlock (lola/nora)", player)

    if "(candace/nora)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(candace/nora)", player), lambda state: state.has_all(candace1, player))
        forbid_item(multiworld.get_location("Pair Attracted (candace/nora)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Attracted (candace/nora)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Attracted (candace/nora)", player), "Pair Unlock (candace/nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/nora)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/nora)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/nora)", player), "Pair Unlock (candace/nora)", player)

    if "(ashley/polly)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(ashley/polly)", player), lambda state: state.has_all(ashley1, player))
        forbid_item(multiworld.get_location("Pair Attracted (ashley/polly)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/polly)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/polly)", player), "Pair Unlock (ashley/polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/polly)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/polly)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/polly)", player), "Pair Unlock (ashley/polly)", player)

    if "(ashley/lillian)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(ashley/lillian)", player), lambda state: state.has_all(lillian1, player))
        forbid_item(multiworld.get_location("Pair Attracted (ashley/lillian)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/lillian)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/lillian)", player), "Pair Unlock (ashley/lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/lillian)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/lillian)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/lillian)", player), "Pair Unlock (ashley/lillian)", player)

    if "(lillian/zoey)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(lillian/zoey)", player), lambda state: state.has_all(lillian2, player))
        forbid_item(multiworld.get_location("Pair Attracted (lillian/zoey)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lillian/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lillian/zoey)", player), "Pair Unlock (lillian/zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lillian/zoey)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lillian/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lillian/zoey)", player), "Pair Unlock (lillian/zoey)", player)

    if "(lailani/sarah)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(lailani/sarah)", player), lambda state: state.has_all(sarah1, player))
        forbid_item(multiworld.get_location("Pair Attracted (lailani/sarah)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lailani/sarah)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lailani/sarah)", player), "Pair Unlock (lailani/sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lailani/sarah)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lailani/sarah)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lailani/sarah)", player), "Pair Unlock (lailani/sarah)", player)

    if "(jessie/lailani)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(jessie/lailani)", player), lambda state: state.has_all(jessie1, player))
        forbid_item(multiworld.get_location("Pair Attracted (jessie/lailani)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Attracted (jessie/lailani)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Attracted (jessie/lailani)", player), "Pair Unlock (jessie/lailani)", player)
        forbid_item(multiworld.get_location("Pair Lovers (jessie/lailani)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Lovers (jessie/lailani)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Lovers (jessie/lailani)", player), "Pair Unlock (jessie/lailani)", player)

    if "(brooke/jessie)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(brooke/jessie)", player), lambda state: state.has_all(jessie2, player))
        forbid_item(multiworld.get_location("Pair Attracted (brooke/jessie)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Attracted (brooke/jessie)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Attracted (brooke/jessie)", player), "Pair Unlock (brooke/jessie)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/jessie)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/jessie)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/jessie)", player), "Pair Unlock (brooke/jessie)", player)

    if "(jessie/lola)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(jessie/lola)", player), lambda state: state.has_all(lola3, player))
        forbid_item(multiworld.get_location("Pair Attracted (jessie/lola)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Attracted (jessie/lola)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Attracted (jessie/lola)", player), "Pair Unlock (jessie/lola)", player)
        forbid_item(multiworld.get_location("Pair Lovers (jessie/lola)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Lovers (jessie/lola)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Lovers (jessie/lola)", player), "Pair Unlock (jessie/lola)", player)

    if "(lola/zoey)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(lola/zoey)", player), lambda state: state.has_all(lola4, player))
        forbid_item(multiworld.get_location("Pair Attracted (lola/zoey)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lola/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lola/zoey)", player), "Pair Unlock (lola/zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lola/zoey)", player), "Unlock Girl(lola)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lola/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lola/zoey)", player), "Pair Unlock (lola/zoey)", player)

    if "(abia/jessie)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(abia/jessie)", player), lambda state: state.has_all(jessie4, player))
        forbid_item(multiworld.get_location("Pair Attracted (abia/jessie)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/jessie)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/jessie)", player), "Pair Unlock (abia/jessie)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/jessie)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/jessie)", player), "Unlock Girl(jessie)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/jessie)", player), "Pair Unlock (abia/jessie)", player)

    if "(lailani/lillian)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(lailani/lillian)", player), lambda state: state.has_all(lillian3, player))
        forbid_item(multiworld.get_location("Pair Attracted (lailani/lillian)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lailani/lillian)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Attracted (lailani/lillian)", player), "Pair Unlock (lailani/lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lailani/lillian)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lailani/lillian)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (lailani/lillian)", player), "Pair Unlock (lailani/lillian)", player)

    if "(abia/lillian)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(abia/lillian)", player), lambda state: state.has_all(lillian4, player))
        forbid_item(multiworld.get_location("Pair Attracted (abia/lillian)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/lillian)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/lillian)", player), "Pair Unlock (abia/lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/lillian)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/lillian)", player), "Unlock Girl(lillian)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/lillian)", player), "Pair Unlock (abia/lillian)", player)

    if "(sarah/zoey)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(sarah/zoey)", player), lambda state: state.has_all(zoey3, player))
        forbid_item(multiworld.get_location("Pair Attracted (sarah/zoey)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Attracted (sarah/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Attracted (sarah/zoey)", player), "Pair Unlock (sarah/zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (sarah/zoey)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (sarah/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (sarah/zoey)", player), "Pair Unlock (sarah/zoey)", player)

    if "(polly/zoey)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(polly/zoey)", player), lambda state: state.has_all(zoey4, player))
        forbid_item(multiworld.get_location("Pair Attracted (polly/zoey)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Attracted (polly/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Attracted (polly/zoey)", player), "Pair Unlock (polly/zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (polly/zoey)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (polly/zoey)", player), "Unlock Girl(zoey)", player)
        forbid_item(multiworld.get_location("Pair Lovers (polly/zoey)", player), "Pair Unlock (polly/zoey)", player)

    if "(nora/sarah)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(nora/sarah)", player), lambda state: state.has_all(sarah3, player))
        forbid_item(multiworld.get_location("Pair Attracted (nora/sarah)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Attracted (nora/sarah)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Attracted (nora/sarah)", player), "Pair Unlock (nora/sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (nora/sarah)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (nora/sarah)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (nora/sarah)", player), "Pair Unlock (nora/sarah)", player)

    if "(brooke/sarah)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(brooke/sarah)", player), lambda state: state.has_all(sarah4, player))
        forbid_item(multiworld.get_location("Pair Attracted (brooke/sarah)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Attracted (brooke/sarah)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Attracted (brooke/sarah)", player), "Pair Unlock (brooke/sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/sarah)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/sarah)", player), "Unlock Girl(sarah)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/sarah)", player), "Pair Unlock (brooke/sarah)", player)

    if "(candace/lailani)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(candace/lailani)", player), lambda state: state.has_all(lailani4, player))
        forbid_item(multiworld.get_location("Pair Attracted (candace/lailani)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Attracted (candace/lailani)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Attracted (candace/lailani)", player), "Pair Unlock (candace/lailani)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/lailani)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/lailani)", player), "Unlock Girl(lailani)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/lailani)", player), "Pair Unlock (candace/lailani)", player)

    if "(abia/candace)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(abia/candace)", player), lambda state: state.has_all(candace3, player))
        forbid_item(multiworld.get_location("Pair Attracted (abia/candace)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/candace)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Attracted (abia/candace)", player), "Pair Unlock (abia/candace)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/candace)", player), "Unlock Girl(abia)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/candace)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Lovers (abia/candace)", player), "Pair Unlock (abia/candace)", player)

    if "(candace/polly)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(candace/polly)", player), lambda state: state.has_all(candace4, player))
        forbid_item(multiworld.get_location("Pair Attracted (candace/polly)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Attracted (candace/polly)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Attracted (candace/polly)", player), "Pair Unlock (candace/polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/polly)", player), "Unlock Girl(candace)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/polly)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (candace/polly)", player), "Pair Unlock (candace/polly)", player)

    if "(ashley/nora)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(ashley/nora)", player), lambda state: state.has_all(nora4, player))
        forbid_item(multiworld.get_location("Pair Attracted (ashley/nora)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/nora)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/nora)", player), "Pair Unlock (ashley/nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/nora)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/nora)", player), "Unlock Girl(nora)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/nora)", player), "Pair Unlock (ashley/nora)", player)

    if "(ashley/brooke)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(ashley/brooke)", player), lambda state: state.has_all(brooke3, player))
        forbid_item(multiworld.get_location("Pair Attracted (ashley/brooke)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/brooke)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Attracted (ashley/brooke)", player), "Pair Unlock (ashley/brooke)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/brooke)", player), "Unlock Girl(ashley)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/brooke)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Lovers (ashley/brooke)", player), "Pair Unlock (ashley/brooke)", player)

    if "(brooke/polly)" in pairs:
        set_rule(multiworld.get_entrance(f"hub-pair(brooke/polly)", player), lambda state: state.has_all(brooke4, player))
        forbid_item(multiworld.get_location("Pair Attracted (brooke/polly)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Attracted (brooke/polly)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Attracted (brooke/polly)", player), "Pair Unlock (brooke/polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/polly)", player), "Unlock Girl(brooke)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/polly)", player), "Unlock Girl(polly)", player)
        forbid_item(multiworld.get_location("Pair Lovers (brooke/polly)", player), "Pair Unlock (brooke/polly)", player)


def girlaccess2(state: CollectionState, player, girl) -> bool:
    if girl == "lola":
        if not state.has("Unlock Girl(lola)", player):
            return False
        else:
            if state.has("Unlock Girl(abia)", player) and state.has("Pair Unlock (abia/lola)", player):
                return True
            elif state.has("Unlock Girl(nora)", player) and state.has("Pair Unlock (lola/nora)", player):
                return True
            elif state.has("Unlock Girl(jessie)", player) and state.has("Pair Unlock (jessie/lola)", player):
                return True
            elif state.has("Unlock Girl(zoey)", player) and state.has("Pair Unlock (lola/zoey)", player):
                return True
            else:
                return False

    elif girl == "jessie":
        if not state.has("Unlock Girl(jessie)", player):
            return False
        else:
            if state.has("Unlock Girl(lailani)", player) and state.has("Pair Unlock (jessie/lailani)", player):
                return True
            elif state.has("Unlock Girl(brooke)", player) and state.has("Pair Unlock (brooke/jessie)", player):
                return True
            elif state.has("Unlock Girl(lola)", player) and state.has("Pair Unlock (jessie/lola)", player):
                return True
            elif state.has("Unlock Girl(abia)", player) and state.has("Pair Unlock (abia/jessie)", player):
                return True
            else:
                return False

    elif girl == "lillian":
        if not state.has("Unlock Girl(lillian)", player):
            return False
        else:
            if state.has("Unlock Girl(ashley)", player) and state.has("Pair Unlock (ashley/lillian)", player):
                return True
            elif state.has("Unlock Girl(zoey)", player) and state.has("Pair Unlock (lillian/zoey)", player):
                return True
            elif state.has("Unlock Girl(lailani)", player) and state.has("Pair Unlock (lailani/lillian)", player):
                return True
            elif state.has("Unlock Girl(abia)", player) and state.has("Pair Unlock (abia/lillian)", player):
                return True
            else:
                return False

    elif girl == "zoey":
        if not state.has("Unlock Girl(zoey)", player):
            return False
        else:
            if state.has("Unlock Girl(lillian)", player) and state.has("Pair Unlock (lillian/zoey)", player):
                return True
            elif state.has("Unlock Girl(lola)", player) and state.has("Pair Unlock (lola/zoey)", player):
                return True
            elif state.has("Unlock Girl(sarah)", player) and state.has("Pair Unlock (sarah/zoey)", player):
                return True
            elif state.has("Unlock Girl(polly)", player) and state.has("Pair Unlock (polly/zoey)", player):
                return True
            else:
                return False

    elif girl == "sarah":
        if not state.has("Unlock Girl(sarah)", player):
            return False
        else:
            if state.has("Unlock Girl(lailani)", player) and state.has("Pair Unlock (lailani/sarah)", player):
                return True
            elif state.has("Unlock Girl(zoey)", player) and state.has("Pair Unlock (sarah/zoey)", player):
                return True
            elif state.has("Unlock Girl(nora)", player) and state.has("Pair Unlock (nora/sarah)", player):
                return True
            elif state.has("Unlock Girl(brooke)", player) and state.has("Pair Unlock (brooke/sarah)", player):
                return True
            else:
                return False

    elif girl == "lailani":
        if not state.has("Unlock Girl(lailani)", player):
            return False
        else:
            if state.has("Unlock Girl(sarah)", player) and state.has("Pair Unlock (lailani/sarah)", player):
                return True
            elif state.has("Unlock Girl(jessie)", player) and state.has("Pair Unlock (jessie/lailani)", player):
                return True
            elif state.has("Unlock Girl(lillian)", player) and state.has("Pair Unlock (lailani/lillian)", player):
                return True
            elif state.has("Unlock Girl(candace)", player) and state.has("Pair Unlock (candace/lailani)", player):
                return True
            else:
                return False

    elif girl == "candace":
        if not state.has("Unlock Girl(candace)", player):
            return False
        else:
            if state.has("Unlock Girl(nora)", player) and state.has("Pair Unlock (candace/nora)", player):
                return True
            elif state.has("Unlock Girl(lailani)", player) and state.has("Pair Unlock (candace/lailani)", player):
                return True
            elif state.has("Unlock Girl(abia)", player) and state.has("Pair Unlock (abia/candace)", player):
                return True
            elif state.has("Unlock Girl(polly)", player) and state.has("Pair Unlock (candace/polly)", player):
                return True
            else:
                return False

    elif girl == "nora":
        if not state.has("Unlock Girl(nora)", player):
            return False
        else:
            if state.has("Unlock Girl(lola)", player) and state.has("Pair Unlock (lola/nora)", player):
                return True
            elif state.has("Unlock Girl(candace)", player) and state.has("Pair Unlock (candace/nora)", player):
                return True
            elif state.has("Unlock Girl(sarah)", player) and state.has("Pair Unlock (nora/sarah)", player):
                return True
            elif state.has("Unlock Girl(ashley)", player) and state.has("Pair Unlock (ashley/nora)", player):
                return True
            else:
                return False

    elif girl == "brooke":
        if not state.has("Unlock Girl(brooke)", player):
            return False
        else:
            if state.has("Unlock Girl(jessie)", player) and state.has("Pair Unlock (brooke/jessie)", player):
                return True
            elif state.has("Unlock Girl(sarah)", player) and state.has("Pair Unlock (brooke/sarah)", player):
                return True
            elif state.has("Unlock Girl(ashley)", player) and state.has("Pair Unlock (ashley/brooke)", player):
                return True
            elif state.has("Unlock Girl(polly)", player) and state.has("Pair Unlock (brooke/polly)", player):
                return True
            else:
                return False

    elif girl == "ashley":
        if not state.has("Unlock Girl(ashley)", player):
            return False
        else:
            if state.has("Unlock Girl(polly)", player) and state.has("Pair Unlock (ashley/polly)", player):
                return True
            elif state.has("Unlock Girl(lillian)", player) and state.has("Pair Unlock (ashley/lillian)", player):
                return True
            elif state.has("Unlock Girl(nora)", player) and state.has("Pair Unlock (ashley/nora)", player):
                return True
            elif state.has("Unlock Girl(brooke)", player) and state.has("Pair Unlock (ashley/brooke)", player):
                return True
            else:
                return False

    elif girl == "abia":
        if not state.has("Unlock Girl(abia)", player):
            return False
        else:
            if state.has("Unlock Girl(lola)", player) and state.has("Pair Unlock (abia/lola)", player):
                return True
            elif state.has("Unlock Girl(jessie)", player) and state.has("Pair Unlock (abia/jessie)", player):
                return True
            elif state.has("Unlock Girl(lillian)", player) and state.has("Pair Unlock (abia/lillian)", player):
                return True
            elif state.has("Unlock Girl(candace)", player) and state.has("Pair Unlock (abia/candace)", player):
                return True
            else:
                return False

    elif girl == "polly":
        if not state.has("Unlock Girl(polly)", player):
            return False
        else:
            if state.has("Unlock Girl(ashley)", player) and state.has("Pair Unlock (ashley/polly)", player):
                return True
            elif state.has("Unlock Girl(zoey)", player) and state.has("Pair Unlock (polly/zoey)", player):
                return True
            elif state.has("Unlock Girl(candace)", player) and state.has("Pair Unlock (candace/polly)", player):
                return True
            elif state.has("Unlock Girl(brooke)", player) and state.has("Pair Unlock (brooke/polly)", player):
                return True
            else:
                return False

    return False