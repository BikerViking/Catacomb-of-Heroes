import genMap

class Generate(object):
	"""docstring for Generate"""
	def __init__(self):
		super(Generate, self).__init__()
		self.seed = 0
		self.genMap = genMap.GenMap()
		# Generate Itens
			# Which Itens and their position
		# Generate Monsters
			# Which Monsters and their position


	def setSeed(self):
		self.seed = 1

	def generateMap(self, T_sprRes, T_winRes):
		return self.genMap.genMap(T_sprRes, T_winRes)