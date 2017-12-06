import windowM
import windowV
import windowC

class windowMVC(object):
	"""
	This class is responsible for the window classes.

	Attributes:
		windowsM: Window Model class
		windowsV: Window View Class
		windowsC: Window Controll Class
	"""
	def __init__(self):

		"""
		Initialize self.

		When this class is instantiated it will set up the Model, View and Controller for the windows.
		Then it will check if the window defaults were changed and if were, it will notify to Model to change it's default values
		When everything is set, it's time to make the window. 
		"""

		super(windowMVC, self).__init__()

		self.windowM = windowM.windowModel() # Model
		self.windowV = windowV.windowView() # View
		self.windowC = windowC.windowController() # Controller

		if self.windowC.checkFile(): # If there's a file
			self.windowM.loadValues() # Load the file's values.
		else:
			self.windowM.defaultValues() # If not, load the default values
			self.windowC.newFile(self.windowM) # And make a file with this values.

		# With everything set, it's time to View the screen.	
		self.windowV.makeScreen(self.windowM.winName, self.windowM.fullScreen, self.windowM.T_winRes, self.windowM.T_baseColor)

	def updateView(self):
		"""
		Updates the view

		Updates the window by running windowV's function.
		"""
		self.windowV.updateView(self.windowM.clock, self.windowM.fps)