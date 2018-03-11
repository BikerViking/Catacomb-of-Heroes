import os

class File(object):
	"""
	This class checks and make an input configuration file.
	"""

	@staticmethod
	def _check_file():
		"""
		Checks if there is a file.

		Returns:
			Input configuration file path or False.
		"""

		if os.path.isfile('../data/prefrences/input.ini'):
			file = "../data/prefrences/input.ini"
			return file
		else:
			return False

	@staticmethod
	def _make_file(values):
		"""
		Makes input configuration file.

		Args:
			values: class, which contais all game keys.
		"""

		file = open("../data/prefrences/input.ini", 'w+')

		file.write("[Input Menu]\r\n")

		file.write("up: ")
		file.write(str(values._menu_key_up) + "\r\n")

		file.write("down: ")
		file.write(str(values._menu_key_down) + "\r\n")

		file.write("left: ")
		file.write(str(values._menu_key_left) + "\r\n")

		file.write("right: ")
		file.write(str(values._menu_key_right) + "\r\n")

		file.write("accept: ")
		file.write(str(values._menu_key_accept) + "\r\n")

		file.write("decline: ")
		file.write(str(values._menu_key_decline) + "\r\n\n")

		file.write("[Input Game]\r\n")
		
		file.write("up: ")
		file.write(str(values._game_key_up) + "\r\n")

		file.write("up left: ")
		file.write(str(values._game_key_up_left) + "\r\n")

		file.write("up right: ")
		file.write(str(values._game_key_up_right) + "\r\n")

		file.write("down: ")
		file.write(str(values._game_key_down) + "\r\n")

		file.write("down left: ")
		file.write(str(values._game_key_down_left) + "\r\n")

		file.write("down right: ")
		file.write(str(values._game_key_down_right) + "\r\n")

		file.write("left: ")
		file.write(str(values._game_key_left) + "\r\n")

		file.write("right: ")
		file.write(str(values._game_key_right) + "\r\n")

		file.write("menu: ")
		file.write(str(values._game_key_menu) + "\r\n")

		file.write("itens: ")
		file.write(str(values._game_key_itens) + "\r\n")

		file.write("accept: ")
		file.write(str(values._game_key_accept) + "\r\n")

		file.write("decline: ")
		file.write(str(values._game_key_decline) + "\r\n")

		file.close()