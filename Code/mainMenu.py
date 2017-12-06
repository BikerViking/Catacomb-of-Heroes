import mainMenuM
import mainMenuV
import mainMenuC

class MainMenuMVC(object):

	"""
	Manages the Main Menu Classes.

	Attributes:
		done: boolean that tells if this state is over.
		nextId: int that defines what State should run next.
		mMM: Main Menu Model Class
		mMV: Main Menu View Class
		mMC: Main Menu Controller Class
	"""

	def __init__(self, Window, Assets, Draw, nextID):
		"""
		Initialize self.

		Sets the default values from this object.

		Args:
			Window: Window Model Class
			Assets: Assets Class:
			Draw: Draw Class
			nextID: Int, this should be removed soon.
		"""
		super(MainMenuMVC, self).__init__()
		
		self.Window = Window
		self.assets = Assets
		self.draw = Draw

		self.done = False
		self.nextID = nextID

		self.mMM = mainMenuM.MainMenuM()
		self.mMV = mainMenuV.MainMenuV(Window)
		self.mMC = mainMenuC.MainMenuC()

	def runLogic(self, Input):
		"""
		Runs this state's logic

		By running controller's function this method is able to run the logic from Main Menu state.
		After that it updates if the state is done and what should be the next id.

		Args:
			Input: Input MC Class.
		"""
		self.mMC.menu(self.mMM, Input)
		self.done = self.mMM.done
		if self.done:
			self.nextID = self.mMM.nextID

	def drawGame(self):
		"""
		Draws this state.

		By running viewer's function this method is able to draw this state's screen.
	
		Returns:
			pygame surface.
		"""
		return self.mMV.draw(self.mMM, self.assets, self.draw)

	def resetValues(self):
		"""
		Reset values from this State.
		"""
		self.done = False
		self.mMM.done = False
		self.mMM.select = 0