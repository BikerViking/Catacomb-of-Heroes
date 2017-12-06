class ModelMenu(object):
	"""docstring for ModelMenu"""
	def __init__(self, setDone):
		super(ModelMenu, self).__init__()
		
		self.isOpen = False
		self.navi = 0

		self.setDone = setDone

	def toMainMenu(self):
		self.setDone(1, True)