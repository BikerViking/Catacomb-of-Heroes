class Structure(object):
	"""docstring for Structure"""
	def __init__(self, isWall = None):
		super(Structure, self).__init__()

		if isWall:
			self.isWall = isWall
		else: 
			self.isWall = False

		self.gfx = []
		self.explored = True