import agent

class Creature(agent.Agent):
	"""
	Creature class

	Everything that can walk, do/take damage and die, it's a creature.
	
	@ TODO:
	A lot of things.

	Attributes:
		hp: int, sets the hit points the creature.
	"""
	def __init__(self):
		super(Creature, self).__init__()

		self.hp = 0