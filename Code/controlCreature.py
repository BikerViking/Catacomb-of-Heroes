class ControlCreature(object):
	"""
	Controls Creatures.

	This class will recieve creatures to be controlled by it.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(ControlCreature, self).__init__()
	
	def moveOrAttack(self, Map, Creature, CreatureList, T_Dir):
		"""
		Moves or Attacks with the Creature.

		Args:
			Map: structure matrix, this method needs to check things on the map.
			Creature: The creature that will move or attack.
			CreatureList: The creature list that are in this map.
			T_Dir: int, tuple, with two values that will be added to Creature's x and y.
		"""
		if not T_Dir == None: # Prevents error.

			# Checks if Creature is trying to move to a wall
			isWall = (Map[Creature.x+T_Dir[0]][Creature.y+T_Dir[1]].isWall == True) 

			# Checks if the Creature is trying to move to another creature.
			target = self.checkCreature(CreatureList, Creature.x+T_Dir[0], Creature.y+T_Dir[1], Creature)

			if target: # If Creature colides with another creature, it should attack it, but don't move.
				print("Attack")
			elif not isWall: # If there is nothing in Creature's way, move it.
				Creature.x += T_Dir[0] 
				Creature.y += T_Dir[1]

	def checkCreature(self, CreatureList, x, y, excludeCreature = None, excludeType = None):
		"""
		Checks for a Creature in CreatureList that has the x and y.

		When a creature moves or attacks, it should ignore himself, so it wont hit himself.
		If the creature has a group of something, it should ignore it's type; 
			ie: A group of skeletons should not attack themselves, but they can kill rats if they're in their way.

		@ TODO
		I'll need to check this method later.
		I have my reasons to believe that there's a bug hidden here... 
		Somewhere... 
		Lurking in between if statements...

		Args:
			CreatureList: list of Creatures 
			x = x coordinate.
			y = y coordinate.
			excludeCreature(Optional): a creature
			excludeType: a type of creature

		Returns:
			target: a Creature object.
		"""

		target = None

		for creature in CreatureList: # Gets creatures from the list.

			if creature.x == x and creature.y == y: # If there is a creature at theese coords:

				if excludeCreature: # But that creature it's not myself.

					if creature is not excludeCreature: # So...:
						target = creature # Attack this

					if excludeType: # But wait, am I targeting a friendly type?:

						if not isinstance(creature, excludeType): # If not:
							target = creature # OK go ahead.

				else: # If I'm confused I can target anyone, including myself
					target = creature

		if target:
			return target
