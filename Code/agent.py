class Agent(object):
	"""
	Agent Class

	This class is father of all game objects
	Everything that the game will show is an Agent and have their own x, y and graphics.

	Attributes:
		x: int, sets the x position.
		y: int, sets the y position.
		gfx: list of sprites.
	"""
	def __init__(self):
		"""
		Initialize self.

		Set the default values for the attributes.
		"""
		super(Agent, self).__init__()		

		self.x = 0
		self.y = 0
		self.gfx = []