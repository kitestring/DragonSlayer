import items_dict_1

class Bazaar(object):
	def __init__(self):
		self.present = False
		self.index = 0
		self.item_key = [items_dict_1.weapons, items_dict_1.armor, items_dict_1.misc]
		self.item = items_dict_1
		
	def selected_item(self, row):
		index = row - 2
		name = self.item_key[self.index][index]
		if self.index == 0:
			price, battle_attributes = self.get_weapon(name)
		elif self.index == 1:
			price, battle_attributes = self.get_armor(name)
		elif self.index == 2:
			price = self.item.misc_price[name]
			battle_attributes = None
			
		return name, price, battle_attributes
	
	def get_weapon(self, name):
		price = self.item.weapon_price[name]
		battle_attributes = self.item.weapon_offense[name]
		return price, battle_attributes
		
	def get_armor(self, name):
		price = self.item.armor_price[name]
		battle_attributes = self.item.armor_defense[name]
		return price, battle_attributes
	
	def build_menu(self, row):
		e = " "
		c = "  -->"
		braketer = "-" * 12
		
		for i in range(0,len(self.item_key[self.index])):
			if self.index == 0 and i == 0:
				title = "Weapons for Sale" 
				t = "Off"
				prev = ""
				next = "next"
			elif self.index == 1 and i == 0:
				title = "Armor for Sale"
				t = "Def"
				prev = "previous"
				next = "next"
			elif self.index == 2 and i == 0:
				title = "Other Items for Sale"
				prev = "previous"
				next = ""
				
			if i == 0:
				result = braketer + title + braketer + "\n\n" + prev + "\n"
			
			if i == row - 2:
				l = c
			else:
				l = e
			
			if self.index == 0:
				if i==1 or i==3:
					result += l + "\t%s:\t\tGold: %d\t\t%s: %d" % (self.item_key[self.index][i], 
									self.item.weapon_price[self.item_key[self.index][i]], t,
									self.item.weapon_offense[self.item_key[self.index][i]])
				elif i == len(self.item_key[self.index])-1:
					result += l + "\t%s:\tGold: %d\t%s: %d" % (self.item_key[self.index][i], 
									self.item.weapon_price[self.item_key[self.index][i]], t,
									self.item.weapon_offense[self.item_key[self.index][i]])
				else:
					result += l + "\t%s:\tGold: %d\t\t%s: %d" % (self.item_key[self.index][i], 
									self.item.weapon_price[self.item_key[self.index][i]], t,
									self.item.weapon_offense[self.item_key[self.index][i]])
			
			elif self.index == 1:
				if i==0 or i==3 or i==4:
					result += l + "\t%s:\t\tGold: %d\t\t%s: %d" % (self.item_key[self.index][i], 
									self.item.armor_price[self.item_key[self.index][i]], t,
									self.item.armor_defense[self.item_key[self.index][i]])
				else:
					result += l + "\t%s:\tGold: %d\t\t%s: %d" % (self.item_key[self.index][i], 
									self.item.armor_price[self.item_key[self.index][i]], t,
									self.item.armor_defense[self.item_key[self.index][i]])
			elif self.index == 2:
				if i==0:
					result += l + "\t%s:\t\tGold: %d" % (self.item_key[self.index][i],
									self.item.misc_price[self.item_key[self.index][i]])
				else:
					result += l + "\t%s:\tGold: %d" % (self.item_key[self.index][i],
									self.item.misc_price[self.item_key[self.index][i]])
				
			if i != len(self.item_key[self.index]) - 1:
				result += "\n"
			elif i == len(self.item_key[self.index]) - 1:
				result += "\n" + next
		
		return result
