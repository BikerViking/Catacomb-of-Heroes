class MainMenuM(object):
	"""
	Main Menu Model Class.

	Attributes:
		done: Boolean that controls if the state is over.
		nextID: int that calls the next State.
		select: int that defines what option from menu is currently selected.
	"""
	def __init__(self):
		super(MainMenuM, self).__init__()

		self.done = False
		self.nextID = 0
		self.select = 0
		
