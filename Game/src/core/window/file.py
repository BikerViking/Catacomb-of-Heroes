import os

class File(object):
	"""
	This class checks and make a window configuration file.
	"""
	@staticmethod
	def _check_file():
		"""
		Check if there is a windows configuration file.

		Returns:
			Window configuration file path or False.
		"""
		if os.path.isfile('../data/prefrences/window.ini'):
			file = "../data/prefrences/window.ini"
			return file
		else:
			return False

	@staticmethod
	def _make_file(values):
		"""
		Makes a window configuration file.

		Args:
			values: data object. File is written into data attributes.
		"""

		file = open("../data/prefrences/window.ini", 'w+')

		file.write("[Window]\r\n")

		file.write("name: ")
		file.write(values._window_name + "\r\n")

		file.write("fullscreen: ")
		file.write(str(values._is_full_screen) + "\r\n")

		file.write("height: ")
		file.write(str(values._window_height) + "\r\n")

		file.write("width: ")
		file.write(str(values._window_width) + "\r\n")

		file.write("sprite: ")
		file.write(str(values._sprite_resolution) + "\r\n")

		file.close()