import dText
import dObjects
import dMap
import dMenu

class Draw(object):

	"""
	Draw class is a "hub" class for all the other draw classes.

	Attributes:
		Text: Object that draws text on the surface.
		Objects: Object that draws game Objects on the surface.
		Map: Object that draws game map on the surface.
		Menu: Object that draws menu on the surface.
	"""

	def __init__(self, T_sprRes, T_winRes):
		"""
		Instantiate the main draw classes.

		Args:
			T_sprRes: an int tuple that contains the game's main sprite resolution.
			T_winRes: an int tuple that cointais the screen resolution.
		"""
		super(Draw, self).__init__()

		self.Text = dText.Text()
		self.Objects = dObjects.Objects(T_sprRes)
		self.Map = dMap.Map(T_sprRes, T_winRes)
		self.Menu = dMenu.Menu(T_winRes)