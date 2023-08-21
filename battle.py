import random
import npc
import inventory
import player

# class Battle:
# 	base_health = 100
# 	def fight(equipped, hit_chance, enemy_name="Monster", enemy_hp=10):
# 		battle = True
# 		# While the battle is going on, well, battle goes on
# 		while battle:
# 			a = int(input("What to do?\n1. Fight\n2. Run"))
# 			if a == 1:
# 				chance = random.random()
# 				if chance > (int(hit_chance)/100):
# 					weapon = equipped["weapon"]
# 					print(f"Hit for {weapon[1]}!\n")
# 					if int(weapon[1]) > int(enemy_hp):
# 						print(f"{enemy_name} has been defeated!")
# 						battle = False
# 				else:
# 					print("Argh! A miss!")
# # class Boss:

# ^ this up here is hot garbage code I made years ago, time for something proper.

class Battle: # returning 0 on a method = you died, returning 1 = you won.
	def __init__(self, gear, enemy, player, currentHealth=-1): # currentHealth is pretty self-explanatory, an integer from 1 to 100 (technically 0 too but then you are dead). Gear is an inventory object. Enemy is a NPC object.
		self.gear = gear
		self.currentHealth = currentHealth
		self.enemy = enemy
		self.player = player
		if self.currentHealth == -1:
			self.currentHealth = self.player.HP
			if self.currentHealth <= 0:
				print("You are not an anime protagonist, as much as you may want to be. Regain health before fighting again!")
				return 0
	def attack(self, offhand): # offhand is only 1 if offhand is being used for the attack.
		HP = self.enemy.HP
		Dmg = self.gear.equip[offhand].stats + self.player.strength - (self.enemy.gear.equip[2].stats) # little trick, mainWeapon is 0 and offhand is 1 in the equip list
		if Dmg < 0:
			Dmg = 0
		evasion = 100 - self.enemy.evasion
		if evasion >= random.random()*100:
			HP -= Dmg
			print(f"Hit {self.enemy.name} for a {Dmg}.")
			if HP <= 0:
				print("Victory!")
				return 1
			self.enemy.HP = HP
		else:
			print("Ya missed!")
			return 0

	def beAttacked(self):
		HP = self.player.HP
		Dmg = self.enemy.gear.equip[0].stats - self.player.defense - (self.gear.equip[2].stats) # randomly uses either offhand or main hand
		if Dmg < 0:
			Dmg = 0
		evasion = 100 - self.player.evasion
		print(f"{self.enemy.name} attacks you, a hit worth {Dmg} damage!")
		if evasion >= random.random()*100:
			HP -= Dmg
			if HP <= 0:
				print("You died, ouch.")
				return 0
			else:
				print(f"You took damage from the enemy, now you got {HP} health left.")
				return 1
		else:
			print("It passed right by you.")
			return 1

	def printHP(self):
		print(f"You have {self.player.HP} HP left.")

	def enemyHP(self):
		print(f"{self.enemy.name} has {self.enemy.HP} HP left.")

	def fightLoop(self):
				# While the battle is going on, well, battle goes on
		battle = 1
		while battle:
			a = int(input("What to do?\n1. Fight\n2. See your HP\n3.See enemy HP\n4. Run\n"))
			if a == 1:
				b = int(input("Main weapon (1) or offhand (2)?\n"))
				result = self.attack(b - 1)
				battle = not result
			elif a == 4:
				if random.random() > .5:
					print("Got away.")
					return
				else:
					print("Failed to run away!")
					result = self.beAttacked()
					battle = result
			elif a == 2:
				self.printHP()
			elif a == 3:
				self.enemyHP()
			self.beAttacked()
			
			

			

		
