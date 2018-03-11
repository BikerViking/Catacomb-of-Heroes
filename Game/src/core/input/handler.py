import pygame

import index
import file

import default
import custom
import control

class Handler(object):
	"""
	Handles the game input.

	Attributes:
		index: object, map the keyboard with all keys.
		file: object, create a file to be loaded with user preferences.
		keys: object, could be either default keys or custom keys.
	"""
	def __init__(self):
		"""
		Init Handler Object:

		index: creates a dictionary with all keyboard keys.
		file: manages input.ini file.
		keys: stores game command keys.
		"""

		super(Handler, self).__init__()

		self.__index = index.Index()

		if (file.File._check_file()):
			self.__keys = custom.Custom(self.__index._keys, file.File._check_file())

		else:
			self.__keys = default.Default(self.__index._keys)
			file.File._make_file(self.__keys)

	def check_input(self, is_input_enable):
		"""
		Checks if the input makes any sense to the game.

		Args:
			is_input_enable: Bool, switch on/off inputs.

		Returns:
			key_id: int, value to State's Controll class controll the game.
		"""

		# pygame, you're awesome.
		# pygame checks for events and handles them.
		# Then I can use theese events to check for inputs.
		for event in pygame.event.get():

			# Quits the game.
			# TODO before quitting: save game.
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			if event.type == pygame.KEYDOWN and is_input_enable:
				key_id = control.Control._get_input(self.__index._keys, self.__keys, event, 1)
				return key_id