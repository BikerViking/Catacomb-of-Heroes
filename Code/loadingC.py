import copy
import graphics

class loadingController(object):
	"""
	Controller class for Loading.

	Attributes:
		Graphics: Graphics Class
		floorFile: String that contains the relative path to floor spritesheet.
		wallFile: String that contains the relative path to wall spritesheet.
		heroFile: String that contains the relative path to hero spritesheet.
	"""

	def __init__(self):
		"""
		Initialize self.

		@ TODO
		Paths need to be on Try/Except to work on Windows machines.
		"""
		super(loadingController, self).__init__()

		self.Graphics = graphics.Graphics()
		self.floorFile = "Assets/GFX/Floor.png"
		self.wallFile = "Assets/GFX/Wall.png"
		self.heroFile = "Assets/GFX/Player_SS.png"

	def loadStuff(self, Model, Assets, T_scale = None):
		"""
		Loads the graphics on Assets Agents

		Args:
			Model: Loading Model Class.
			Assets: Assets Class
			T_scale(Optional): int Tuple of two values that scales the sprite.
		"""
		self.loadFloor(Assets, T_scale) 
		self.loadWall(Assets, T_scale)
		self.loadHero(Assets, T_scale)
		Model.done = True

	def loadFloor(self, Assets, T_scale = None):
		"""
		Load floor graphics and give it to the floor agent object on Assets.

		Args:
			Assets: Assets Class
			T_scale(Optional): int Tuple of two values that scales the sprite.
		"""
		Assets.getAsset(0, 0).gfx = self.Graphics.loadGraphics(self.floorFile, ((0, 0)), 1, (16,16), T_scale)
		
	def loadWall(self, Assets, T_scale = None):
		"""
		Load wall graphics and give it to the wall agent object on Assets.

		Args:
			Assets: Assets Class
			T_scale(Optional): int Tuple of two values that scales the sprite.
		"""

		Assets.getAsset(1, 0).gfx = self.Graphics.loadGraphics(self.wallFile, ((0, 0)), 1, (16, 16), T_scale)


	def loadHero(self, Assets, T_scale = None):
		"""
		Load hero graphics and give it to the hero agent object on Assets.

		Args:
			Assets: Assets Class
			T_scale(Optional): int Tuple of two values that scales the sprite.
		"""
		Assets.getAsset(2, 0).gfx = self.Graphics.loadGraphics(self.heroFile, ((0, 0)), 2, (16, 16), T_scale)
		


	# Scrap code, could be useful someday.
	# for i in range(len(Assets.floorList)):
		# Assets.getAsset(0, i).gfx = self.Graphics.loadGraphics(self.floorFile, ((0+i)*16, 0), 1, (16,16), T_scale)