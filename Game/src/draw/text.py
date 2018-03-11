class Text(object):
	"""docstring for Text"""
	def __init__(self):
		super(Text, self).__init__()

		self.__default_text_color 	= (255, 255, 255)
		self.__default_bg_color 	= (0, 0, 0)
		self.__default_pos 			= (0, 0)
		
	def __text_handler(self, font, text, color = None, bg_color = None):

		if not (color or bg_color):

			if not color:
				color 		= self.__default_text_color

			if not bg_color:
				bg_color 	= self.__default_bg_color

		text_surface 		= font.render(text, False, color, bg_color)

		return text_surface

	def draw_text(self, surface, font, text, color = None, bg_color = None, pos = None):

		text_surface 			= self.__text_handler(font, text, color, bg_color)
		text_rect 				= text_surface.get_rect()

		if pos:
			text_rect.topleft 	= pos

		else:
			text_rect.topleft 	= self.__default_pos

		surface.blit(text_surface, text_rect)