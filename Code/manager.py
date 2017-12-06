import assets
import draw

import managerM
import managerC

class ManagerMC(object):

	"""
	Manages the Model and the Controller of the Manager system.

	Attributes:
		assets: Holds all game objects that will be used in the game.
		draw: Have all draw classes with their function to draw the game.
		managerM: Manager Model Class.
		managerC: Manager Control Class.
	"""

	def __init__(self, window):
		"""
		This method creates objects that are useful for all screens that it manages.

		Args:
			window: Window class holds important values that will be used by game screens
		"""
		super(ManagerMC, self).__init__()

		self.window = window

		self.assets = assets.Assets()
		self.draw = draw.Draw(self.window.windowM.T_sprRes, self.window.windowM.T_winRes)

		self.managerM = managerM.managerModel(self.window, self.assets, self.draw)
		self.managerC = managerC.managerController()


	def gameLoop(self):
		"""
		Runs the Manager Controller game loop.
		"""
		self.managerC.gameLoop(self.managerM, self.window.windowV.baseSurface, self.window.updateView)