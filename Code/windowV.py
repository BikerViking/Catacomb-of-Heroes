import pygame
from pygame import font

class windowView(object):
	"""
	This class is responsible for displaying the window.
	"""
	def __init__(self):
		"""
		Initialize self.

		As a simple View class this class will get information from the Model Class to make the window.
		"""
		super(windowView, self).__init__()

	def makeScreen(self, winName, fullScreen, T_winRes, T_baseColor):
		"""
		This method makes the screen.

		After the initialization of pygame, the args values are used to make the window.

		Args:
		winName: String that will be displayed at the window.
		fullScreen: A boolean that indicates if the game window should be displayed in full screen or not.
		T_winRes: Tuple that contains the window resolution
		T_baseColor: Tuple that contains a color for the window.
		"""

		pygame.init() # Init pygame

		if fullScreen:
			pygame.display.toggle_fullscreen()

		pygame.display.set_caption(winName) # Sets the game window name.

		# Creates a base surface pygame object for the window. 
		# This is the base layer of the game, everything is drawn on top of this surface.
		self.baseSurface = pygame.display.set_mode(T_winRes) # this surface size is the same as the window resolution
		self.baseSurface.fill(T_baseColor) # Sets the color for this base surface.

	def updateView(self, clock, fps):
		"""
		Updates the game window code.

		This update is done via pygame functions.

		Args:
		clock: pygame object that helps to track time
		fps: an int that sets the how the frames per second rate for the game.
		"""
		pygame.display.flip()
		pygame.display.update()
		clock.tick(fps)