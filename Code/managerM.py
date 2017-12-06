import loading
import mainMenu
import game

class managerModel(object):
	"""
	This is the Model class from the manager system.

	Attributes:
	load, menu, game, etc: game states.
	stateList: A list of game states.
	stateID: an int that will pick one of the game states from the stateList.
	"""
	def __init__(self, Window, Assets, Draw):
		"""
		Manager model needs to instantiate all game states and append them in a list.

		Args:
		Window: Window Class that hold useful data for the game states.
		Assets: Assets Class that hold all in game objects
		Draw: Draw Class that have all the draw methods to draw the game.
		"""
		super(managerModel, self).__init__()
		
		self.load = loading.loadingMVC(Window.windowM, Assets, Draw, 1)
		self.menu = mainMenu.MainMenuMVC(Window.windowM, Assets, Draw, 0)
		self.game = game.GameMVC(Window.windowM, Assets, Draw, 1)
		
		self.stateList = [self.load, self.menu, self.game]
		self.stateID = 0

	def getState(self):
		"""
		This method gets current state.

		Returns:
		Current game state.
		"""
		return self.stateList[self.stateID]
