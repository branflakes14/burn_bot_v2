def burn_logic(zones, stats):
    # check we don't double 1cmc spell on 3 mana and get left with 2cmc cards we can't cast
    cntonespells = 0
    if stats.mana_pool == 3:
        for x in zones.hand:
            if hasattr(x, 'cmc'):
                if x.cmc == 1:
                    cntonespells += 1
    if cntonespells == 2:
        list = ['Goblin_Guide', 'Monastery_Swiftspear', 'Rift_Bolt', 'Lava_Spike', 'Lightning_Bolt']
        for c in list:
            for x in zones.hand:
                if x.name == c:
                    if x.cmc >= stats.mana_pool:
                        x.resolve(zones, stats, x)
                        break
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
                stats.damage_dealt += 3
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
