import wx
import os
import terrain_3
import statistics_1
import entities_1
import town_2

class GameFrame(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(620,530))
		self.CreateStatusBar() # A Status bar in the bottom of the window
		
		# Set up the menu. 
		filemenu = wx.Menu()
		menuNew = filemenu.Append(wx.ID_NEW, "&New", " Opens a new game")
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Opens a saved game")
		menuSave = filemenu.Append(wx.ID_SAVE, "&Save", " Saves the game from this point")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Provides a background about this program")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT,"E&xit", " Close the program without saving")
		
		# Create the menubar.
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&Game") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content.
		self.Show(True)
		
		self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
	
	def OnNew(self, event):
		panel.new_game()
	
	def OnOpen(self, event):  #jump
		"""Open a file"""
		self.dirname = ''
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.txt", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			panel.load(f)
			f.close
			dlg.Destroy()

	def OnSave(self, event):
		self.dirname = ''
		dlg = wx.FileDialog(self, "Save your game", self.dirname, "", "*.txt", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'w')
			f.write(panel.get_game_string())
			f.close
			dlg.Destroy()
		
	def OnAbout(self, event):
		message = """
		Dragon Slayer was written as a learning game to reinforce the basic 
		concepts of Python, Object Orientated Programming, and GUI creation.
		Special thanks to the following tutorial websites who got me pointed
		in the right direction: codecademy.com, learnpythonthehardway.org, &
		wiki.wxpython.org
		
		Thanks,
		Ken Kite
		"""
		title = "About Dragon Slayer"
		dlg = wx.MessageDialog(self, message, title, wx.OK)
		dlg.ShowModal() # Show it
		dlg.Destroy() # finally destroy it when finished.
	
	def OnExit(self, event):
		self.Close(True)  # Close the frame.
		
class GamePanel(wx.Panel):
	
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		
		# create sizers
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		attributesSizer = wx.BoxSizer(wx.HORIZONTAL)
		txtSizer = wx.BoxSizer(wx.HORIZONTAL)
		controlSizer = wx.BoxSizer(wx.HORIZONTAL)
		
		gridTraits = wx.GridBagSizer(hgap=5, vgap=5)
		gridInventory = wx.GridBagSizer(hgap=4, vgap=4)
		movecontrolSizer = wx.BoxSizer(wx.VERTICAL)
		
		stompSizer = wx.BoxSizer(wx.VERTICAL)
		
		upmoveSizer = wx.BoxSizer(wx.HORIZONTAL)
		hmoveSizer = wx.BoxSizer(wx.HORIZONTAL)
		dnmoveSizer = wx.BoxSizer(wx.HORIZONTAL)
		
		misccontrolSizer = wx.BoxSizer(wx.VERTICAL)
		fightingcontrolSizer = wx.BoxSizer(wx.VERTICAL)
		
		# populate character properties grid
		self.lbllevel = wx.StaticText(self, label="Level: ")
		self.txtlevel = wx.TextCtrl(self, size=(-1,-1), style=wx.TE_READONLY)
		gridTraits.Add(self.lbllevel, pos=(0,0))
		gridTraits.Add(self.txtlevel, pos=(0,1))
		
		self.lblhealth = wx.StaticText(self, label="Health: ")
		self.txthealth = wx.TextCtrl(self, size=(-1,-1), style=wx.TE_READONLY)
		gridTraits.Add(self.lblhealth, pos=(1,0))
		gridTraits.Add(self.txthealth, pos=(1,1))
		
		self.lblexperience = wx.StaticText(self, label="Experience: ")
		self.txtexperience = wx.TextCtrl(self, size=(-1,-1), style=wx.TE_READONLY)
		gridTraits.Add(self.lblexperience, pos=(2,0))
		gridTraits.Add(self.txtexperience, pos=(2,1))
		
		self.lbloffense = wx.StaticText(self, label="Offense: ")
		self.txtoffense = wx.TextCtrl(self, size=(-1,-1), style=wx.TE_READONLY)
		gridTraits.Add(self.lbloffense, pos=(3,0))
		gridTraits.Add(self.txtoffense, pos=(3,1))
		
		self.lbldefense = wx.StaticText(self, label="Defense: ")
		self.txtdefense = wx.TextCtrl(self, size=(-1,-1), style=wx.TE_READONLY)
		gridTraits.Add(self.lbldefense, pos=(4,0))
		gridTraits.Add(self.txtdefense, pos=(4,1))
		
		self.lblagility = wx.StaticText(self, label="Agility: ")
		self.txtagility = wx.TextCtrl(self, size=(-1,-1), style=wx.TE_READONLY)
		gridTraits.Add(self.lblagility, pos=(5,0))
		gridTraits.Add(self.txtagility, pos=(5,1))
		
		attributesSizer.Add(gridTraits, 0, wx.ALIGN_LEFT, wx.ALL)
		# add a spacer to the sizers
		attributesSizer.Add((50,10))
		
		# populate character inventory grid
		self.lblgold = wx.StaticText(self, label="Gold: ")
		self.txtgold = wx.TextCtrl(self, size=(200,-1), style=wx.TE_READONLY)
		gridInventory.Add(self.lblgold, pos=(0,0))
		gridInventory.Add(self.txtgold, pos=(0,1))
		
		self.lblweapon = wx.StaticText(self, label="Weapon: ")
		self.txtweapon = wx.TextCtrl(self, size=(200,-1), style=wx.TE_READONLY)
		gridInventory.Add(self.lblweapon, pos=(1,0))
		gridInventory.Add(self.txtweapon, pos=(1,1))
		
		self.lblarmor = wx.StaticText(self, label="Armor: ")
		self.txtarmor = wx.TextCtrl(self, size=(200,-1), style=wx.TE_READONLY)
		gridInventory.Add(self.lblarmor, pos=(2,0))
		gridInventory.Add(self.txtarmor, pos=(2,1))
		
		self.lblhealing = wx.StaticText(self, label="Healing Potion: ")
		self.txthealing = wx.TextCtrl(self, size=(200,-1), style=wx.TE_READONLY)
		gridInventory.Add(self.lblhealing, pos=(3,0))
		gridInventory.Add(self.txthealing, pos=(3,1))
		
		self.lblwings = wx.StaticText(self, label="Wings: ")
		self.txtwings = wx.TextCtrl(self, size=(200,-1), style=wx.TE_READONLY)
		gridInventory.Add(self.lblwings, pos=(4,0))
		gridInventory.Add(self.txtwings, pos=(4,1))
		
		attributesSizer.Add(gridInventory, 0, wx.ALIGN_LEFT, wx.ALL)
		
		
		# create 2 multiline TextCtrls - One will be the map output the other the game output dialogue
		self.map = wx.TextCtrl(self, size=(400,200), style=wx.TE_MULTILINE | wx.TE_READONLY)
		self.output = wx.TextCtrl(self, size=(200,200), style=wx.TE_MULTILINE | wx.TE_READONLY)
		txtSizer.Add(self.map)
		txtSizer.Add(self.output)
		
		# add stomp checkbox
		self.stomp = wx.CheckBox(self, label=" Stomp to attract enemy")
		self.Bind(wx.EVT_CHECKBOX, self.OnStompCheck, self.stomp)
		stompSizer.Add((20,30))
		stompSizer.Add(self.stomp)
		
		
		# add movement buttons
		self.up = wx.Button(self, label = "Up")
		self.left = wx.Button(self, label = "Left")
		self.right = wx.Button(self, label = "Right")
		self.down = wx.Button(self, label = "Down")
		
		self.Bind(wx.EVT_BUTTON, self.OnUpClick, self.up)
		self.Bind(wx.EVT_BUTTON, self.OnLeftClick, self.left)
		self.Bind(wx.EVT_BUTTON, self.OnRightClick, self.right)
		self.Bind(wx.EVT_BUTTON, self.OnDownClick, self.down)
		
		upmoveSizer.Add((45,20))
		upmoveSizer.Add(self.up)
		hmoveSizer.Add(self.left)
		hmoveSizer.Add(self.right)
		dnmoveSizer.Add((45,20))
		dnmoveSizer.Add(self.down)
		
		movecontrolSizer.Add(upmoveSizer)
		movecontrolSizer.Add(hmoveSizer)
		movecontrolSizer.Add(dnmoveSizer)
		
		# add miscellaneous buttons
		self.wings = wx.Button(self, label = "Wings")
		self.potion = wx.Button(self, label = "Potion")
		
		self.Bind(wx.EVT_BUTTON, self.OnWingsClick, self.wings)
		self.Bind(wx.EVT_BUTTON, self.OnPotionClick, self.potion)
		
		misccontrolSizer.Add((20,15))
		misccontrolSizer.Add(self.wings)
		misccontrolSizer.Add(self.potion)
		
		# add fighting buttons
		self.attack = wx.Button(self, label = "Attack")
		self.flee = wx.Button(self, label = "Flee")
		
		self.Bind(wx.EVT_BUTTON, self.OnAttackClick, self.attack)
		self.Bind(wx.EVT_BUTTON, self.OnFleeClick, self.flee)
		
		fightingcontrolSizer.Add((20,15))
		fightingcontrolSizer.Add(self.attack)
		fightingcontrolSizer.Add(self.flee)
		
		controlSizer.Add(stompSizer)
		controlSizer.Add((20,20))
		controlSizer.Add(movecontrolSizer)
		controlSizer.Add((20,20))
		controlSizer.Add(misccontrolSizer)
		controlSizer.Add((20,20))
		controlSizer.Add(fightingcontrolSizer)
		
		mainSizer.Add(attributesSizer, 0, wx.CENTER, wx.ALL)
		mainSizer.Add(txtSizer, 0, wx.CENTER, wx.ALL)
		mainSizer.Add(controlSizer, 0, wx.CENTER, wx.ALL)
		self.SetSizerAndFit(mainSizer)
		
		self.Market = town_2.Bazaar()
		self.Realm = terrain_3.Map()
		self.update_map()
		self.Hero = entities_1.DragonSlayer()
		self.update_attributes_inventory()
		self.Enemy = None
		self.battle_controls("disable")
		self.calc_healing_price()
	
	def OnStompCheck(self, event):
		pass
		
	def OnUpClick(self, event): 
		if self.Market.present == True:
			# logic that determines which index to switch to as a function of changing row number
			if self.Market.index == 0 and self.Realm.row == 2:
				event.Skip()
			elif self.Market.index == 1 and self.Realm.row == 2:
				self.Market.index -= 1
				self.Realm.row = 8
				self.update_map()
			elif self.Market.index == 2 and self.Realm.row == 2:
				self.Market.index -= 1
				self.Realm.row = 7
				self.update_map()
			else:
				self.Realm.row -= 1
				self.update_map()
		elif self.Realm.row == 0:
			event.Skip()
		else:
			self.Realm.traverse = "up"
			self.travel()
			
	def OnLeftClick(self, event):
		if self.Market.present == True:
			pass
			#leave town
			self.moving_controls("exit town")
			self.Realm.row = 1
			self.Realm.column = 1
			self.Realm.move()
			self.update_map()
			self.update_output("append", "\nYou left the village.\n")
		elif self.Realm.column == 0:
			event.Skip()
		else:
			self.Realm.traverse = "left"
			self.travel()
			
	def OnRightClick(self, event):
		if self.Realm.column == self.Realm.columns - 1:
			event.Skip()
		elif self.Market.present == True:
			name, price, battle_attributes = self.Market.selected_item(self.Realm.row)
			if price > self.Hero.gold:
				self.update_output("append", "\nGet the fuck out of here you broke ass mother fucker.\n")
			else:
				self.purchase(name, price, battle_attributes)
		else:
			self.Realm.traverse = "right"
			self.travel()
			
	def OnDownClick(self, event):
		if self.Market.present == True:
			# logic that determines which index to switch to as a function of changing row number
			if self.Market.index == 2 and self.Realm.row == 3:
				event.Skip()
			elif self.Market.index == 1 and self.Realm.row == 7:
				self.Market.index += 1
				self.Realm.row = 2
				self.update_map()
			elif self.Market.index == 0  and self.Realm.row == 8:
				self.Market.index += 1
				self.Realm.row = 2
				self.update_map()
			else:
				self.Realm.row += 1
				self.update_map()
			
		elif self.Realm.row == self.Realm.rows - 1:
			event.Skip()
		else:
			self.Realm.traverse = "down"
			self.travel()

	def update_output(self, action, message):
		if action == "clear":
			self.output.Clear()
		elif action == "append":
			self.output.AppendText(message)
	
	def OnWingsClick(self, event):
		if self.Hero.wings < 1:
			self.update_output("append", "\nYou have no wings.\nYou'll have to walk home.\n")
		else:
			self.update_output("append", "\nYou spread your wings and fly home.\n")
			self.Realm.land[self.Realm.row][self.Realm.column] = " "
			self.Realm.row = 1
			self.Realm.column = 1
			self.Realm.move()
			self.update_map()
			self.Hero.wings -= 1
			self.update_attributes_inventory()
		
	def OnPotionClick(self, event):
		if self.Hero.healing > 0:
			self.Hero.healing -= 1
			self.Hero.hp = self.Hero.max_hp
			self.update_attributes_inventory()
		else:
			self.update_output("append", "\nYou don't have any healing potions.\nLooks like you're fucked.\n")
	def OnAttackClick(self, event):
		#You attack the enemy
		
		if statistics_1.hit_flee_success(self.Hero.agility, self.Enemy.agility):
			damage = statistics_1.damage(self.Hero.offense, self.Enemy.defense)
			self.update_output("append", "\nYour attack connected.\nYou've inflicted damage of\n%d to the %s.\n" %(damage, self.Enemy.name))
			self.Enemy.hp -= damage
		else:
			self.update_output("append", "\nSHIT BALLS!!!\nYou Missed and only pissed him off.\n")
		
		self.enemy_attack()
	
	def enemy_attack(self):
		#If the enemy is still alive he attacks you
		if self.Enemy.alive(self.Enemy.hp):
			if statistics_1.hit_flee_success(self.Enemy.agility,self.Hero.agility):
				damage = statistics_1.damage(self.Enemy.defense, self.Hero.offense)
				self.update_output("append", "\nThe %s hit you.\nYou've taken damage of %d.\n" %(self.Enemy.name, damage))
				self.Hero.hp -= damage
				self.update_attributes_inventory()
				if not(self.Hero.alive(self.Hero.hp)):
					self.hero_defeated()
			else:
				self.update_output("append", "\nThe %s missed you.\n" % self.Enemy.name)
		else:
			self.enemy_defeated()
			
	def enemy_defeated(self):
		self.update_output("append", "\nYou have killed the %s\n" % self.Enemy.name)
		self.update_output("append", "\nYour prize is %d gold &\n%d experience points.\n" % (self.Enemy.gold, self.Enemy.xp))
		self.Hero.gold += self.Enemy.gold
		self.Hero.experience += self.Enemy.xp
		if self.Hero.lvl_chk():
				self.update_output("append", "\nYou've vanquished enough enemies to level up.\nYou grow stronger.\n")
				self.calc_healing_price()
		self.update_attributes_inventory()
		self.moving_controls("enable")
		self.battle_controls("disable")
		if self.Enemy.name == "Dragon":
			self.Victory()
		
	def Victory(self):
		self.update_output("append", "\nCongratulations you have defeated all who came before you and now you have semen on your shoes.")
		self.moving_controls("disable")
		
	def hero_defeated(self):
		self.update_output("append", "\n\nThe fucking %s killed you.\n\n\nYou dead bitch!!\n" % self.Enemy.name)
		self.battle_controls("disable")
	
	def calc_healing_price(self):
		self.Market.item.misc_price["Healing Potion"] = 15 + (self.Hero.level * 5)
	
	def OnFleeClick(self, event):
		if statistics_1.hit_flee_success(self.Hero.agility, self.Enemy.agility):
			self.update_output("append", "\nYou successfully evaded the %s.\n" % self.Enemy.name)
			self.moving_controls("enable")
			self.battle_controls("disable")
		else:
			self.update_output("append", "\nYou failed to evade the %s.\n" % self.Enemy.name)
			self.enemy_attack()
			
	def update_map(self):
		self.map.Clear()
		if self.Market.present == False:
			self.map.AppendText(self.Realm.display())
		elif self.Market.present == True:
			self.map.AppendText(self.Market.build_menu(self.Realm.row))
		
	def moving_controls(self, state):
		if state == "enable":
			self.up.Enable()
			self.left.Enable()
			self.right.Enable()
			self.down.Enable()
			self.wings.Enable()
			self.potion.Enable()
		elif state == "disable":
			self.up.Disable()
			self.left.Disable()
			self.right.Disable()
			self.down.Disable()
			self.wings.Disable()
			self.potion.Disable()
		elif state == "enter town":
			self.wings.Disable()
			self.potion.Disable()
			self.left.SetLabel("Exit")
			self.right.SetLabel("Select")
			self.Market.present = True
		elif state == "exit town":
			self.wings.Enable()
			self.potion.Enable()
			self.left.SetLabel("Left")
			self.right.SetLabel("Right")
			self.Market.present = False
	def battle_controls(self, state):
		if state == "enable":
			self.attack.Enable()
			self.flee.Enable()
		elif state == "disable":
			self.attack.Disable()
			self.flee.Disable()
	
	def purchase(self, item, price, battle_attributes): 
		if self.Market.index == 0:
			self.update_output("append", "\nYou just purchased a %s.\nNice weapon upgrade.\nGo and fuck some shit up.\n" % item)
			if self.Hero.weapon != "Unarmed":
				old_price, old_off = self.Market.get_weapon(self.Hero.weapon)
				self.Hero.offense -= old_off
			self.Hero.weapon = item
			self.Hero.offense += battle_attributes
			
		if self.Market.index == 1:
			self.update_output("append", "\nYou just purchased %s.\nNow you will laugh at your enemies attacks.\n" % item)
			if self.Hero.armor != "Naked":
				old_price, old_def = self.Market.get_armor(self.Hero.armor)
				self.Hero.defense -= old_def
			self.Hero.armor = item
			self.Hero.defense += battle_attributes 
			
		if self.Market.index == 2:
			self.update_output("append", "\nYou just purchased %s.\nThis should assist you on your travels.\n" % item)
			if item == "Healing Potion":
				self.Hero.healing += 1
			elif item == "Wings":
				self.Hero.wings += 1
		
		self.Hero.gold -= price
		self.update_attributes_inventory()
		
	def travel(self):
		self.Realm.move()
		self.update_map()
		
		if self.Realm.destination() != None:
			self.update_output("clear", None)
			self.update_output("append", "\nYou have arrived at the %s.\n" % self.Realm.destination())
			if self.Realm.destination() == "village":
				self.moving_controls("enter town")
				self.Market.present = True
				self.Market.index = 0
				self.Realm.row = 2
				self.update_map()
			elif self.Realm.destination() == "dragons lair":
				self.moving_controls("disable")
				self.battle_controls("enable")
				self.Enemy = entities_1.Enemy(24)
				self.update_output("append", "\nYou've encountered a %s.\n" % self.Enemy.name)
		else:
			enemy_encountered, enemy_type = statistics_1.encounter_enemy(self.stomp.GetValue(),self.Realm.column)
			if enemy_encountered == True:
				self.moving_controls("disable")
				self.battle_controls("enable")
				self.Enemy = entities_1.Enemy(enemy_type)
				self.update_output("append", "\nYou've encountered a %s.\n" % self.Enemy.name)
	
	def load(self, file):  #jump
		
		for i in range(0,16):
			s = file.readline()
			
			if i==0:
				if str(s)[:len(str(s))-1] != "8902wjkjfa82390qu9943ksd":
					self.update_output("clear", None)
					self.update_output("append", "\nYou have loaded in invalid file.\n")
					break
				else:
					print "did we get here?"
					self.update_output("clear", None)
					self.map.Clear()
					self.Realm.land[self.Realm.row][self.Realm.column] = " "
			elif i==1:
				self.Hero.level = int(s)
			elif i==2:
				self.Hero.hp = int(s)
			elif i==3:
				self.Hero.max_hp = int(s)
			elif i==4:
				self.Hero.experience = int(s)
			elif i==5:
				self.Hero.offense = int(s)
			elif i==6:
				self.Hero.defense = int(s)
			elif i==7:
				self.Hero.agility = int(s)
			elif i==8:
				self.Hero.gold = int(s)
			elif i==9:
				self.Hero.weapon = str(s)[:len(str(s))-1]
			elif i==10:
				self.Hero.armor = str(s)[:len(str(s))-1]
			elif i==11:
				self.Hero.healing = int(s)
			elif i==12:
				self.Hero.wings = int(s)
			elif i==13:
				self.Realm.row = int(s)
			elif i==14:
				self.Realm.column = int(s)
			elif i==15:
				self.Market.present = self.string2bool(s)
	
				if self.Market.present == False:
					print "here too"
					self.Realm.land[1][1] = " "
					self.Realm.land[self.Realm.row][self.Realm.column] = "i"
				elif self.Market.present == True:	
					self.moving_controls("enter town")
					self.Market.index = 0
					self.Realm.row = 2
					
				self.update_map()
				self.update_attributes_inventory()
	
	def get_game_string(self):
		s = "8902wjkjfa82390qu9943ksd\n"
		s += str(self.Hero.level) + "\n"
		s += str(self.Hero.hp) + "\n"
		s += str(self.Hero.max_hp) + "\n"
		s += str(self.Hero.experience) + "\n"
		s += str(self.Hero.offense) + "\n"
		s += str(self.Hero.defense) + "\n"
		s += str(self.Hero.agility) + "\n"
		s += str(self.Hero.gold) + "\n"
		s += str(self.Hero.weapon) + "\n"
		s += str(self.Hero.armor) + "\n"
		s += str(self.Hero.healing) + "\n"
		s += str(self.Hero.wings) + "\n"
		s += str(self.Realm.row) + "\n"
		s += str(self.Realm.column) + "\n"
		s += str(self.Market.present)
		return s
	
	
	def new_game(self):
		self.update_output("clear", None)
		self.map.Clear()
		self.Realm.land[self.Realm.row][self.Realm.column] = " "
		
		self.Hero.level = 1
		self.Hero.hp = 30
		self.Hero.max_hp = 30
		self.Hero.experience = 0
		self.Hero.offense = 3
		self.Hero.defense = 3
		self.Hero.agility = 2
		self.Hero.gold = 50
		self.Hero.weapon = "Unarmed"
		self.Hero.armor = "Naked"
		self.Hero.healing = 0
		self.Hero.wings = 0
		self.Realm.row = 1
		self.Realm.column = 1
	
		self.Realm.land[self.Realm.row][self.Realm.column] = "i"
		self.update_map()
		self.update_attributes_inventory()
	
	def string2bool(self, v):
		if v == "True":
			return True
		elif v == "False":
			return False
	
	def update_attributes_inventory(self):
		self.txtlevel.Clear()
		self.txtlevel.AppendText(str(self.Hero.level))
		
		self.txthealth.Clear()
		self.txthealth.AppendText(str(self.Hero.hp))
		
		self.txtexperience.Clear()
		self.txtexperience.AppendText(str(self.Hero.experience))
		
		self.txtoffense.Clear()
		self.txtoffense.AppendText(str(self.Hero.offense))
		
		self.txtdefense.Clear()
		self.txtdefense.AppendText(str(self.Hero.defense))
		
		self.txtagility.Clear()
		self.txtagility.AppendText(str(self.Hero.agility))
		
		self.txtgold.Clear()
		self.txtgold.AppendText(str(self.Hero.gold))
		
		self.txtweapon.Clear()
		self.txtweapon.AppendText(self.Hero.weapon)
		
		self.txtarmor.Clear()
		self.txtarmor.AppendText(self.Hero.armor)
		
		self.txthealing.Clear()
		self.txthealing.AppendText(str(self.Hero.healing))
		
		self.txtwings.Clear()
		self.txtwings.AppendText(str(self.Hero.wings))
		
print "\n\n\n" + "Start" + "-" * 18 
		
app = wx.App(False)
frame = GameFrame(None, title="Dragon Slayer")
panel = GamePanel(frame)
frame.Show(True)
app.MainLoop()

print "END" + "-" * 20 + "\n\n\n"