
class Map(object):
	def __init__(self):
		self.rows = 12
		self.columns = 61 
		self.row = 1
		self.column = 1
		self.traverse = ""
		self.in_town = False
		
		self.land = []
		self.initial_build()

		
	def move(self):
		self.land[self.row][self.column] = " "
		
		if self.traverse == "up":
			self.row -= 1
		elif self.traverse == "down":
			self.row += 1
		elif self.traverse == "left":
			self.column -= 1
		elif self.traverse == "right":
			self.column += 1
		
		self.traverse = ""
		self.land[self.row][self.column] = "i"
		
	def destination(self):
		if self.row == 0 and self.column == 0:
			return "village"
		elif self.row == self.rows - 1 and self.column == self.columns - 1:
			return "dragons lair"
		else:
			return None
			
			# Statistics to determine if an enemy is encounterd
		
	def display(self):
		result = ""
		self.static_items()
		for row in range(0, len(self.land)):
			result += " ".join(self.land[row])
			if row != len(self.land) - 1:
				result += "\n"
		return result
		
	def initial_build(self):
		for x in range(0,self.rows):
			self.land.append([" "] * self.columns) 
		self.static_items()
		self.move()
		
	def static_items(self):
		self.land[self.rows - 1][self.columns - 1] = "!"
		self.land[0][0] = ":"
		
	def town(self, action, level):
		if action == "enter":
			self.row = 2
			self.in_town = True
			potion_price = 15+(level*5)
			self.land = [["    Weapons For Sale\n", "    Bambo Pole\tOffense: +2\tGold: 10", "    Club\t\tOffense: +4\tGold: 60",
						"    Copper Sword\tOffense: +10\tGold: 180", "    Hand Axe\tOffense: +15\tGold: 560",
						"    Broad Sword\tOffense: +20\tGold: 1500", "    Flame Sword\tOffense: +28\tGold: 9800",
						"    Enchanted Sword\tOffense: +40\tGold: 15000", "    Next"],["    Armor For Sale\n", "    Previous",
						"    Clothes\t\tDefense: +2\tGold: 20", "    Leather Armor\tDefense: +4\tGold: 70", "    Chain Mail\tDefense: +10\tGold: 300",
						"    Half Plate\tDefense: +16\tGold: 1000", "    Full Plate\tDefense: +24\tGold: 3000", "    Enchanted Armor\tDefense: +28\tGold: 7500",
						 "    Next"], ["    Other Items For Sale\n", "    Previous", "    Wings\t\tGold: 25", "    Healing Potion\tGold: %d" % potion_price]] 
		elif action == "exit":
			self.row = 1
			self.column = 1
			self.land = []
			self.initial_build()
			self.in_town = False
			
	def display_town(self, move_cursor):
		twn = ""
		for line in range(0, len(self.land[1])):
			twn += self.land[1][line] + "\n"
		return twn
		
	def town_move(self):
		twn = ""
		for line in range(0, len(self.land[1])):
			if line == self.column:
				twn += ">" + self.land[1][line][1:] + "\n"
			else:
				twn += self.land[1][line] + "\n"
		return twn
		
			