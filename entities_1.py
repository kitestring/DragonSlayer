import enemy_dict_1
from random import randint
from math import ceil
from math import exp

class being(object):
	def alive(self, hp):
		if hp < 1:
			return False
		else:
			return True
	
class DragonSlayer(being):
	def __init__(self):
		self.level = 1
		self.hp = 30
		self.max_hp = 30
		self.experience = 0
		self.offense = 3
		self.defense = 3
		self.agility = 2
		self.gold = 50
		self.weapon = "Unarmed"
		self.armor = "Naked"
		self.healing = 0
		self.wings = 0
		self.lvl_up = []
		self.init_lvl_up()
		
	def init_lvl_up(self):
		self.lvl_up.append(0)
		self.lvl_up.append(7)
		for i in range(2,51):
			new_value = ceil(self.lvl_up[i-1]+(self.lvl_up[i-1]/2.0))
			self.lvl_up.append(new_value)
	
	def lvl_chk(self):
		if self.experience >= self.lvl_up[self.level]:
			self.level += 1
			self.max_hp = ceil(self.max_hp+(self.max_hp*0.25))
			self.hp = self.max_hp
			self.offense += 3 
			self.defense += 3 
			self.agility += 2
			return True
		else:
			return False
			
			
class Enemy(being):
	def __init__(self, type):
		self.name = enemy_dict_1.creatures[type]["name"]
		self.hp = enemy_dict_1.creatures[type]["HP"]
		self.xp = enemy_dict_1.creatures[type]["XP"]
		self.gold = enemy_dict_1.creatures[type]["Gold"]
		self.offense = enemy_dict_1.creatures[type]["Offense"]
		self.defense = enemy_dict_1.creatures[type]["Defense"]
		self.agility = enemy_dict_1.creatures[type]["Agility"]
		self.gold = self.enemy_gold(self.gold)
		
	def enemy_gold(self, max_gold):
		min_gold = ceil(max_gold/2)
		return randint(min_gold,max_gold)