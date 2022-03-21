def burn_logic_v3(zones, stats):
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
            for x in zones.hand:
                if x.name == c:
                    x.resolve(zones, stats, x)

    # cast a FAT command if 2+ creatures
    if stats.mana_pool >= 2 and sum(x.name == 'Atarkas_Command' for x in zones.hand) > 0 and sum(y.cardtype == 'Creature' for y in zones.battlefield) >= 2:
        for x in zones.hand:
            if x.name == 'Atarkas_Command':
                x.resolve(zones, stats, x)
                break
    return zones, stats

