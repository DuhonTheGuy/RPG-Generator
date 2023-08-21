class Player:
    def __init__(self, HP=0, evasion=0, strength=0, defense=0): # everything here is basically an NPC, except defense which is a player-only stat, along with strength. Both add to item damage/damage mitigation.
        self.HP = HP
        self.evasion = evasion
        self.strength = strength
        self.defense = defense
        