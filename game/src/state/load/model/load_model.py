import model_font

class LoadModel(object):
	"""
	docstring for LoadModel
	"""

	def __init__(self):
		super(LoadModel, self).__init__()

		self._is_done = False

		self._model_font = model_font.ModelFont()

	def _load_font(self, assets):

		self._model_font._load_font(assets)

	def _switch_is_done(self):

		self._is_done = not self._is_done

	def _get_is_done(self):

		return self._is_done