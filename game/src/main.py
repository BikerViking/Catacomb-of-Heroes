# Imports
import sys
import os

import pygame
from core import core

class Main(object):
	"""docstring for Main"""

	def __init__(self):
		super(Main, self).__init__()

		self.Core = core.Core()

		self.Core.Window.make_screen()
		for i in range(1000):
			self.Core.Window.update_screen()
		# self.Manager = manager.Manager(self.Core)

		exit()
		# self.Manager.run()

	# Magic is done here:
if __name__ == "__main__":
	Main()
