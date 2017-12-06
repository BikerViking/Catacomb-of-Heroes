import window
import manager

class Core(object):
	""" 
	This class will start up all basic systems of the game.

	Attributes:
		Window: Hold window default data, makes the window and controlls it.
		Manager: This is the "Screen manager" of the game.
	"""
	def __init__(self):
		"""
		Initialize self.

		When this class is instantiated it will set the basic systems and then run the Manager Game loop
		"""
		super(Core, self).__init__()

		# Window
		self.window = window.windowMVC()

		# TODO Sound 

		# Manager
		self.manager = manager.ManagerMC(self.window)

		# The game loop.
		while True:

			self.manager.gameLoop()