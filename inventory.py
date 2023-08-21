import item

class Inventory:
	# def add(item, slot, stat, bag):
	# 	bag = {
	# 		"slot": str(slot),
	# 		"stat": int(stat)
	# 	}
	# 	return bag

	# ^ old code
	def __init__(self, items=[], equip=[]): # Note: Elements of "items" have to be item objects
		self.items = items # Bag items
		self.equip = equip # Equipped, in the order of: [mainWeapon, offhand, armor, trinket]
	def give(self, gifts=None): # Note: Gifts are item objects too!
		self.items.append(gifts)
	def take(self, rob=[]):
		for i in rob:
			try:
				self.items.remove(i)
			except:
				print("Error: Item not found in bag.")
				pass
	def peek(self):
		print("You are carrying:")
		bag = ""
		for i in self.items:
			bag += f"    - {i.name}, with a number of {i.stats}\n"
	def equipThis(self, putOn=[]):
		for i in putOn:
			if i in self.items:
				self.equip.append(i)
	def unequip(self, takeOff=[]):
		for i in takeOff:
			if i in self.equip:
				self.equip.remove(i)
	def nameList(self):
		return [(_.name, _) for _ in self.items]
	