import pygame

import os
from ast import literal_eval as make_tuple

from .. import system

class Window(system.System):
	"""docstring for Window"""
	def __init__(self):

		self.__clock 	 = pygame.time.Clock()
		self.__fps 		 = 30
		self.__base_color = (188, 235, 234)

		self.__core_values = {"name" 		: None,
							  "fullscreen" 	: None,
							  "resolution" 	: None,
							  "sprite" 		: None # delete this later, please.
							 }

		super(Window, self).__init__(self.__core_values)

	def default_values(self):

		name 		= "Catacombs"
		fullscreen 	= False
		resolution 	= (512, 448)
		sprite 		= (32, 32)

		self.__core_values["name"] 			= name
		self.__core_values["fullscreen"] 	= fullscreen
		self.__core_values["resolution"] 	= resolution
		self.__core_values["sprite"] 		= sprite

	def set_values(self, key, value):

		if key == "name":
			value = str(value)

		elif key == "fullscreen":

			if value == "True":
				value = True

			else:
				value = False

		elif key == "resolution" or key == "sprite":
			value = make_tuple(value)

		self.__core_values[key] = value

	def make_screen(self):

		os.environ['SDL_VIDEO_CENTERED'] = '1'

		pygame.init()

		if self.__core_values["fullscreen"]:
			# TODO for some reason my pygame is not working fullscreen :(
			pass

		pygame.display.set_caption(self.__core_values["name"])

		self.core_surface = pygame.display.set_mode((self.__core_values["resolution"]))
		self.core_surface.fill(self.__base_color)

	def update_screen(self):

		pygame.display.flip()
		pygame.display.update()
		self.__clock.tick(self.__fps)
