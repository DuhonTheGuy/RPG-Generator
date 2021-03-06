import time
from battle import Battle
# from battle import Boss
from inventory import Inventory

equipped = {"helm": ["Test Helm", 100000], "chestpiece": ["Test Chestpiece", 100000], "leggings": ["Test Leggings", 100000], "weapon": ["Test Sword", 100000]}

inventory = {}

class reader:
	def __init__(self):
		self.equipped = {"helm": ["Test Helm", 100000], "chestpiece": ["Test Chestpiece", 100000], "leggings": ["Test Leggings", 100000], "weapon": ["Test Sword", 100000]}
		self.inventory = {}
		self.variables = {}
		self.slotList = ["weapon", "helmet", "chestpiece", "leggings"]

	def read(self, path):
		slotList = ["weapon", "helmet", "chestpiece", "leggings"]
		# global equipped
		# global inventory
		with open(str(path), "r") as f:
			load = f.readlines()
		#variables = {}
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
		args = line[1].split(",")
		hit_chance = args[2]
		name = args[0]
		health = args[1]
		Battle.fight(self.equipped, hit_chance, name, health)

	def handleInventory(self, line):
		line = line.split("=")
		line = line[1]
		if line.startswith("+"):
			item = line[1:].split("^")
			name = item[0]
			stats = int(item[2])
			slot = item[1]
			if slot in self.slotList:
				pass
			else:
				print("Error: Slot not valid.")
				return
			self.inventory[str(name)] = Inventory.add(name, slot, stats, self.inventory)
			print("######################################################")
			print(f"||   You got a {name}! It's a {slot} with {stats} power!  ||")
			print("######################################################")
			print()
		elif line.startswith("-"):
			item = line[1:]
			if item.replace("\n", "") in self.inventory:
				self.inventory.pop(str(item.replace("\n", "")))
				print(f"Your {item[:len(item) - 1]} has been taken from your pockets!")
