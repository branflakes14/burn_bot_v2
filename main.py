#!/usr/bin/python3
from functions import *
from classes import *

zones = Zones
stats = Stats

while stats.current_iteration < stats.max_goldfishes:
    # pregame stuff
    reset_game(zones, stats)
    # shuffle and draw a starting hand
    shuffle(zones)
    getopeninghand(zones)
    # play a game
    while stats.damage_dealt < stats.damage_limit:
        # upkeep/draw
        stats.prowess = 0
        stats.total_turns += 1
        stats.turn += 1
        cast_rift_bolts(zones, stats)
        if stats.turn > 1:
            drawcard(zones)
        print('Turn:', stats.turn)
        print('Hand after draw step:', card_names_in_zone(zones.hand))
        # play a land if possible and make mana
        play_land(zones)
        stats.mana_pool = sum(x.cardtype == 'Land' for x in zones.battlefield)
        # decide what spells to cast based on how much mana we have
        cast_spells(zones, stats)
        # combat

        print('Battlefield precombat:', card_names_in_zone(zones.battlefield))
        swing(zones, stats)

        # end of turn
        for x in zones.battlefield:
            if hasattr(x, 'summoning_sickness'):
                x.summoning_sickness == 0
            if x.name == 'Eidolon':
                stats.damage_dealt += 2

        cast = []
        for x in zones.cast_this_turn:
            if hasattr(x, 'name'):
                cast.append(x.name)
            else:
                cast.append(x)
        print('Cast this turn:', cast)
        print('Damage dealt by EOT:', stats.damage_dealt)
        print('-------------------------')
        zones.cast_this_turn.clear()
        cast.clear()


# result
print('Goldfishes performed:', stats.max_goldfishes)
print('Total turns taken:', stats.total_turns)
print('Average turn to kill:', stats.total_turns/stats.max_goldfishes)
