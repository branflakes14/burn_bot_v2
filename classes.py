#region CARDS
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
        s.prowess
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

#region ZONES
class Zones:
    battlefield = []
    hand = []
    graveyard = []
    exile = []
    deck = []
    cast_this_turn = []

class Stats:
    mana_pool = 0
    life_total = 20
    damage_dealt = 0
    turn = 0
    lands_in_play = 0
    prowess = 0
    total_turns = 0
    current_iteration = 0
    max_goldfishes = 1

#endregion
