import pygame
import copy

class Map(object):
	"""
	This class draws the map on the screen.

	Attributes:
		dark: pygame surface that will darken a sprite.
	"""
	def __init__(self, T_sprRes, T_winRes):
		"""
		Initialize self.

		Args:
			T_sprRes: int Tuple with the base sprite resolution.
			T_winRes: int Tuple with the window resolution.
		"""
		super(Map, self).__init__()

		self.T_sprRes = T_sprRes
		self.T_winRes = T_winRes

		self.dark = pygame.Surface(self.T_sprRes).convert_alpha()
		self.dark.fill((0,0,0, .40*255))

	def drawMap(self, Model, Assets):
		"""	
		Draws the map.

		@ TODO Field of Vision:
		Draws diffrent things based on players field of vision.

		Args:
			Model: Game Model class
			Assets: Assets Class

		Returns:
			mapSurface: pygame surface with the map drawn.
		"""

		mapSurface = pygame.Surface(self.T_winRes) # Makes a surface with the screen size.
		mapRes = ([x/self.T_sprRes[0] for x in self.T_winRes]) # Makes a grid with the sprite size and window size.

		mapToDraw = Model.mapList[Model.level] # Gets the map that will be drawn from Model.

		wall = copy.copy(Assets.getAsset(1, Model.level)) # Copies the wall object from Assets.
		floor = copy.copy(Assets.getAsset(0, Model.level)) # Copies the floor object from Assets.

		darkWall = copy.copy(Assets.getAsset(1, Model.level).gfx[0]) # Copies the wall object from Assets.
		darkWall.blit(self.dark, (0, 0)) # Darken this sprite by code.

		darkFloor = copy.copy(Assets.getAsset(0, Model.level).gfx[0]) # Copies the floor object from Assets.
		darkFloor.blit(self.dark, (0, 0)) # Darken this sprite by code.

		for x in range(0, mapRes[0]):
			for y in range(0, mapRes[1]):

				isVisible = True # TODO isVisible will be changed based on heros field of vision.
					
				if isVisible: 
					if Model.mapList[Model.level][x][y].isWall: 
						mapSurface.blit(wall.gfx[0], (x*self.T_sprRes[0], y*self.T_sprRes[1]))
					else:
						mapSurface.blit(floor.gfx[0], (x*self.T_sprRes[0], y*self.T_sprRes[1]))
				# TODO elif wasExplored:
					# This will draw the darken sprites of walls and floors if they were explored.
				# TODO else:
					# This will draw a black square, 'cuz player didn't explore this tile yet.

		return mapSurface