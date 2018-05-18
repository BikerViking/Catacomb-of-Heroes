class LoadView(object):
	"""docstring for LoadView"""
	def __init__(self):
		super(LoadView, self).__init__()

		self.__msg 			= "LOADING"

		self.__count_fps 	= 0
		self.__is_max_count = False
	
	def _draw(self, window, assets, draw):

		surface = window.get_base_surface()
		font 	= assets._font.get_font(0)

		surface.fill((0, 0, 0))

		self.__animate(window)

		draw.draw_text(surface, font, self.__msg, pos = (5, surface.get_rect()[3]-25))

	def __animate(self, window):

		self.__count_fps += 1
		fps = window.get_fps()

		if self.__count_fps == fps or self.__count_fps == fps*2 or self.__count_fps == fps*3:
			if not self.__is_max_count:
				self.__msg += "."
			else:
				self.__msg = self.__msg[:-1]

		if self.__count_fps == fps*3:
			self.__is_max_count = not self.__is_max_count
			self.__count_fps = 0

	def _done(self, window, assets, draw):

		draw.draw_text(window.get_base_surface(), assets._font.get_font(0), "Loading Done!", pos = (5, window.get_base_surface().get_rect()[3]-25))