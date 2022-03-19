#region BURN
class Goblin_Guide:
    name = 'Goblin_Guide'
    cardtype = 'Creature'
    cmc = 1
    power = 2
    summoning_sickness = 0
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Monastery_Swiftspear:
    name = 'Monastery_Swiftspear'
    cardtype = 'Creature'
    cmc = 1
    power = 1
    summoning_sickness = 0
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Eidolon:
    name = 'Eidolon'
    cardtype = 'Creature'
    cmc = 2
    power = 2
    summoning_sickness = 1
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Spike_Jester:
    name = 'Spike_Jester'
    cardtype = 'Creature'
    cmc = 2
    power = 3
    summoning_sickness = 0
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Wild_Nacatl:
    name = 'Wild_Nacatl'
    cardtype = 'Creature'
    cmc = 1
    power = 3
    summoning_sickness = 1
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Lightning_Bolt:
    name = 'Lightning_Bolt'
    cardtype = 'Spell'
    cmc = 1
    spelldamage = 3
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.graveyard.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        s.damage_dealt += x.spelldamage
        s.prowess += 1
        return z, s, x
class Lava_Spike:
    name = 'Lava_Spike'
    cardtype = 'Spell'
    cmc = 1
    spelldamage = 3
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.graveyard.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        s.damage_dealt += x.spelldamage
        s.prowess += 1
        return z, s, x
class Rift_Bolt:
    name = 'Rift_Bolt'
    cardtype = 'Spell'
    cmc = 1
    spelldamage = 3
    def resolve(self, z, s, x):
        z.exile.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Boros_Charm:
    name = 'Boros_Charm'
    cardtype = 'Spell'
    cmc = 2
    spelldamage = 4
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.graveyard.append(x)
        z.hand.remove(x)
        s.damage_dealt += x.spelldamage
        s.mana_pool -= x.cmc
        s.prowess += 1
        return z, s, x
class Atarkas_Command:
    name = 'Atarkas_Command'
    cardtype = 'Spell'
    cmc = 2
    spelldamage = 3
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.graveyard.append(x)
        z.hand.remove(x)
        cnt = 0
        for b in z.battlefield:
            if hasattr(b, 'summoning_sickness'):
                if b.summoning_sickness == 0:
                    cnt += 1
        s.damage_dealt += (x.spelldamage + cnt)
        s.mana_pool -= x.cmc
        s.prowess += 1
        return z, s, x
class Skullcrack:
    name = 'Skullcrack'
    cardtype = 'Spell'
    cmc = 2
    spelldamage = 3
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.graveyard.append(x)
        z.hand.remove(x)
        s.damage_dealt += x.spelldamage
        s.mana_pool -= x.cmc
        s.prowess += 1
        return z, s, x
class Lightning_Helix:
    name = 'Lightning_Helix'
    cardtype = 'Spell'
    cmc = 2
    spelldamage = 3
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.graveyard.append(x)
        z.hand.remove(x)
        s.damage_dealt += x.spelldamage
        s.mana_pool -= x.cmc
        s.prowess += 1
        return z, s, x
class Fetchland:
    name = 'Fetchland'
    cardtype = 'Land'
    cmc = 0
class Land:
    name = 'Land'
    cardtype = 'Land'
    cmc = 0
#endregion

#region INFECT
class Glistener_Elf:
    name = 'Glistener_Elf'
    cardtype = 'Creature'
    cmc = 1
    power = 1
    summoning_sickness = 1
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Blighted_Agent:
    name = 'Blighted_Agent'
    cardtype = 'Creature'
    cmc = 2
    power = 1
    summoning_sickness = 1
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Noble_Hierarch:
    name = 'Noble_Hierarch'
    cardtype = 'Creature'
    cmc = 1
    power = 1
    summoning_sickness = 1
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.mana_pool -= x.cmc
        return z, s, x
class Blossoming_Defense:
    name = 'Blossoming_Defense'
    cardtype = 'Spell'
    cmc = 1
    spelldamage = 2
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.damage_dealt += 2
        s.mana_pool -= x.cmc
        return z, s, x
class Groundswell:
    name = 'Groundswell'
    cardtype = 'Spell'
    cmc = 1
    spelldamage = 2
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        if s.landfall == 1:
            s.damage_dealt += 4
        else:
            s.damage_dealt += 2
        s.mana_pool -= x.cmc
        return z, s, x
class Might_of_Old_Krosa:
    name = 'Might_of_Old_Krosa'
    cardtype = 'Spell'
    cmc = 1
    spelldamage = 4
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.damage_dealt += 2
        s.mana_pool -= x.cmc
        return z, s, x
class Vines_of_Vastwood:
    name = 'Vines_of_Vastwood'
    cardtype = 'Spell'
    cmc = 2
    spelldamage = 4
    def resolve(self, z, s, x):
        z.cast_this_turn.append(x)
        z.battlefield.append(x)
        z.hand.remove(x)
        s.damage_dealt += 4
        s.mana_pool -= x.cmc
        return z, s, x
#endregion

#region ZONES
class Zones:
    battlefield = []
    hand = []
    graveyard = []
    exile = []
    deck = []
    cast_this_turn = []


class Stats:
    with open('config.txt', 'r') as file:
        config = [line.rstrip() for line in file]
    archetype = 0
    for x in config:
        if x.count('ARCHETYPE'):
            archetype = int(x.split('=')[1])
        if x.count('LIFE_TOTAL'):
            life_total = int(x.split('=')[1])
        if x.count('ITERATIONS'):
            iterations = int(x.split('=')[1])
        if archetype == 2:
            life_total = 10
    if archetype == 0:
        exit()
    file.close()
    mana_pool = 0
    damage_dealt = 0
    turn = 0
    lands_in_play = 0
    prowess = 0
    total_turns = 0
    current_iteration = 0
    landfall = 0

#endregion
