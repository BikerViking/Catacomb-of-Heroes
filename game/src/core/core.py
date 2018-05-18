# Imports
import sys
import os

import pygame

from file				import file
from system.window		import window
from system.input		import input

class Core(object):
	"""
	This class will 'boot up' the basics systems of the game.

	Attributes:
		file:		TODO
		window:		Package, manages game window.
		sound: 		Package, manages game sound.
		control: 	Package, manages game input.
		manager:	Package, manages the game.
	"""

	def __init__(self):
		"""
		Initialize Core.

		When this class is instantiated it will set the basic systems of the
		game.

		"""

		super(Core, self).__init__()

		file_name 	= "config.dat"

		if os.name == "nt":
			dir_path 	= "\data\prefrences\\"

		else:
			dir_path 	= "data/prefrences/"

		self.File 	= file.File()

		self.Window = window.Window()
		self.Input 	= input.Input()

		if self.File.is_file(dir_path+file_name):
			self.File.load_values("window", self.Window, (dir_path+file_name))
			self.File.load_values("input", self.Input, (dir_path+file_name))

		else:
			self.Window.default_values()
			self.Input.default_values()
			self.File.make_file("window", self.Window.get_values(), (dir_path+file_name))
			self.File.make_file("input", self.Input.get_values(), (dir_path+file_name))

		# Window.make_screen()

		# while True:

		# 	key = Input.event_handler()

		# 	if key:
		# 		print (key)

		# 	Window.update_screen()
