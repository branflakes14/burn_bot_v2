import random
from classes import *

def load_deck():
    with open('decklist.txt', 'r') as file:
        deck_file = [line.rstrip() for line in file]
    deck_of_names = []
    deck = []
    for x in deck_file:
        parts = str(x).split(' ', 1)
        copies = int(parts[0])
        card = parts[1]
        for y in range(copies):
            deck_of_names.append(card)
    for x in deck_of_names:
        if x == 'Goblin Guide':
            deck.append(Goblin_Guide())
        elif x == 'Monastery Swiftspear':
            deck.append(Monastery_Swiftspear())
        elif x == 'Eidolon of the Great Revel':
            deck.append(Eidolon())
        elif x == 'Lightning Bolt':
            deck.append(Lightning_Bolt())
        elif x == 'Lava Spike':
            deck.append(Lava_Spike())
        elif x == 'Rift Bolt':
            deck.append(Rift_Bolt())
        elif x == 'Boros Charm':
            deck.append(Boros_Charm())
        elif x == 'Atarkas Command':
            deck.append(Atarkas_Command())
        elif x == 'Skullcrack':
            deck.append(Skullcrack())
        elif x == 'Lightning Helix':
            deck.append(Lightning_Helix())
        elif x == 'Land':
            deck.append(Land())
        elif x == 'Fetchland':
            deck.append(Fetchland())
        else:
            quit()
    if len(deck) != 60:
        exit()
    return deck
def shuffle(zones):
    random.shuffle(zones.deck)
    return zones
def drawcard(zones):
    zones.hand.append(zones.deck[0])
    del zones.deck[0]
    return zones
def getopeninghand(zones):
    while len(zones.hand) < 7:
        drawcard(zones)
    if (landcount(zones) < 2) or (landcount(zones) > 3):
        putbackhand(zones)
        shuffle(zones)
    while len(zones.hand) < 6:
        drawcard(zones)
    if (landcount(zones) < 2) or (landcount(zones) > 3):
        putbackhand(zones)
        shuffle(zones)
    while len(zones.hand) < 5:
        drawcard(zones)
    if (landcount(zones) < 1) or (landcount(zones) > 3):
        putbackhand(zones)
        shuffle(zones)
    while len(zones.hand) < 4:
        drawcard(zones)
    if (landcount(zones) == 0) or (landcount(zones) == 4):
        putbackhand(zones)
        shuffle(zones)
    while len(zones.hand) < 3:
        drawcard(zones)
    return zones
def landcount(zones):
    land = 0
    for x in zones.hand:
        if x.cardtype == 'Land':
            land += 1
    return land
def putbackhand(zones):
    while len(zones.hand) > 0:
        zones.deck.append(zones.hand[0])
        del zones.hand[0]
    return zones
def cast_rift_bolts(zones, stats):
    for x in zones.exile:
        if x.name == 'Rift_Bolt':
            stats.damage_dealt += 3
            zones.graveyard.append(x)
            zones.exile.remove(x)
            stats.prowess += 1
            zones.cast_this_turn.append('Rift_Bolt')
    return zones, stats
def card_names_in_zone(zones):
    h = []
    for x in zones:
        h.append(x.name)
    return h
def card_types_in_zone(zones):
    h = []
    for x in zones:
        h.append(x.cardtype)
    return h
def print_all_cards_in_game(zones):
    if len(zones.hand) > 0:
        print('Hand:', card_names_in_zone(zones.hand))
    if len(zones.battlefield) > 0:
        print('Battlefield:', card_names_in_zone(zones.battlefield))
    if len(zones.graveyard) > 0:
        print('Graveyard:', card_names_in_zone(zones.graveyard))
    if len(zones.exile) > 0:
        print('Exile:', card_names_in_zone(zones.exile))
def play_land(zones):
    if sum(x.cardtype == 'Land' for x in zones.hand) > 0:
        for x in zones.hand:
            if x.name == 'Fetchland':
                #find a Land in the deck and put it into play
                for y in zones.deck:
                    if y.name == 'Land':
                        zones.battlefield.append(y)
                        zones.deck.remove(y)
                        shuffle(zones)
                        break
                zones.graveyard.append(x)
                zones.hand.remove(x)
                return zones
        for x in zones.hand:
            if x.name == 'Land':
                zones.battlefield.append(x)
                zones.hand.remove(x)
                return zones
    return zones
def reset_game(zones, stats):
    zones.battlefield.clear()
    zones.hand.clear()
    zones.graveyard.clear()
    zones.exile.clear()
    zones.deck.clear()
    zones.deck = load_deck()
    stats.mana_pool = 0
    stats.damage_limit = 20
    stats.damage_dealt = 0
    stats.turn = 0
    stats.lands_in_play = 0
    stats.prowess = 0
    stats.current_iteration += 1
    return zones, stats
def swing(zones, stats):
    for x in zones.battlefield:
        if hasattr(x, 'power'):
            if hasattr(x, 'summoning_sickness'):
                if x.summoning_sickness == 0:
                    stats.damage_dealt += x.power
                    if x.name == 'Monastery_Swiftspear':
                        stats.damage_dealt += stats.prowess
    return zones, stats
#casting logic
def cast_spells(zones, stats):
    # cast a FAT command if 2+ creatures
    if (stats.mana_pool >= 2) and sum(x.name == 'Atarkas_Command' for x in zones.hand) > 0 and sum(y.cardtype == 'Creature' for y in zones.battlefield) >= 2:
        for x in zones.hand:
            if x.name == 'Atarkas_Command':
                x.resolve, zones, stats, x
    # manually hard cast rift bolt in topdeck mode
    if (stats.mana_pool >= 3) and (len(zones.hand) == 1) and (zones.hand[0].name == 'Rift_Bolt'):
        zones.graveyard.append(zones.hand[0])
        del zones.hand[0]
        stats.mana_pool -= 3
        stats.prowess += 1
        return zones, stats
    if stats.mana_pool >= 2:
        twomanapriority = ['Eidolon', 'Boros_Charm', 'Goblin_Guide', 'Monastery_Swiftspear', 'Rift_Bolt', 'Lava_Spike', 'Lightning_Bolt', 'Atarkas_Command', 'Lightning_Helix', 'Skullcrack']
        for c in twomanapriority:
            for x in zones.hand:
                if x.name == c:
                    if x.cmc <= stats.mana_pool:
                        x.resolve(zones, stats, x)
                        if stats.mana_pool == 0:
                            return zones, stats
    if stats.mana_pool == 1:
        onemanapriority = ['Goblin_Guide', 'Monastery_Swiftspear', 'Rift_Bolt', 'Lava_Spike', 'Lightning_Bolt']
        for c in onemanapriority:
            for x in zones.hand:
                if x.name == c:
                    if x.cmc >= stats.mana_pool:
                        x.resolve(zones, stats, x)
                        return zones, stats
    return zones, stats
