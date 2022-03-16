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
        elif x == 'Wild Nacatl':
            deck.append(Wild_Nacatl())
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
    cntonecmc = 0
    for x in zones.hand:
        if hasattr(x, 'cmc'):
            if x.cmc == 1:
                cntonecmc += 1
    if (landcount(zones) < 2) or (landcount(zones) > 3) or cntonecmc == 0:
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
def creatures_on_battlefield(zones):
    h = []
    for x in zones.battlefield:
        if x.cardtype == 'Creature':
            h.append(x.name)
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
    stats.damage_dealt = 0
    stats.turn = 0
    stats.lands_in_play = 0
    stats.prowess = 0
    stats.current_iteration += 1
    return zones, stats
def swing(zones, stats):
    for x in zones.battlefield:
        if x.cardtype == 'Creature':
            if x.summoning_sickness == 0:
                if x.name == 'Monastery_Swiftspear':
                    stats.damage_dealt += (x.power + stats.prowess)
                else:
                    stats.damage_dealt += x.power
    return zones, stats
#casting logic
def cast_spells(zones, stats):
    # if you have two mana and only one 1cmc card in hand, don't cast a 1cmc card if there's a 2cmc card
    if stats.mana_pool == 2:
        cntone = 0
        cnttwo = 0
        for x in zones.hand:
            if hasattr(x, 'cmc'):
                if x.cmc == 1:
                    cntone += 1
        for x in zones.hand:
            if hasattr(x, 'cmc'):
                if x.cmc == 2:
                    cnttwo += 1
        if cntone == 1 and cnttwo > 1:
            list = ['Eidolon', 'Boros_Charm', 'Atarkas_Command', 'Lightning_Helix',
                               'Skullcrack', 'Goblin_Guide', 'Wild_Nacatl', 'Monastery_Swiftspear', 'Rift_Bolt',
                               'Lava_Spike', 'Lightning_Bolt']
            while stats.mana_pool > 0:
                for c in list:
                    for x in zones.hand:
                        if x.name == c:
                            if x.cmc <= stats.mana_pool:
                                x.resolve(zones, stats, x)
                if stats.mana_pool == 0:
                    return zones, stats
            return zones, stats
    # cast a FAT command if 2+ creatures
    if stats.mana_pool >= 2 and sum(x.name == 'Atarkas_Command' for x in zones.hand) > 0 and sum(y.cardtype == 'Creature' for y in zones.battlefield) >= 2:
        for x in zones.hand:
            if x.name == 'Atarkas_Command':
                x.resolve(zones, stats, x)
                break
    # manually hard cast rift bolt if it's the only play
    rifts = sum(x.name == 'Rift_Bolt' for x in zones.hand)
    lands = sum(x.cardtype == 'Land' for x in zones.hand)
    if stats.mana_pool >= 3 and len(zones.hand) == (rifts+lands):
        for x in zones.hand:
            if x.name == 'Rift_Bolt':
                zones.graveyard.append(x)
                zones.hand.remove(x)
                stats.mana_pool -= 3
                stats.prowess += 1
                break
    # hold off casting nacatl if it's turn 3+
    if stats.turn >= 3:
        if stats.mana_pool >= 2:
            list = ['Eidolon', 'Goblin_Guide', 'Monastery_Swiftspear', 'Rift_Bolt',
                    'Lava_Spike', 'Lightning_Bolt', 'Boros_Charm', 'Atarkas_Command',
                    'Lightning_Helix', 'Skullcrack', 'Wild_Nacatl']
            while stats.mana_pool > 0 and sum(x.cardtype != 'Land' for x in zones.hand) > 0:
                for c in list:
                    for x in zones.hand:
                        if x.name == c:
                            if x.cmc <= stats.mana_pool:
                                x.resolve(zones, stats, x)
                if stats.mana_pool == 1 and sum(x.cardtype != 'Land' for x in zones.hand) > 0:
                    break
            return zones, stats
    # generic casting turns
    if stats.mana_pool >= 2:
        list = ['Eidolon', 'Goblin_Guide', 'Wild_Nacatl', 'Monastery_Swiftspear', 'Rift_Bolt',
                           'Lava_Spike', 'Lightning_Bolt', 'Boros_Charm',  'Atarkas_Command',
                           'Lightning_Helix', 'Skullcrack']
        while stats.mana_pool > 0 and sum(x.cardtype != 'Land' for x in zones.hand) > 0:
            for c in list:
                for x in zones.hand:
                    if x.name == c:
                        if x.cmc <= stats.mana_pool:
                            x.resolve(zones, stats, x)
            if stats.mana_pool == 1 and sum(x.cardtype != 'Land' for x in zones.hand) > 0:
                break
        return zones, stats
    if stats.mana_pool == 1 and sum(x.cardtype != 'Land' for x in zones.hand) > 0:
        list = ['Wild_Nacatl', 'Goblin_Guide', 'Monastery_Swiftspear', 'Rift_Bolt', 'Lava_Spike', 'Lightning_Bolt']
        for c in list:
            for x in zones.hand:
                if x.name == c:
                    if x.cmc >= stats.mana_pool:
                        x.resolve(zones, stats, x)
                        return zones, stats
    return zones, stats
