import structure

class GenMap(object):
	"""docstring for GenMap"""
	def __init__(self):
		super(GenMap, self).__init__()
		
	def genMap(self, T_sprRes, T_winRes):

		map_width, map_height = ([x/T_sprRes[0] for x in T_winRes])

		new_map = [[structure.Structure(False) for x in range (0, map_height)] for y in range (0, map_width)]
		
		new_map[7][3].isWall = True
		new_map[8][3].isWall = True
		new_map[7][10].isWall = True
		new_map[8][10].isWall = True

		for x in range(map_width):
			new_map[x][0].isWall = True
			new_map[x][map_height-1].isWall = True

		for y in range(map_height):
			new_map[0][y].isWall = True
			new_map[map_width-1][y].isWall = True
			
		return new_map