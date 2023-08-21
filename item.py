class Item:
    def __init__(self, slot, name, stats=0): # Slot is based on inventory's equip order.
        self.stats = stats
        self.slot = slot
        self.name = name