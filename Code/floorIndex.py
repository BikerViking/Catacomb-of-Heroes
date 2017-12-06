import structure

class FloorIndex(object):
	"""
	Class that make floors objects.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(FloorIndex, self).__init__()
	
	@staticmethod
	def makeFloor():
		"""
		Static Method!

		Makes all floor objects of the game.

		Returns:
			List: List of structure.
		"""
		testFloor = structure.Structure() 
		# Here will be filled with all floors used by the game
		
		List = []
		List.append(testFloor) 
		# And here is where it will append it to a list

		return List