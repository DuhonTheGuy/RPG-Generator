import random

class Battle:
	def __init__(equipped, hit_chance, enemy_name="Monster", enemy_hp=10):
		self.equipped = equipped
		self.hit_chance = hit_chance
		self.enemy_name = enemy_name
		self.enemy_hp = enemy_hp
	
	def start_battle(self):
		while True:
			while True:
				try:
					a = int(input('What to do?\n1. Fight\n2. Run'))
					if a not in range(1, 3):
						raise TypeError		# This is just to call the except statement
					else:
						break
				except TypeError:
					print('Please select a valid input')
		
			if a == 1:
				chance = random.random()
				if chance > int(self.hit_chance) / 100:
					weapon = self.equipped['weapon']
					print('Hit for {}!\n'.format(weapon[1]))
					if int(weapon[1]) > int(self.enemy_hp):
						print('{} has been defeated!'.format(self.enemy_name))
						break
					else:
						print('Argh! A miss!')