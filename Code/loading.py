import loadingM
import loadingC
import loadingV

class loadingMVC(object):
	"""
	Manages all loading classes.

	Attributes:
		done: boolean that tells if this state is over.
		nextId: int that defines what State should run next.
		loadM: Loading Model Class.
		loadV: Loading view Class.
		loadC: Loading Controller Class.
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
		super(loadingMVC, self).__init__()

		self.Window = Window
		self.assets = Assets
		self.draw = Draw

		self.done = False
		self.nextID = nextID

		self.loadM = loadingM.loadingModel()
		self.loadV = loadingV.loadingView(Window)
		self.loadC = loadingC.loadingController()

	def runLogic(self, Input):
		"""
		Runs this state's logic

		By running controller's function this method is able to run the logic from loading state.
		After that it updates if the state is done and what should be the next id.

		Args:
			Input: Input MC Class.
		"""
		self.loadC.loadStuff(self.loadM, self.assets, self.Window.T_sprRes)
		
		self.done = self.loadM.done
		if self.done:
			self.nextID = self.loadM.nextID

	def drawGame(self):
		"""
		Draws this state.

		By running viewer's function this method is able to draw this state's screen.

		Returns:
			pygame surface.
		"""
		return self.loadV.draw(self.loadM, self.assets, self.draw)

	def resetValues(self):
		"""
		Reset values from this State.
		"""
		self.done = False
		self.loadM.done = False

		self.loadV.resetValues()