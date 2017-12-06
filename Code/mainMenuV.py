import pygame

class MainMenuV(object):
	"""
	View Class for Main Menu

	Attributes:
		menu: String list with main menu options.
		notSelected: int tuple that holds the not selected color.
		color0: int tuple color for option 0.
		color1: int tuple color for option 1.
		color2: int tuple color for option 2.
		color3: int tuple color for option 3.
		color4: int tuple color for option 4.
	"""
	def __init__(self, Window):
		"""
		Initialize self.

		Args:
			Window: Window Model class used for set some attributes values.
		"""
		super(MainMenuV, self).__init__()

		self.menu = ["PLAY", "OPTIONS", "STATISTICS", "EXIT"]

		self.notSelected = (125, 125, 125)

		self.T_winRes = Window.T_winRes


	def setColors(self, select):
		"""
		Set the color of the options from menu.

		Args: 
			select: int that changes one color.
		"""
		self.color0 = self.notSelected
		self.color1 = self.notSelected
		self.color2 = self.notSelected
		self.color3 = self.notSelected

		if select == 0:
			self.color0 = None
		elif select == 1:
			self.color1 = None
		elif select == 2:
			self.color2 = None
		elif select == 3:
			self.color3 = None

	def draw(self, Model, Assets, Draw):
		"""
		Draws Main Menu on a surface.

		Args:
			Model: Main Menu Model Class.
			Assets: Assets Class.
			Draw: Draw Class.

		Returns:
			menuSurface: pygame Surface.
		"""

		menuSurface = pygame.Surface(self.T_winRes) # Makes a Surface using window size.
		menuSurface.fill((0,0,0)) # Fill it with a color.

		self.setColors(Model.select) # Change the one color value.

		# Draw options on the surface.
		Draw.Text.drawText(menuSurface, Assets.fonts.fonts[1], self.menu[0], self.color0, None, (5, self.T_winRes[1]/2+140))
		Draw.Text.drawText(menuSurface, Assets.fonts.fonts[1], self.menu[1], self.color1, None, (5, self.T_winRes[1]/2+160))
		Draw.Text.drawText(menuSurface, Assets.fonts.fonts[1], self.menu[2], self.color2, None, (5, self.T_winRes[1]/2+180))
		Draw.Text.drawText(menuSurface, Assets.fonts.fonts[1], self.menu[3], self.color3, None, (5, self.T_winRes[1]/2+200))

		return menuSurface