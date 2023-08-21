# ====================================
# Basically the compiler
# ====================================
import time
import battle
import inventory
import item
import player
import npc


class reader:
	"""
	The gear and player lists describe the objects. For gear you'd do [[("item1", stats, slot), ("item2", stats, slot)],[("equip1", stats, slot), ("equip2", stats, slot)]], where the first nested list is the bag, the second is the equips.
	For the player its just a 4-tuple of the stats
	"""
	def __init__(self):
		self.variables = {}
		self.items = None
		self.playerStats = None

	def start(self, gear=[[],[]], playerStats=(100, 0, 0, 0)):
		# Initializes the player's inventory
		bag = []
		for i in gear[0]:
			bag.append(item.Item(int(i[2]), i[0], int(i[1])))
		equipped = [0]*4
		for i in gear[1]:
			equipped[i[2]] = (item.Item(int(i[2]), i[0], int(i[1])))
		self.items = inventory.Inventory(bag, equipped)

		self.playerStats = player.Player(int(playerStats[0]), int(playerStats[1]), int(playerStats[2]), int(playerStats[3]))

	def read(self, path, startFile):
		with open(str(startFile), "r") as j:
			load = j.readlines()
		gear = eval(load[0].replace("\n", ""))
		playerStats = eval(load[1].replace("\n", ""))
		self.start(gear, playerStats)
		j.close()
		with open(str(path), "r") as f:
			load = f.readlines()
		# Starts reading line by line
		for line in load:
			# Code to print

			if line.startswith("-"):
				self.printLine(line)

			# Code to print variables
			elif line.startswith("#-"):
				self.printVar(line)

			# Code to declare variables
			elif line.startswith("#"):
				self.handleVar(line)

			# Print with input waiting
			elif line.startswith("/"):
				self.printLineWait(line)

			# Built-in battle
			elif line.startswith(".battle"):
				self.handleBattle(line)

			# Inventory shenanigans
			elif line.startswith(".item"):
				self.handleInventory(line)





	def printLine(self, line):
		line = line[1:].replace("\n", "")
		print(line)

	def printVar(self, line):
		line = line[2:].replace("\n", "")
		if str(line) not in self.variables:
			print(f"Error: Variable not found, '{line}'")
		else:
			print(f"{self.variables[str(line)]}")
			print()

	def handleVar(self, line):
		line = line[1:].replace("\n", "")
		var = line.split("=")
		if var[1].startswith("+"):
			var[1] = input(var[1].replace("+", ""))
			self.variables[str(var[0])] = var[1]
		# Basic math with variables
		elif var[1].startswith("math."):
			var[1] = var[1].replace("math.", "")
			if "+" in var[1]:
				numbers = var[1].split("+")
				numbers = [int(i) for i in numbers]
				self.variables[str(var[0])] = sum(numbers)

	def printLineWait(self, line):
		line = line[1:].replace("\n", "")
		input(line)
		print()

	def handleBattle(self, line):
		line = line[1:].replace("\n", "")
		line = line.split("=")
		args = line[1].split(", ")
		name = args[0]
		health = args[1]
		armor = args[2].replace("(", "").replace(")", "").split(";")
		armorItem = item.Item(2, armor[0], int(armor[1]))
		weapon = args[3].replace("(", "").replace(")", "").split(";")
		evasion = args[4]
		weaponItem = item.Item(2, weapon[0], int(weapon[1]))
		enemyItems = inventory.Inventory([], [weaponItem, None, armorItem, None])
		enemy = npc.NPC(enemyItems, name, 1, 0, int(health), int(evasion))
		basicallyStreetFighter = battle.Battle(self.items, enemy, self.playerStats)
		battle.Battle.fightLoop(basicallyStreetFighter)

	def handleInventory(self, line):
		line = line.split("=")
		line = line[1]
		if line.startswith("+"):
			itemRead = line[1:].split("^")
			name = itemRead[0]
			stats = int(itemRead[2])
			slot = itemRead[1]
			obj = item.Item(slot, name, stats)
			self.items.give(obj)
			print("######################################################")
			print(f"||   You got a {name}! It's a {slot} with {stats} power!  ||")
			print("######################################################")
			print()
		elif line.startswith("-"):
			itemRead = line[1:]
			inv = self.items.nameList()
			itemReadName = itemRead.replace("\n", "")
			if itemRead.replace("\n", "") in [_[0] for _ in inv]:
				ind = [_[0] for _ in inv].index(itemRead.replace("\n", ""))
				self.items.take([inv[ind][1]])
				print(f"Your {itemReadName} has been taken from your pockets!")
