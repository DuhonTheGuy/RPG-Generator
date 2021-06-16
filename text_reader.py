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
				line = self.handleLines(line, 1)
				self.printLine(line)

			# Code to print variables
			elif line.startswith("#-"):
				line = self.handleLines(line, 2)
				self.printVar(line)

			# Code to declare variables
			elif line.startswith("#"):
				line = self.handleLines(line, 1)
				self.handleVar(line)

			# Print with input waiting
			elif line.startswith("/"):
				line = self.handleLines(line, 1)
				self.printLineWait(line)

			# Built-in battle
			elif line.startswith(".battle"):
				line = self.handleLines(line, 1)
				self.handleBattle(line)

			# Inventory shenanigans
			elif line.startswith(".item"):
				line = self.handleLines(line, 1)
				self.handleInventory(line)

			# Choice system
			elif line.startswith("%"):
				line = self.handleLines(line, 1)
				self.handleChoice(line)
			
# ==========================================================================================================================

	def handleChoice(self, line):
		choiceTitle = line.replace("%", "").split(":")
		choice = [str(count + 1) + ". " + str(item) for count, item in enumerate(choiceTitle[1].split("^"))]
		print("You are presented with a choice: " + choiceTitle[0] + "\n" + ' \n'.join(choice)) # Prints out all of the choices, and since f strings can't have "\n" I had to make this monstrocity
		try:
			a = int(input())
			print(f"You choose {choice[a - 1].replace('.', ',')}")
		except:
			print("Error: Choice answer must be a number.")
			return

	def printLine(self, line):
		print(line)

	def printVar(self, line):
		if str(line) not in self.variables:
			print(f"Error: Variable not found, '{line}'")
		else:
			print(f"{self.variables[str(line)]}")
			print()

	def handleVar(self, line):
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
		input(line)
		print()

	def handleBattle(self, line):
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
			item = line.split("^")
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
			item = line
			if item.replace("\n", "") in self.inventory:
				self.inventory.pop(str(item.replace("\n", "")))
				print(f"Your {item[:len(item) - 1]} has been taken from your pockets!")

	def handleLines(self, line, commandSize):
		line = line[int(commandSize):].replace("\n", "")
		return line
