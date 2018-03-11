import pygame
import ConfigParser

import file
import index
import custom

class Control(object):
	"""
	Verifies valid game input.
	"""
	
	"""
	def __init__(self):
		super(Control, self).__init__()
	"""

	@staticmethod
	def _get_input(index, keys, event, state):
		"""
		Gets valid game input.

		Args:
			index: dictionary, it contains all keyboard mapped.
			key: object, could be either custom or default.
			event: pygame event, used to check what key was pressed.
			state: int, checks which state of the game is beeing controled.

		Returns:
			key_id: int, value to State's Controll class controll the game.
		"""

		key_id = None

		# Fail safe: if the keyboard is somewhat special
		# it will be treated here.
		if (index[pygame.key.name(event.key)] == "unknown key"):
			print("ERROR: unknown key")

		# Checks game state.
		if state == 1:

			# checks index for the key that pygame got 
			# and verifies if it's a valid game input.
			# If it does, return a int value.
			if (int(index[pygame.key.name(event.key)]) == int(keys._menu_key_up)):
				print("Menu Key: UP")
				key_id = 2

			if (int(index[pygame.key.name(event.key)]) == int(keys._menu_key_down)):
				print("Menu Key: DOWN")
				key_id = 3

			if (int(index[pygame.key.name(event.key)]) == int(keys._menu_key_left)):
				print("Menu Key: LEFT")
				key_id = 4

			if (int(index[pygame.key.name(event.key)]) == int(keys._menu_key_right)):
				print("Menu Key: RIGHT")
				key_id = 5

			if (int(index[pygame.key.name(event.key)]) == int(keys._menu_key_accept)):
				print("Menu Key: ACCEPT")
				key_id = 1

			if (int(index[pygame.key.name(event.key)]) == int(keys._menu_key_decline)):
				print("Menu Key: DECLINE")
				key_id = 0

		elif (state == 2):

			if (index[pygame.key.name(event.key)] == keys._game_key_up):
				key_id = 8

			if (index[pygame.key.name(event.key)] == keys._game_key_up_left):
				key_id = 7

			if (index[pygame.key.name(event.key)] == keys._game_key_up_right):
				key_id = 9

			if (index[pygame.key.name(event.key)] == keys._game_key_down):
				key_id = 2

			if (index[pygame.key.name(event.key)] == keys._game_key_down_left):
				key_id = 1

			if (index[pygame.key.name(event.key)] == keys._game_key_down_right):
				key_id = 3

			if (index[pygame.key.name(event.key)] == keys._game_key_left):
				key_id = 4

			if (index[pygame.key.name(event.key)] == keys._game_key_right):
				key_id = 6

			if (index[pygame.key.name(event.key)] == keys._game_key_menu):
				key_id = 13

			if (index[pygame.key.name(event.key)] == keys._game_key_itens):
				key_id = 12

			if (index[pygame.key.name(event.key)] == keys._game_key_accept):
				key_id = 11

			if (index[pygame.key.name(event.key)] == keys._game_key_decline):
				key_id = 10

		return key_id