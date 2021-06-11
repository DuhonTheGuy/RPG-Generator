import random

class Battle:
	base_health = 100
	def fight(equipped, hit_chance, enemy_name="Monster", enemy_hp=10):
		battle = True
		# While the battle is going on, well, battle goes on
		while battle:
			a = int(input("What to do?\n1. Fight\n2. Run"))
			if a == 1:
				chance = random.random()
				if chance > (int(hit_chance)/100):
					weapon = equipped["weapon"]
					print(f"Hit for {weapon[1]}!\n")
					if int(weapon[1]) > int(enemy_hp):
						print(f"{enemy_name} has been defeated!")
						battle = False
				else:
					print("Argh! A miss!")
# class Boss: