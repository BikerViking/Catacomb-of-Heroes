import gameM
import gameV
import gameC

class GameMVC(object):
	"""
	Manages all game classes

	Attribues:
		done: boolean that tells if this state is over.
		nextId: int that defines what State should run next.
		Model: Game Model Class.
		View: Game view Class.
		Controller: Game Controller Class.
	"""
	def __init__(self, Window, Assets, Draw, nextID):
		"""
		Initialize self.

		Args:
			Window: Window Model class.
			assets: Assets Class.
			draw: Draw Class:
			nextID(Temporary - I'll remove this later): int that defines what State should run next.

		"""
		super(GameMVC, self).__init__()
		
		self.Window = Window
		self.assets = Assets
		self.draw = Draw

		self.done = False
		self.nextID = nextID

		self.Model = gameM.GameModel(self.assets)
		self.View = gameV.GameView()
		self.Controller = gameC.GameController(self.Model, self.Window.T_sprRes, self.Window.T_winRes)

	def runLogic(self, Input):
		"""
		Runs this state's logic

		By running controller's function this method is able to run the logic from game state.
		After that it updates if the state is done and what should be the next id.

		Args:
			Input: Input MC Class.
		"""

		self.Controller.gameLogic(Input)
		self.done = self.Model.done
		if self.done:
			self.nextID = self.Model.nextID

	def drawGame(self):
		"""
		Draws this state.

		By running viewer's function this method is able to draw this state's screen.

		Returns:
			pygame surface.
		"""
		return self.View.draw(self.Model, self.assets, self.draw)

	def resetValues(self):
		"""
		Reset values from this State.
		"""
		self.done = False
		self.Model.done = False
		self.Model.modelMenu.isOpen = False