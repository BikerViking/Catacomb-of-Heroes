class Objects(object):
	"""
	Draws agents.
	"""
	def __init__(self, T_sprRes):
		"""
		Initialize self.

		Args:
			T_sprRes: int Tuple with the base sprite resolution.
		"""
		super(Objects, self).__init__()
		self.T_sprRes = T_sprRes

	def drawObjects(self, Surface, Agent, T_coord = None):
		"""
		Draws the agents on Surface.

		@TODO: Animation
		This class needs to ask if the Agent.gfx len is more that 1. 
		If it is, it needs to cicle through the Agent.gfx list and change the image that will be drawn.
		Since I'm working on the game's mechanics, this will be added later.
		It's not hard to do it, It is just not a prioty right now. 

		Args:
			Surface: pygame surface
			Agent: Agent Object
			T_coord(Optional): int Tuple with two values that will be used as coordinates.
		"""

		# if len(Agent.gfx) == 1:
		if T_coord:
			Surface.blit(Agent.gfx[0], (T_coord[0]*self.T_sprRes[0], T_coord[1]*self.T_sprRes[1]))
			
		else:	
			Surface.blit(Agent.gfx[0], (Agent.x*self.T_sprRes[0], Agent.y*self.T_sprRes[1]))
		# else:

