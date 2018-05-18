import pygame

class ModelFont(object):
	"""docstring for ModelFont"""
	def __init__(self):
		super(ModelFont, self).__init__()

		self.__path 		= "../data/assets/fonts/"
		
		self.__size 		= 8 # TODO This needs to be a variable.
		self.__debug_font	= pygame.font.Font(self.__path + "Pixeled.ttf", self.__size)
		self.__main_font 	= pygame.font.Font(self.__path + "DUNGRG.ttf", self.__size)

	def _load_font(self, assets):

		assets._font.set_fonts(self.__debug_font)
		assets._font.set_fonts(self.__main_font)