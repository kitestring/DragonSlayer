from random import randint
from math import ceil

def encounter_enemy(stomping,column):
	
	if stomping == True:
		probability = 90
	elif stomping == False:
		probability = 40
	
	result = true_false(probability)
	
	if result:
		return result, enemy_type(enemy_zone(column))
	else:
		return result, None
		
def enemy_type(zone):
	if zone == 1:
		low = 0
	else:
		low = (zone-2)*2
	high = ((zone-1)*2)+1
	
	return randint(low,high)
	
def true_false(probability):
	number = randint(1,100)
	
	if number < probability:
		return True
	else:
		return False
		
def enemy_zone(column):
	zone = ceil((column + 1.0)/5.0)
	
	if zone == 13:
		zone = 12
	
	return zone
	
def hit_flee_success(attacker_agility, defender_agility):
	probability = 50.0 + ((attacker_agility - defender_agility)*10)
	
	if probability < 0:
		probability = 0
	elif probability > 100:
		probability = 100
	
	return true_false(probability)
	
def damage(attacker_offense, defender_defense):
	result = attacker_offense - defender_defense
	if result < 1:
		result = 1
	return result
