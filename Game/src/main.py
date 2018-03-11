import core.window.maker 		as Window
import core.input.handler 		as Control
import manager.state_manager 	as Manager

class Main(object):
	"""
	This class will 'boot up' the basics systems of the game.

	Attributes:
		window:		Package, manages game window.
		sound: 		Package, manages game sound.
		control: 	Package, manages game input.
		manager:	Package, manages the game.
	"""

	def __init__(self):
		"""
		Initialize Main.

		When this class is instantiated it will set the basic systems and then 
		run the Manager's Game loop.
		"""

		super(Main, self).__init__()

		# Window
		self.__window 		= Window.Maker()

		# TODO Sound
		self.__sound 		= None

		# Input
		self.__control 		= Control.Handler()

		# Manager
		self.__game 	 	= Manager.StateManager(self.__window, self.__sound, self.__control)

	def _game_loop(self):
		"""
		TODO Comments
		"""

		while(True):
			self.__game.run(self.__window, self.__sound, self.__control)
			self.__window.update_fps()

# Magic is done here:
if __name__ == "__main__":
	Main()._game_loop()