import time
from battle import Battle
# from battle import Boss
from inventory import Inventory

equipped = {"helm": ["Test Helm", 100000], "chestpiece": ["Test Chestpiece", 100000], "leggings": ["Test Leggings", 100000], "weapon": ["Test Sword", 100000]}

inventory = {}

class reader:
	def read(path):
		slotList = ["weapon", "helmet", "chestpiece", "leggings"]
		global equipped
		global inventory
		with open(str(path), "r") as f:
			load = f.readlines()
		variables = {}
		# Starts reading line by line
		for line in load:
			# Code to print
			if line.startswith("-"):
				line = line[1:].replace("\n", "")
				print(line)
				print()
			# Code to print variables
			elif line.startswith("#-"):
				line = line[2:].replace("\n", "")
				if str(line) not in variables:
					print(f"Error: Variable not found, '{line}'")
				else:
					print(f"{variables[str(line)]}")
					print()
			# Code to declare variables
			elif line.startswith("#"):
				line = line[1:].replace("\n", "")
				var = line.split("=")
				if var[1].startswith("+"):
					var[1] = input(var[1].replace("+", ""))
					variables[str(var[0])] = var[1]
				# Basic math with variables
				elif var[1].startswith("math."):
					var[1] = var[1].replace("math.", "")
					if "+" in var[1]:
						numbers = var[1].split("+")
						numbers = [int(i) for i in numbers]
						variables[str(var[0])] = sum(numbers)
			# Print with input waiting
			elif line.startswith("/"):
				line = line[1:].replace("\n", "")
				input(line)
				print()
			# Built-in battle
			elif line.startswith(".battle"):
				line = line[1:].replace("\n", "")
				line = line.split("=")
				args = line[1].split(",")
				hit_chance = args[2]
				name = args[0]
				health = args[1]
				Battle.fight(equipped, hit_chance, name, health)
			# Inventory shenanigans
			elif line.startswith(".item"):
				line = line.split("=")
				line = line[1]
				if line.startswith("+"):
					item = line[1:].split("^")
					name = item[0]
					stats = int(item[2])
					slot = item[1]
					if slot in slotList:
						pass
					else:
						print("Error: Slot not valid.")
						return
					inventory[str(name)] = Inventory.add(name, slot, stats, inventory)
					print("######################################################")
					print(f"||   You got a {name}! It's a {slot} with {stats} power!  ||")
					print("######################################################")
					print()
				elif line.startswith("-"):
					item = line[1:]
					if item.replace("\n", "") in inventory:
						inventory.pop(str(item.replace("\n", "")))
						print(f"Your {item[:len(item) - 1]} has been taken from your pockets!")