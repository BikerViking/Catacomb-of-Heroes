import pygame
import ConfigParser # Makes easier to read data from file.

class Custom(object):
	"""
	Loads keys.

	Attributes:
		menu_key: Keys that control menu.
		game_key: Keys that control game.
	"""
	def __init__(self, key, file):
		"""
		Inits Custom Object

		Args:
			key: dictionary, it contains all keyboard mapped.
			file: file, it contains custom input settings.
		"""

		super(Custom, self).__init__()

		self.__custom_menu_keys(key, file)
		self.__custom_game_keys(key, file)

	def __custom_menu_keys(self, key, file):
		"""
		Uses key and file to set custom menu keys.

		Args:
			key: dictionary, it contains all keyboard mapped.
			file: file, it contains custom input settings.
		"""
		
		config = ConfigParser.ConfigParser()
		config.read(file)	

		self._menu_key_up 		= config.get("Input Menu", "up")
		self._menu_key_down 	= config.get("Input Menu", "down")
		self._menu_key_left 	= config.get("Input Menu", "left")
		self._menu_key_right 	= config.get("Input Menu", "right")

		self._menu_key_accept 	= config.get("Input Menu", "accept")
		self._menu_key_decline 	= config.get("Input Menu", "decline")

	def __custom_game_keys(self, key, file):
		"""
		Uses key and file to set custom game keys.

		Args:
			key: dictionary, it contains all keyboard mapped.
			file: file, it contains custom input settings.
		"""

		config = ConfigParser.ConfigParser()
		config.read(file)

		self._game_key_up 			= config.get("Input Game", "up")
		self._game_key_up_left 		= config.get("Input Game", "up left")
		self._game_key_up_right 	= config.get("Input Game", "up right")
		self._game_key_down 		= config.get("Input Game", "down")
		self._game_key_down_left 	= config.get("Input Game", "down left")
		self._game_key_down_right 	= config.get("Input Game", "down right")
		self._game_key_left 		= config.get("Input Game", "left")
		self._game_key_right 		= config.get("Input Game", "right")

		self._game_key_menu 		= config.get("Input Game", "menu")
		self._game_key_itens 		= config.get("Input Game", "itens")
		self._game_key_accept 		= config.get("Input Game", "accept")
		self._game_key_decline 		= config.get("Input Game", "decline")