class MainMenuC(object):
	"""
	Controller class from main menu.

	This class will manipulates, via player input, the Model.select
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(MainMenuC, self).__init__()
		
	def navi(self, Model, Input):
		"""
		Navigates throught menu.

		Args:
			Model: Main Menu Model Class
			Input: Input Class.

		Returns:
			Model.select: int.
		"""

		key = Input.handle() # get a key id from input.

		# Use this key to navigate up/down
		if key == 1:
			Model.select -= 1
		if key == 2:
			Model.select += 1

		# Cicle through the options.
		if Model.select < 0 or Model.select > 3:
			if Model.select < 0:
				Model.select = 3
			if Model.select > 3:
				Model.select = 0

		
		if key == 0: # If the Confirm key was pressed
			return Model.select 

	def menu(self, Model, Input):
		"""
		Make the controller method for menu.
		
		Args:
			Model: Main Menu Model Class
			Input: Input Class.
		"""
		choice = self.navi(Model, Input)

		# PLAY
		if choice == 0: # If PLAY was selected
			print("I WANT TO PLAY") # One day, pal, one day.
			Model.done = True # Set this state as done.
			Model.nextID = 2 # Foward to the state number 2, which is the 

		# TODO OPTIONS
		elif choice == 1:
			print("OPTIONS")

		# TODO STATISTICS
		elif choice == 2:
			print("STATISTICS")

		# EXIT
		elif choice == 3: 
			Input.close() # Uses the input MVC method to quit the game.
