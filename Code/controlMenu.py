import copy

class ControlMenu(object):
	"""
	Controls the Menu navigation.
	"""
	def __init__(self, Model):
		"""
		Initialize self.

		Args:
			Model: Menu Model Object from Game Model Class.
		"""
		super(ControlMenu, self).__init__()
		self.Model = Model

	def NavigateMenu(self, key):

		"""
		Modifies the value from Model Class

		Args:
			Key: int, from the Input Class.
		"""

		maxChoice = 2

		# Navigates up and down the menu.
		if key == 1:
			self.Model.navi -= 1
		if key == 2:
			self.Model.navi += 1

		# Cicle thrught the menu.
		if self.Model.navi < 0 or self.Model.navi > maxChoice:
			if self.Model.navi < 0:
				self.Model.navi = maxChoice
			if self.Model.navi > maxChoice:
				self.Model.navi = 0

		# Decides what to do when hit confirm button.
		if key == 0:
			if self.Model.navi == 0:
				self.Model.isOpen = False
			elif self.Model.isOpen == 1:
				self.Model.toMainMenu()
