class ControlHero(object):
	"""
	Controls the hero.
	"""
	def __init__(self):
		super(ControlHero, self).__init__()
	
	def setDir(self, key):
		"""	
		Sets hero direction.

		Args:
			Key: int from Input class

		Returns:
			int, tuple with the direction that hero must move.
		"""
		if key == 1:
			return (0, -1)
		if key == 2:
			return (0, 1)
		if key == 3:
			return (-1, 0)
		if key == 4:
			return (1, 0)

		if key == 5:
			return (-1, -1)
		if key == 6:
			return (1, -1)
		if key == 7:
			return(-1, 1)
		if key == 8:
			return (1, 1)