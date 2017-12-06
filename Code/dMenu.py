import pygame

class Menu(object):
	"""
	Draws ingame menu.
	"""
	def __init__(self, T_winRes):
		"""
		Initialize self.

		Args:
			T_winRes: int Tuple with the window resolution.
		"""
		super(Menu, self).__init__()
		
		self.T_winRes = T_winRes

	def drawMenu(self):
		"""
		Draws the menu on screen.

		Returns:
			menuSurface: pygame surface
		"""

		menuSurface = pygame.Surface((self.T_winRes[0]/4, self.T_winRes[1]/4))

		menuSurface.fill((0, 0, 0))

		return menuSurface
