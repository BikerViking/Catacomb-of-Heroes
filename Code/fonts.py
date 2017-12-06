import pygame
from pygame import font

class Fonts(object):
	"""
	This class loads and appends the game fonts in a list.

	Attributes:
		fonts: List of game fonts
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(Fonts, self).__init__()

		self.fonts = self.loadFonts()


	def loadFonts(self):
		"""	
		Load the game fonts.

		This method loads the game fonts from assets folder and uses pygame to do it.
		When fonts are loaded in variables, it appends on the list, then returns it.

		Returns:
			List of fonts.
		"""

		# Try/Except to make it work on windows machines.
		try:
			debug = pygame.font.Font("Assets/Font/Pixeled.ttf", 8) # Relative path, font size.
			msg = pygame.font.Font("Assets/Font/Pixeled.ttf", 8)
		except:
			debug = pygame.font.Font("Assets\Font\Pixeled.ttf", 8)
			msg = pygame.font.Font("Assets\Font\Pixeled.ttf", 8)

		fonts = []
		fonts.append(debug)
		fonts.append(msg)

		return fonts

