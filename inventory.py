class Inventory:
	def add(item, slot, stat, bag):
		bag = {
			"slot": str(slot),
			"stat": int(stat)
		}
		return bag;