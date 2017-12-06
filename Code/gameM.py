import copy

import modelMenu
import generate

class GameModel(object):
	"""
	Fist of all, sorry, this class it's a mess.
	I'll clean this up once I finish game controll fowarding control code.
	So, as is now, there's no point for commenting right now. This class will have big changes.
	"""
	def __init__(self, Assets):
		super(GameModel, self).__init__()
			
		self.done = False
		self.nextID = 1

		self.generate = generate.Generate()		

		self.modelMenu = modelMenu.ModelMenu(self.setDone)

		self.inventoryFlag = False
		self.targetFlag = False

		self.level = 0
		self.mapList = [self.generate.generateMap((32, 32), (512, 448))]
		self.creatureList = []

		self.copyHero = Assets.getAsset(2, 0)

		self.hero = None

	def setDone(self, nextID, done):
		self.nextID = nextID
		self.done = done

	def setMenu(self, menuFlag):
		self.menuFlag = menuFlag

	def setMenuID(self, Flag):
		if Flag:
			self.menuID += self.menuID
		else:
			self.menuID -= self.menuID

	def getMenuID(self):
		return self.menuID

	def getMap(self):
		return self.mapList[self.level]

	def makeHero(self):
		self.hero = copy.copy(self.copyHero)
		self.hero.x = 10
		self.hero.y = 10