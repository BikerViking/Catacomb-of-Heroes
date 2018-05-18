from abc import abstractmethod

class System(object): # metaclass=ABCMeta # Maybe...

	"""docstring for TODONAME"""
	def __init__(self, core_values):
		super(System, self).__init__()
		self.__core_values = core_values

	@abstractmethod
	def default_values(self):
		pass

	def set_values(self, key, value):
		self.__core_values[key] = value

	def get_values(self, key = None):

		if key:
			return self.__core_values[key]

		else:
			return self.__core_values