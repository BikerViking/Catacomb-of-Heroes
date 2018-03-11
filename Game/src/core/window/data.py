import pygame
import ConfigParser
from ast import literal_eval as make_tuple


class Data(object):
	""" 
	Holds information about game window.

	Attributes:
		clock: pygame Object, keep track of the time.
		fps: int, this controls the Frames Per Second of the game
		base_color: int tuple, window background color
		base_surface: pygame surface, base surface of the game.
		window_name: string, holds the string to be displayed on the window
		is_full_screen: boolean, checks if it should be on full screen
		window_height: int, determinates the window height
		window_width: int, determinates the window width
		sprite_resolution: int tuple, the height and width of sprites.
	"""

	def __init__(self, file = None):
		"""
		Inits WindowValues class.
		
		Args:
			file: dat file, contains user custom settings for the window.
		"""

		super(Data, self).__init__()
		
		self.__core_values()

		if file:
			self.__custom_values(file)
		else:
			self.__default_values()
		
	def __core_values(self):
		"""
		Set the core values of the game window.
		"""

		self._clock 		= pygame.time.Clock()
		self._fps 			= 25
		self._base_color 	= (188, 235, 234)

		self._base_surface 	= (0, 0)

	def __default_values(self):
		"""
		Set the default values for window.
		"""

		self._window_name 		= "Catacombs"

		self._is_full_screen 	= False

		self._window_height 	= 512
		self._window_width 		= 448

		self._sprite_resolution = (32, 32)

	def __custom_values(self, file):
		"""
		Set values with custom values from file.

		Args:
			file: dat file, contains user custom settings for the window.
		"""

		config = ConfigParser.ConfigParser()
		config.read(file)
		
		self._window_name 		= config.get("Window", "name")

		self._is_full_screen 	= bool(config.get("Window", "fullscreen"))

		self._window_height 	= int(config.get("Window", "height"))
		self._window_width 		= int(config.get("Window", "width"))

		self._sprite_resolution = make_tuple(config.get("Window", "sprite"))

	def get_window_resolution(self):
		"""
		Returns window actual resolution

		Returns:
			tuple with windows's height and width
		"""

		return (self._window_height, self._window_width)

	def get_sprite_resolution(self):
		"""
		Returns sprite resolution

		Returns:
			sprite_resolution: tuple with sprite's height and width
		"""

		return self._sprite_resolution