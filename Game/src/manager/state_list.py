import sys, os

package_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(package_path)

import assets.manager 							as assets
import draw.text 								as draw
import state.load.controller.load_controller 	as load_controller

class StateList(object):
	"""
	docstring for StateList
	"""

	def __init__(self):
		super(StateList, self).__init__()

		self._assets 		= assets.Manager()
		self._draw			= draw.Text()

		self.__load_game 	= load_controller.LoadController()
		"""
		self.__main_menu 	= 
		self.__game_state 	=
		"""

		self._list 			= []

		self._list.append(self.__load_game)

	def get_state(self, state_id):
		return self._list[state_id]