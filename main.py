#!/usr/bin/python3
from functions import *
from classes import *

zones = Zones
stats = Stats

with open("config.txt", 'r') as file:
    stuff = [line.rstrip() for line in file]
file.close()

while stats.current_iteration < stats.iterations:
    if stats.goldfishmode == 1:
        print(stats.current_iteration)
    # pregame stuff
    reset_game(zones, stats)
    # shuffle and draw a starting hand
    shuffle(zones)
    getopeninghand(zones, stats)
    # play a game
    while stats.damage_dealt < stats.life_total:
        # upkeep/draw
        stats.landfall = 0
        stats.mana_pool = 0
        stats.prowess = 0
        stats.total_turns += 1
        stats.turn += 1
        cast_rift_bolts(zones, stats)
        if stats.turn > 1:
            drawcard(zones)
        if stats.goldfishmode == 0:
            print('Turn:', stats.turn)
            print('Hand after draw step:', card_names_in_zone(zones.hand))
        # play a land if possible and make mana
        x = sum(z.cardtype == 'Land' for z in zones.battlefield)
        play_land(zones)
        if sum(z.cardtype == 'Land' for z in zones.battlefield) > x:
            stats.landfall = 1
        stats.mana_pool += sum(x.cardtype == 'Land' for x in zones.battlefield)
        if stats.goldfishmode == 0:
            print('Mana for turn:', stats.mana_pool)
        # decide what spells to cast based on how much mana we have
        cast_spells(zones, stats)
        cast = []
        for x in zones.cast_this_turn:
            if hasattr(x, 'name'):
                cast.append(x.name)
            else:
                cast.append(x)
        if stats.goldfishmode == 0:
            if len(cast) > 0:
                print('Cast this turn:', cast)
            if len(zones.exile) > 0:
                print('Suspended this turn:', card_names_in_zone(zones.exile))
        # combat
        if stats.goldfishmode == 0:
            if len(creatures_on_battlefield(zones)) > 0:
                print('Battlefield:', creatures_on_battlefield(zones))
        swing(zones, stats)

        # end of turn
        for x in zones.battlefield:
            if x.cardtype == 'Creature':
                x.summoning_sickness = 0
            if x.name == 'Eidolon':
                stats.damage_dealt += 2
        if stats.goldfishmode == 0:
            print('Damage dealt by EOT:', stats.damage_dealt)
            print('-------------------------')
        zones.cast_this_turn.clear()
        cast.clear()


# result
print('Goldfishes performed:', stats.iterations)
print('Total turns taken:', stats.total_turns)
print('Average turn to kill:', stats.total_turns/stats.iterations)
