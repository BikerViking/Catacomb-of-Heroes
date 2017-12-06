# Events

# IMPORTS
	# Third Party

	# My modules
import inputM
import inputC
'''

'''
class InputMC(object):

	def __init__(self):
		super(InputMC, self).__init__()

		self.inputM = inputM.inputModel()
		self.inputC = inputC.InputController()


	def handle(self):
		return self.inputC.handle(self.inputC)