import pygame
import copy

class GameView(object):
	"""
	This is the view of the Game State.

	Attibutes:
		cont: int, keep tracks of the frames.
	"""
	def __init__(self):
		"""
		Initialize self.
		"""
		super(GameView, self).__init__()
			
		self.T_winRes = (512, 448)
		self.spr_res= 32

		self.cont = 0

	def draw(self, Model, Assets, Draw):
		"""
		Draws the game.

		Args:
			Model: Model Class for Game State
			Assets: Assets Class
			Draw: Draw Class

		Returns:
			game_surface: pygame Surface.
		"""
		game_surface = pygame.Surface(self.T_winRes) # Makes a Surface using window size.

		game_surface = Draw.Map.drawMap(Model, Assets) # Uses Draw to draw the map on the surface.

		Draw.Objects.drawObjects(game_surface, Model.hero) # Uses Draw to draw the hero on the surface

		if Model.modelMenu.isOpen: # If Menu is Open:
			# Draw the menu
			game_surface.blit(Draw.Menu.drawMenu(), (game_surface.get_width()/2.66, game_surface.get_height()/2.66)) 
			
			# TODO
			# Draw text on this menu surface.

			# I made this for testing purposes.
			self.cont += 1

			if self.cont == 25:
				self.cont = 0

				if Model.modelMenu.navi == 0:
					print("RESUME GAME")
				else:
					print("QUIT TO MAIN MENU")
		
		return game_surface 
