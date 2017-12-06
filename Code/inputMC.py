import inputM
import inputC

class InputMC(object):
	"""
	Unite input's Model and Controller

	Attributes:
		inputM: Model class for input.
		inputC: Controller class for input.
		Flag: boolean that turns on/off the inputs.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(InputMC, self).__init__()

		self.inputM = inputM.inputModel()
		self.inputC = inputC.InputController()

		self.Flag = False

	def handle(self):
		"""
		Handles the input.

		By running a inputC's function, this handles the input.
		"""
		return self.inputC.handle(self.inputM, self.Flag)

	def close(self):
		"""
		Closes the game.

		By running a inputC's function, this closes the game.
		"""
		self.inputC.close()