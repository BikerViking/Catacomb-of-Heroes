import graphics

class Assets(object):
	"""docstring for Assets"""
	def __init__(self):
		super(Assets, self).__init__()

		self.__gfx_dict = {"fonts"      : None, # stores font dict
                           "actors"     : None # stores dict of actors objects
                                                # witch contains an animation dict for every action.
                           }

		self.__assets = {"GFX" : self.__gfx_dict}

	def load_asset(self, key1, key2, asset):
		self.__assets[key1][key2] = asset


	def get_asset(self, key1, key2, key3):
		return self.__assets[key1][key2][key3]
