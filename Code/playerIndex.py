import player

class PlayerIndex(object):
	"""
	Class that make the player objects.
	"""
	def __init__(self):
		"""
		Initialize self.		
		"""
		super(PlayerIndex, self).__init__()
	
	@staticmethod
	def makeHero():
		"""
		Static Method!

		Makes all player objects of the game.

		Returns:
			List: List of player.
		"""
		testHero = player.Hero()
		# Here will be filled with all floors used by the game

		List = []
		List.append(testHero)
		# And here is where it will append it to a list

		return List