import pygame

class loadingView(object):

	"""
	View class for loading.

	Attributes:
		fps: int that coordinates the animation of this state.
		T_winRes: int tuple screen resolution.
		color: int Tuple of three values.
		text: String that will be drawn on screen.
		count: int that counts how many frames have passed.
		flag: boolean that reset count.
	"""

	def __init__(self, Window):
		"""
		Initialize self.

		Args:
			Window: Window Model class used for set some attributes values.
		"""
		super(loadingView, self).__init__()

		self.fps = Window.fps/4
		self.T_winRes = Window.T_winRes
		self.color = (0, 0, 0)

		self.resetValues()

	def resetValues(self):
		"""
		Reset View Values to it's default.
		"""

		self.text = "LOADING "
		
		self.count = 0

		self.flag = True

	def draw(self, Model, Assets, Draw):
		"""
		Draws this state Screen.

		Args:
			Model: Loading Model Class.
			Assets: Assets Class.
			Draw: Draw Class.

		Returns:
			loadSurface: pygame Surface
		"""
		loadSurface = pygame.Surface(self.T_winRes) # Makes a Surface using window size.
		loadSurface.fill(self.color) # Fill it with the color.

		self.loading(loadSurface, Model, Assets, Draw) # runs loading method.

		return loadSurface


	def loading(self, Surface, Model, Assets, Draw):

		"""
		Draws the loading animation.

		Args:
			Surface: pygame surface.
			Model: Loading Model Class.
			Assets: Assets Class.
			Draw: Draw Class.
		"""
		
		# Draw text on screen.
		Draw.Text.drawText(Surface, Assets.fonts.fonts[0], self.text, None, None, (5, self.T_winRes[1]-25))

		self.count += 1 # Count frames.
 
		if Model.done: # If Model is done

				self.text = "LOADING DONE!" # Change the text.


		else:
			# Animate the loading text.
			if (self.count == self.fps or self.count == self.fps*2 or self.count == self.fps*3): 
				# This will run 3 times for each if.
				if self.flag: # If flag:
					self.text += "." # Add this char on the text.
				else: # If not
					self.text = self.text[:-1] # Subtract this char.

			if self.count == self.fps*3: # When count is equal to fps*3:
				self.flag = not self.flag # Change the flag
				self.count = 0 # Reset count