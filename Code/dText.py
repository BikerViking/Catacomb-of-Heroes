class Text(object):
	"""
	This class handles drawing text on screen.

	Attributes:
		color: int tuple that sets the base text color.
		bgColor: int tuple that sets the base text background color.
	
	"""

	def __init__(self):
		"""
		Initialize self.

		It initialize it's attributes with default values.
		"""
		super(Text, self).__init__()

		self.color = (255, 255, 255)
		self.bgColor = (0, 0, 0)

	def textHandler(self, font, text, color = None, bgColor = None):
		"""
		Handle text to prepare it to draw.

		Args:
			font: pygame font object.
			text: string that will be drawn
			color(Optional): text color
			bgColor(Optional): background text color.

		Returns:
			textSurface: pygame surface.
		"""
		if color or bgColor:
			if color and bgColor:
				textSurface = font.render(text, False, color, bgColor) # text, antialias, color, backgroundColor. It converts it to a pygame surface.
			elif not bgColor:
				textSurface = font.render(text, False, color, self.bgColor)
			else:
				textSurface = font.render(text, False, self.color, bgColor)
		else:
			textSurface = font.render(text, False, self.color, self.bgColor)

		return textSurface

	def drawText(self, surface, font, text, color = None, bgColor = None, T_coord = None):
		"""
		Draws the text on a given surface at a given coordinate.

		Args:
			surface: pygame surface where the text will be drawn.
			font: pygame font of the text.
			text: String of the text.
			color(Optional): Color of the text.
			bgColor(Option): Background Color of the text.
			T_coord(Optional): int Tuple that defines where this text will be drawn.
		"""
		textSurface = self.textHandler(font, text, color, bgColor) # First of all, we need to handle the text.
		textRect = textSurface.get_rect() # Then we get it's rect size.

		if T_coord: # Then we set the top left coordinate of this surface
			textRect.topleft = T_coord
		else:
			textRect.topleft = (0, 0)

		surface.blit(textSurface, textRect) # And finally we can draw this text, which is now a surface, on the surface.
