class loadingModel(object):
	"""
	Model class for Loading.

	Attributes:
		done: boolean that tells if this state is over.
		nextId: int that defines what State should run next.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(loadingModel, self).__init__()

		self.done = False
		self.nextID = 1

	# Scrap code, could be useful someday.
		# self.percentage = 0
		# self.total = 0