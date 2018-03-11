import pygame

class Default(object):
	"""
	Sets default keys for the game.

	Attributes:
		menu_key_x: Keys that control menu
		game_key_y: Keys that control game
	"""
	def __init__(self, key):
		"""
		Inits Default Object

		Args:
			Key: dictionary, it contains all keyboard mapped
		"""

		super(Default, self).__init__()

		self.__default_menu_key(key)
		self.__default_game_keys(key)

	def __default_menu_key(self, key):
		"""
		Uses key to set default menu keys.

		Args:
			key: dictionary, it contains all keyboard mapped.
		"""

		self._menu_key_up 		= key["up"]
		self._menu_key_down		= key["down"]
		self._menu_key_left 	= key["left"]
		self._menu_key_right 	= key["right"]

		self._menu_key_accept 	= key["return"]
		self._menu_key_decline 	= key["backspace"]

	def __default_game_keys(self, key):
		"""
		Uses key to set default game keys

		Args:
			Key: dictionary, it contains all keyboard mapped
		"""

		self._game_key_up 			= key["[8]"]
		self._game_key_up_left 		= key["[7]"]
		self._game_key_up_right 	= key["[9]"]
		self._game_key_down 		= key["[2]"]
		self._game_key_down_left 	= key["[1]"]
		self._game_key_down_right 	= key["[3]"]
		self._game_key_left 		= key["[4]"]
		self._game_key_right 		= key["[6]"]

		self._game_key_menu 		= key["escape"]
		self._game_key_itens 		= key["[5]"]
		self._game_key_accept 		= key["enter"]
		self._game_key_decline 		= key["backspace"]