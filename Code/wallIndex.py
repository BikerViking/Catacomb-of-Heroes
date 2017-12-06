import structure

class WallIndex(object):
	"""
	Class that make wall objects.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(WallIndex, self).__init__()
	
	@staticmethod
	def makeWall():
		"""
		Static Method!
		
		Makes all wall objects of the game.

		Returns:
			List: List of structure.
		"""

		# Same as floorIndex, this makes a structure. But giving it a True arg makes it a wall.
		testWall = structure.Structure(True) 
		# Here will be filled with all walls used by the game

		List = []
		List.append(testWall)
		# And here is where it will append it to a list

		return List