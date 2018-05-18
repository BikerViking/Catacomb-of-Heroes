import pygame

from .. import system
class Input(system.System):
	"""docstring for Input"""
	def __init__(self):

		self.__core_values = {"up" 			: None,
							  "down"		: None,
							  "left" 		: None,
							  "right" 		: None,
							  "upleft" 		: None,
							  "upright" 	: None,
							  "downleft"	: None,
							  "downright"	: None,
							  "itens"		: None,
							  "accept"		: None,
							  "decline"		: None,
							  "menu"		: None
							 }

		super(Input, self).__init__(self.__core_values)

	def default_values(self):
		up 			= 119	# w
		down 		= 120	# x
		left		= 97	# a
		right		= 100	# d
		upleft		= 113	# q
		upright		= 101	# e
		downleft	= 122	# z
		downright	= 99	# c
		itens		= 303	# right shift
		accept		= 13	# return
		decline		= 8		# backspace
		menu		= 27	# esc

		self.__core_values["up"] 			= up
		self.__core_values["down"] 			= down
		self.__core_values["left"] 			= left
		self.__core_values["right"] 		= right
		self.__core_values["upleft"] 		= upleft
		self.__core_values["upright"] 		= upright
		self.__core_values["downleft"] 		= downleft
		self.__core_values["downright"] 	= downright
		self.__core_values["itens"] 		= itens
		self.__core_values["accept"] 		= accept
		self.__core_values["decline"] 		= decline
		self.__core_values["menu"] 			= menu

	def set_values(self, key, value):
		self.__core_values[key] = int(value)

	def __get_input(self, input):

		for key, value in self.__core_values.items():

			if input == value:
				return key

		else:
			return False


	def event_handler(self):

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				# TODO SAVE BEFORE QUIT.
				pygame.quit()
				exit()

			elif event.type == pygame.KEYDOWN:
				# print (event.key, end=" ")
				# print (type(event.key))
				return self.__get_input(event.key)
