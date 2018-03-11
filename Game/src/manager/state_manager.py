import state_list

class StateManager(object):
	"""docstring for StateManager"""
	def __init__(self, window, sound, control):
		super(StateManager, self).__init__()

		self._actual_state 	= 0
		self._state_list 	= state_list.StateList()

	def run(self, window, sound, control):

		if not self._state_list.get_state(self._actual_state).get_is_running():
			self._actual_state = self._state_list.get_state(self._actual_state).get_next_state()

		else:
			self._state_list.get_state(self._actual_state).run(window, sound, control, 
																self._state_list._assets, self._state_list._draw)
