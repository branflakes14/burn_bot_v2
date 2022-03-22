from functions import *

def burn_logic_v2(zones, stats):
    # manually hard cast rift bolt if it's the only play
    rifts = sum(x.name == 'Rift_Bolt' for x in zones.hand)
    lands = sum(x.cardtype == 'Land' for x in zones.hand)
    if stats.mana_pool >= 3 and len(zones.hand) == (rifts+lands):
        for x in zones.hand:
            if x.name == 'Rift_Bolt':
                zones.graveyard.append(x)
                zones.hand.remove(x)
                stats.damage_dealt += 3
                stats.mana_pool -= 3
                stats.prowess += 1
                break

    # if we're at odd mana, try and get to even mana
    list = ['Goblin_Guide', 'Monastery_Swiftspear', 'Wild_Nacatl', 'Rift_Bolt', 'Lava_Spike', 'Lightning_Bolt']
    if stats.turn >= 3:
        list = ['Lava_Spike', 'Lightning_Bolt', 'Goblin_Guide', 'Monastery_Swiftspear', 'Wild_Nacatl', 'Rift_Bolt']
    if stats.mana_pool % 2:
        for c in list:
            tripped = 0
            for x in zones.hand:
                if x.name == c:
                    x.resolve(zones, stats, x)
                    tripped = 1
                    break
            if tripped == 1:
                break

    # cast a FAT command if 2+ creatures
    if stats.mana_pool >= 2 and sum(x.name == 'Atarkas_Command' for x in zones.hand) > 0 and sum(y.cardtype == 'Creature' for y in zones.battlefield) >= 2:
        for x in zones.hand:
            if x.name == 'Atarkas_Command':
                x.resolve(zones, stats, x)
                break

    # force eidolon t2 before next comment code
    if stats.mana_pool == 2:
        for x in zones.hand:
            if x.name == 'Eidolon':
                x.resolve(zones, stats, x)
                return zones, stats

    # then check if we can cast 1cmc spells equal to our remaining mana, if so do so
    cntonemana = 0
    for x in zones.hand:
        if x.cardtype != 'Land':
            if x.cmc == 1:
                cntonemana += 1
    if cntonemana >= stats.mana_pool:
        while stats.mana_pool > 0:
            for c in list:
                for x in zones.hand:
                    if x.name == c:
                        x.resolve(zones, stats, x)
                        if stats.mana_pool == 0:
                            return zones, stats


    # otherwise just spaff the hand, fam
    list = ['Eidolon', 'Boros_Charm', 'Atarkas_Command', 'Lightning_Helix', 'Skullcrack', 'Goblin_Guide', 'Monastery_Swiftspear', 'Lava_Spike', 'Lightning_Bolt', 'Rift_Bolt', 'Wild_Nacatl']
    # while we still have mana, keep trying to cast spells
    while stats.mana_pool > 0:
        temp = zones.hand
        for c in list:
            for x in zones.hand:
                if x.name == c and stats.mana_pool >= x.cmc:
                    x.resolve(zones, stats, x)


        if zones.hand == temp:
            return zones, stats


    return zones, stats
