import pygame
import inputMC

class managerController(object):
	"""
	This is the controller for the manager class.

	Attributes:
		inputMC: Class that models and handles the input.
		alpha: sets alpha when you change from one state to the other.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(managerController, self).__init__()

		self.inputMC = inputMC.InputMC()
		self.alpha = 0


 	def gameLoop(self, Model, winSurface, updateView):
 		"""
 		The game runs inside a loop. This defines what are the methods called in this loop.

 		Args:
 			Model: Manager Model class to acess their state list.
 			winSurface: pygame surface which was done by the Window class.
 			updateView: Method from Window class that updates the game.
 		"""
 		if not Model.getState().done: # While model is not done:
 			Model.getState().runLogic(self.inputMC) # State can run it's logic.
 			
 		winSurface.blit(Model.getState().drawGame(), (0,0)) # Draw the view of the state on top of the base surface of the window.

 		self.changeState(Model, winSurface) # Change state when needed.

 		updateView() # Runs the windowV method to update this loop in a framerate.


 	def fade(self, winSurface, inOut):
 		"""
		Fades in or out the screen

		Args:
			winSurface: The window base Surface
			inOut: a boolean that tells this function if it's going to fade In (True) or fade Out (False).
 		"""

	 	if inOut: # If True, Fade In:
	 		self.alpha += 10 # Adds alpha
	 		if self.alpha > 255: # alpha cannot be greater than 255:
	 			self.alpha = 255 # so if it is, set it to 255.
	 	else: # If False, Fade Out:
	 		self.alpha -= 10 # Subtract alpha
	 		if self.alpha < 0: # alpha cannot be less than 0:
	 			self.alpha = 0 # so if it is set it to 0.

 		surface = pygame.Surface(winSurface.get_size()) # Make a temp surface, with the window resolution.
 		surface.set_alpha(self.alpha) # set it's alpha.
 		winSurface.blit(surface, (0, 0)) # draw it on top of everything
 		

 	def changeState(self, Model, winSurface):
 		"""
		This method changes the state of the game.

		Args:
			Model: Manager Model class.
			winSurface: Window base surface.
 		"""

 		if Model.getState().done: # If the state is over.
			self.inputMC.Flag = False # Forbid input.
			pygame.event.clear() # Clears input list.
 			self.fade(winSurface, True) # Fades in.

		 	if self.alpha == 255: # Once it's completly faded in
		 		Model.getState().resetValues() # Reset the actual state values
				Model.stateID = Model.getState().nextID # Get the next state 

 		elif not self.alpha == 0: # If State is not done and it's faded in
 			self.fade(winSurface, False) # Fade out
 			self.inputMC.Flag = True # Allow getting inputs again.