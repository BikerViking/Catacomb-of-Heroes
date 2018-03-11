import sys, os
from threading import Thread

# Hope that this works on windows/mac
pack_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.append(pack_path)

import model.load_model as load_model
import view.load_view 	as load_view

class LoadController(object):
	"""docstring for LoadController"""
	def __init__(self):
		super(LoadController, self).__init__()
		
		self.__is_running 	= True
		self.boot_up()

	def boot_up(self):

		self.__load_model 	= load_model.LoadModel()
		self.__load_view	= load_view.LoadView()

	def get_is_running(self):

		return self.__is_running

	def __swich_is_running(self):

		self.__is_running = not self.__is_running

		# Free some memory.
		if self.__is_running == False:
			del self.__load_model
			del self.__load_view

	def get_next_state(self):
		return 0

	def run(self, window, sound, control, assets, draw):

		# Get Input
		thread_control = Thread(target = control.check_input, args = (False,))

		# Update
		thread_load = Thread(target = self.__load_stuff, args = (assets,))

		# Draw
		thread_view = Thread(target = self.__view_stuff, args = (window, assets, draw,))

		if not self.__load_model._get_is_done():
			thread_control.start()
			thread_load.start()	
			thread_view.start()

			# self.__load_model._switch_is_done()
		else:
			self.__load_view._done(window, assets, draw)
			self.__swich_is_running()

	def __load_stuff(self, assets):

		self.__load_model._load_font(assets)

	def __view_stuff(self, window, assets, draw):

		self.__load_view._draw(window, assets, draw)
