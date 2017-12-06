import pygame
from ast import literal_eval as make_tuple

class windowModel(object):
	"""
	This class is responsible for modeling the window.
	"""

	def __init__(self):
		"""
		Game window needs to have their clock and FPS rate. 
		Since this values won't change by any options inside the game they are set when this class is made.
		"""
		super(windowModel, self).__init__()

		self.clock = pygame.time.Clock()
		self.fps = 25

	def defaultValues(self):
		"""
		This method hold all default data from the game's window
		"""

		'''
		The ideia is to have multiple modifiers for the game/window name.
		So, game starts by the simple name of Catacombs. As heroes die on the catacomb, 
		name will change based on player's performance.

		It starts as just Catacombs, and then evolves to Catacombs of Newbs or something.
		But when you start of doind epic stuff on the game, it will end as Catacombs of Heroes. 
		Players should realize that the dungeon is actually the catacombs of his dead heroes.

		And this should blow his mind.
		'''
		self.winName = "Catacombs"
		#icon = TODO
		
		# Resolutions:
		self.fullScreen = 0
		self.windowHeight = 512
		self.windowWidth = 448
		self.T_winRes = (self.windowHeight, self.windowWidth) # "T_" it's my way to make tuples more visible when codding.
		self.T_sprRes = (32, 32)

		# Base color
		self.T_baseColor = (188, 235, 234)

	def loadValues(self):
		"""
		Loads values for Model.

		This method loads the values of the screen from a file.dat
		"""

		file = open("opt.dat", 'r')

		self.winName = file.readline()[:-2]
		# self.icon = TODO
		
		# Resolutions.
		self.fullScreen = int(file.readline())
		self.windowHeight = int(file.readline())
		self.windowWidth = int(file.readline())
		self.T_winRes = (self.windowHeight, self.windowWidth) 
		self.T_sprRes = make_tuple(file.readline())

		# Base color
		self.T_baseColor = make_tuple(file.readline())

		file.close()