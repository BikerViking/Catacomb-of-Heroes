import pygame

class InputController(object):
	"""	
	This class controls inputs.

	@TODO
	A way to change keys.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(InputController, self).__init__()
		# self.flag = False

	def close(self):
		"""
		Closes the game.

		It properly closes the game by quitting the pygame and exiting the python.
		"""
		pygame.quit()
		exit()

	def handle(self, inputM, flag):
		"""
		Handles the input.

		Args:
			inputM: input's Model Class
			flag: boolean that turns the input on/off

		Returns:
			a int that represents a key.
		"""
		for event in pygame.event.get(): # Gets pygame events
			if event.type == pygame.QUIT: # If the event is Quit (if the [x] button was clicked)
				self.close() # Close the game.
			if event.type == pygame.KEYDOWN and flag: # If was a keydown event and if the flag is true:

				if inputM.keys[pygame.key.name(event.key)] == "unknown key": # prevents error on the game if a wiered key is pressed.
					print ("ERROR: UNKNOWN KEY")				
					pass

				if inputM.keys[pygame.key.name(event.key)] == inputM.K_START: # If the key pressed is equals to Model key:
					return -1 # return a int.

				if inputM.keys[pygame.key.name(event.key)] == inputM.K_OK:
					return 0
				
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_UP:
					return 1
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_DOWN:
					return 2
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_LEFT:
					return 3
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_RIGHT:
					return 4
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_UL:
					return 5
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_UR:
					return 6
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_DL:
					return 7
				if inputM.keys[pygame.key.name(event.key)] == inputM.K_DR:
					return 8

# Scrap code, could be useful someday.
				# if self.flag:
				# 	self.inputM.N_UP = self.inputM.keys[pygame.key.name(event.key)]
				# 	self.flag = False
				# 	print("N_UP: " + pygame.key.name(event.key) + " " + str(self.inputM.N_UP))

				# if self.inputM.keys[pygame.key.name(event.key)] == self.inputM.N_NG:
				# 	self.flag = True