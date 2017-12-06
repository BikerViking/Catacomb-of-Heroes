import fonts
import structure

import floorIndex
import wallIndex
import playerIndex

class Assets(object):
	"""
	This class hold the data of game objects.

	Attributes:
		fonts: list of game fonts objects
		floorList: list of floor objects
		wallList: list of wall objects
		heroList: list of heroes objects
 	"""
	def __init__(self):
		super(Assets, self).__init__()
		
		self.fonts = fonts.Fonts()

		self.floorList = floorIndex.FloorIndex.makeFloor()
		self.wallList = wallIndex.WallIndex.makeWall()
		self.heroList = playerIndex.PlayerIndex.makeHero()

	def getAsset(self, typeID, assetID):
		"""
		Picks a object from assets list.

		Args:
			typeID: an int that defines the type of Asset 
			assetID: an int that defines the Asset object

		Returns:
			Agent
		"""

		if typeID == 0:
			return self.floorList[assetID]
		elif typeID == 1:
			return self.wallList[assetID]
		elif typeID == 2:
			return self.heroList[assetID]