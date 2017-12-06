import pygame

class Graphics(object):

	"""
	THis class gets a spritesheet file and selects items from the spritesheet
	converts what they got into a pygame Surface, appends it to a list and returns it.

	Attributes:
		colorKey: int, tuple, this is the color of the sprite that will be set transparent.
	"""

	def __init__(self):
		"""
		Initialize self.

		Sets up the default value for colorKey.
		"""
		super(Graphics, self).__init__()

		self.colorKey = (255, 255, 255)

	def loadGraphics(self, File, T_coord, numSpr, T_sprRes, T_scale = None):

		"""
		Load sprites from a file.

		Args:
			File: String, relative path to spritesheet file.
			T_coord: int, tuple, the coordinate to the sprite.
			numSpr: int, number of sprites that will be load from the file.
			T_sprRes: int, tuple, resolution of the sprite on the file.
			T_scale(Optional): int, tuple, scales the sprite.

		Returns:
			spriteList: list of pygame Surfaces which contais sprites.
		"""

		spriteSheet = pygame.image.load(File).convert() # Temp pygame surface with the whole spritesheet.

		col, row = T_coord # Made this just for visualization.

		width, height = T_sprRes # To understand what is what.

		spriteList = []

		for i in range(numSpr):

			image = pygame.Surface([width, height]).convert() # Blank temp pygame surface

			# Get the sprite at given coordinates and draw it on the image surface.
			image.blit(spriteSheet, (0,0), (col*width+(width*i), row*height, width, height)) 

			image.set_colorkey(self.colorKey) # Sets the background transparent.

			if T_scale: # Scales the sprite, if needed.
				image = pygame.transform.scale(image, T_scale)

			spriteList.append(image) # Appends on the List.

		return spriteList 

