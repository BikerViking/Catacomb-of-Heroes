import os
import ConfigParser

"""
TODO:

Verify if file is OK.
"""

class File(object):

	def __init__(self):
		super(File, self).__init__()

	def is_file(self, path):
		""" Checks if there's user configuration files. """

		if os.path.isfile(path):
			# self.config_file = path
			return path

		else:
			return False

	def make_file(self, title, core_values, path):
		"""
		Recieves dictionary from class and uses it's values to create a
		configuration file.

		Args:
			title = string, set a reference title for load_values to read.
			core_values = dictionary witch contains data to be written on file.
		"""

		if self.is_file(path):
			file = open(path, "a")

		else:
			file = open(path, "w")

		file.write("[" + title + "]\n")

		for key, value in core_values.items():
			file.write(key + ": " + str(value) + "\n")

		file.write("\n")
		file.close()


	def load_values(self, title, system, path):
		"""
		Reads file's values and loads them on the system's dictionary.

		Args:
			title = string, set a reference title for load_values to read.
			system = core class, where values are going to be loaded on.

		"""

		try:
			config = ConfigParser.ConfigParser()
			config.read(self.is_file(path))

			for key in system.get_values():
				system.set_values(key, config.get(title, key))

		except:
			print ("Config File is corrupt!")
