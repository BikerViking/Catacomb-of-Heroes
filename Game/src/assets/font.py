class Font(object):
	"""
	docstring for Font
	"""

	def __init__(self):
		super(Font, self).__init__()

		self.__font_list = []
		
	def set_fonts(self, font_path):

		self.__font_list.append(font_path)

	def get_font(self, font_id):

		return self.__font_list[font_id]
