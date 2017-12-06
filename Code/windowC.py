import pygame
import os

class windowController(object):
	"""
	This class is responsible for controlling the window.
	"""

	def __init__(self):
		"""
		As a simple Controller class this don't need any Attributes.
		"""
		super(windowController, self).__init__()

	def checkFile(self):
		"""
		Checks if there's a window file in the game's folder.
		This window file have all information about the window screen.

		Returns:
			Returns a boolean.
		"""

		# At this point everyone knows that Linux superior to any other OS by far.
		# but for the poor souls out there that refuses to evolve, this try/except will help them out.
		try:
			if os.path.isfile('./opt.dat'):
				return True
			else:
				return False

		except Exception as e:
			if os.path.isfile('\opt.dat'):
				return True
			else:
				return False

		
	def newFile(self, windowModel):
		"""
		Makes a new file.

		This function makes a new file with the windowModel values.

		Args:
			windowModel: The model class for window.
		"""

		opt = open("opt.dat", 'w+')

		# Window Values
		opt.write(windowModel.winName + "\r\n") # +"\r\n" was the way that I found to jump to the next line.
		opt.write(str(windowModel.fullScreen) + "\r\n") # You can argue that there's far better ways to do it.
		opt.write(str(windowModel.windowHeight) + "\r\n") # But mine works.
		opt.write(str(windowModel.windowWidth) + "\r\n") # However, this uniq tecniq gave me a problem with window name
		opt.write(str(windowModel.T_sprRes) + "\r\n") # That's why at windowM file, self.winName = file.readline()[:-2] at loadValues method.
		opt.write(str(windowModel.T_baseColor) + "\r\n") # That ignores the last 2 chars in the string. Happy ending.

		opt.close()