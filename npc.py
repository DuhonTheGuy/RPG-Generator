import inventory

class NPC:
    """
    Gear is an inventory object. Everything that is in the bag is dropped upon death, and everything equipped
    has a 10% chance to drop too. Evasion goes from 0 to 100, and indicates the enemy's chance to dodge
    """
    def __init__(self, gear, name, aggro=0, boss=0, HP=1, evasion=0): 
        self.gear = gear
        self.aggro = aggro
        self.boss = boss
        self.HP = HP
        self.evasion = evasion
        self.name = name
