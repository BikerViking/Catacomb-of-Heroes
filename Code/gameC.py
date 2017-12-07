import copy

import structure
import controlMenu
import controlCreature
import controlHero

class GameController(object):
	"""
	Controller class for Game.

	Attributes:
		controlMenu: Class that controls the modelMenu inside Game Model Class
		controlCreature: Class that controls creatures
		controlHero: Class that controls Hero
	"""
	def __init__(self, Model, T_sprRes, T_winRes):
		"""
		Initialize self.
		
		Args:
			Model: Game Model Class
			T_sprRes: int Tuple with the base sprite resolution.
			T_winRes: int Tuple with the window resolution.
		"""

		super(GameController, self).__init__()

		self.Model = Model
		self.T_sprRes = T_sprRes
		self.T_winRes = T_winRes

		self.controlMenu = controlMenu.ControlMenu(self.Model.modelMenu)

		self.controlCreature = controlCreature.ControlCreature()
		self.controlHero = controlHero.ControlHero()


	def gameLogic(self, Input):

		"""
		Runs the game logic.

		Here is where the magic happens. This method will run the game's logic.

		@TODO
		A lot of things. I'm currently working on fowarding the inputs to diffrent controllers
		the Model.makeHero() is here intentionally, 'cuz I'm just testing input interactions.
		Once this is done I'll clean code and continue to add things to this logic to handle
		such as using itens, control monsters, etc.

		Args:
			Input: Input class.
		"""

		# LOGIC

		# GET INPUT AND DECIDE WHAT TO DO WITH IT;
			# INPUTS CAN HANDLE MENU SCREEN, INVENTORY SCREEN, TARGET AND THE PLAYER
		# IF, AND I SAID, IF player acted: 
		# (moved, attacked, used item, shot a spell or equiped a piece of gear) and 
		# his initiative score is 0 or below 0 
		self.Model.makeHero()

		key = Input.handle()
		
		if not key == None:
			if self.Model.modelMenu.isOpen:
				self.controlMenu.NavigateMenu(key)
			
			elif self.Model.inventoryFlag:
				#NavigateInventory(key)
				pass

			elif self.Model.targetFlag:
				# controlTarget(key)
				pass
			else:
				self.controlCreature.moveOrAttack(self.Model.getMap(), self.Model.hero, self.Model.creatureList, self.controlHero.setDir(key))

		if key == 0 and not self.Model.modelMenu.isOpen:
			self.Model.inventoryFlag = not self.Model.inventoryFlag
		elif key == -1 or (key == 0 and self.Model.modelMenu.isOpen):
			self.Model.modelMenu.isOpen = not self.Model.modelMenu.isOpen


		# THEN MONSTERS CAN ACT.
			# if a monster has a patrol = true, it will act every turn.
			# if not, monster can only act if the hero sees them.

			# picture this, a skeleton is not a patrol kinda of monster. So he'll just relax in his confy cold coffin, chillin' ya know?
			# Bats and Rats however, their're the type of monster that likes to roam the place. So they'll have True on patrol.

			# Some fallen heroes that became monsters will have a diffrent logic. If, somehow, I can do it, some fallen heroes would set patrol on or have his own room to a epic battle and tresoures.

