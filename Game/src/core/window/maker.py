import pygame
import data
import file

class Maker(object):
	"""
	Makes game window.

	Attributes:
		file: object, checks/creates window file
		data: object, contains windows values.
	"""
	
	def __init__(self):
		"""
		Init Maker object.

		file: manages window.ini file.
		data: holds window data.
		"""

		super(Maker, self).__init__()

		if (file.File._check_file()):
			self.__data = data.Data(file.File._check_file())
		else:
			self.__data = data.Data()
			file.File._make_file(self.__data)

		self.__make_screen()

	def __make_screen(self):
		"""
		Makes screen.

		Checks for data's values for pygame make game screen.
		"""

		pygame.init() # Inits pygame

		if (self.__data._is_full_screen):
			# pygame.display.toggle_fullscreen() # my pygame is having trouble with this code.
			pass

		pygame.display.set_caption(self.__data._window_name)
		self.__data._base_surface = pygame.display.set_mode(self.__data.get_window_resolution())
		self.__data._base_surface.fill(self.__data._base_color)

	def get_base_surface(self):
		return self.__data._base_surface

	def get_fps(self):
		return self.__data._fps

	def update_fps(self):
		"""
		Updates the game window code.

		This update is done via pygame functions.

		Args:
			clock: pygame object that helps to track time
			fps: an int that sets the how the frames per second rate for the game.
		"""

		pygame.display.flip()
		pygame.display.update()
		self.__data._clock.tick(self.__data._fps)